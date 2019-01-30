from antlr.LanguageVisitor import *
from declarations import SymbolTable, UserFunction, Constant
from exceptions import VariableRedeclarationException, TypeMismatchException, \
    UnknownFunctionException, UnknownReferenceExcpetion
from value import eval_expression_literal, Type, Value, get_type_of
from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker

from antlr.LanguageLexer import LanguageLexer
from antlr.LanguageParser import LanguageParser


class ProgramExecutor:

    def execute(self, code_text):
        lexer = LanguageLexer(InputStream(code_text))
        stream = CommonTokenStream(lexer)
        parser = LanguageParser(stream)
        tree = parser.program()
        executor = StatementExecutor(SymbolTable(), RuntimeStack())
        executor.visitProgram(tree)


class RuntimeStack:

    def __init__(self, initial_frames=None):
        if initial_frames is None:
            initial_frames = []
        self._frames = initial_frames

    def pop(self):
        self._frames.pop()

    def peek(self):
        return self._frames[-1]

    def push(self, frame):
        self._frames.append(frame)

    def find(self, variable_name):

        for frame in reversed(self._frames):
            value = frame.get_variable(variable_name)
            if value is not None:
                return value

        return None

    def set_variable(self, name, value):
        self.peek().set_variable(name, value)


class StatementExecutor(LanguageVisitor):

    def __init__(self, symbols: SymbolTable, stack: RuntimeStack):
        self._symbols = symbols
        self._stack = stack
        self._stack.push(Frame())

    def visitDeclarationFunction(self, ctx: LanguageParser.DeclarationFunctionContext):
        name = ctx.functionSignature().IDENTIFIER().getText()
        self._symbols.add_function(UserFunction(name, self._get_function_arguments(ctx), self._get_function_code(ctx)))

    @staticmethod
    def _get_function_arguments(ctx: LanguageParser.DeclarationFunctionContext):
        identifiers = ctx.functionSignature().functionParameters().IDENTIFIER()
        return list(map(lambda i: i.getText(), identifiers))

    @staticmethod
    def _get_function_code(ctx: LanguageParser.DeclarationFunctionContext):
        return ctx.codeBlock()

    def visitDeclarationConstant(self, ctx: LanguageParser.DeclarationConstantContext):
        name = ctx.IDENTIFIER().getText()
        value = eval_expression_literal(ctx.expressionLiteral())
        self._symbols.add_constant(Constant(name, value, ctx))

    def run_returnable(self, statements):
        for statement in statements:
            result = self.visitStatement(statement)
            if result is not None:
                return result

    def visitProgram(self, ctx: LanguageParser.ProgramContext):
        for declaration in ctx.declaration():
            self.visitDeclaration(declaration)

        for statement in ctx.statement():
            result = self.visitStatement(statement)
            if result is not None:
                return result

    def visitDeclaration(self, ctx: LanguageParser.DeclarationContext):
        self.visitChildren(ctx)

    def visitStatement(self, ctx: LanguageParser.StatementContext):

        if ctx.statementVariableDeclaration():
            return self.visitStatementVariableDeclaration(ctx.statementVariableDeclaration())
        if ctx.statementAssignment():
            return self.visitStatementAssignment(ctx.statementAssignment())
        if ctx.statementReturn():
            return self.visitStatementReturn(ctx.statementReturn())
        if ctx.statementIf():
            return self.visitStatementIf(ctx.statementIf())
        if ctx.statementFor():
            return self.visitStatementFor(ctx.statementFor())
        if ctx.statementWhile():
            return self.visitStatementWhile(ctx.statementWhile())
        if ctx.statementExpression():
            return self.visitStatementExpression(ctx.statementExpression())

    def visitStatementExpression(self, ctx: LanguageParser.StatementExpressionContext):
        self.visitExpression(ctx.expression())

    def visitStatementVariableDeclaration(self, ctx: LanguageParser.StatementVariableDeclarationContext):
        variable_name = ctx.IDENTIFIER().getText()
        if self._stack.find(variable_name) is not None:
            raise VariableRedeclarationException([], [])

        value = self.visitExpression(ctx.expression())
        self._stack.peek().set_variable(variable_name, value)

    def visitStatementAssignment(self, ctx: LanguageParser.StatementAssignmentContext):
        variable_name = ctx.IDENTIFIER().getText()
        variable = self._stack.find(variable_name)
        if variable is None:
            raise UnknownReferenceExcpetion(variable_name, None)

        expression_value = self.visitExpression(ctx.expression())
        variable.value = expression_value.value if expression_value is not None else Value(Type.NULL, None)

    def visitStatementFor(self, ctx: LanguageParser.StatementForContext):
        self.visitStatementVariableDeclaration(ctx.statementVariableDeclaration())
        ret = Value(Type.NULL, None)
        while True:

            conditional = self.visitExpression(ctx.statementExpression().expression())

            if conditional.type is not Type.BOOL:
                raise TypeMismatchException("For conditions must be type boolean", None, conditional.type,
                                            Type.BOOL)
            if conditional.value:
                ret = self.visitCodeBlock(ctx.codeBlock())
                if ret is not None:
                    ret = ret
                    break
                self.visitExpression(ctx.expression())
            else:
                break

        return ret

    def visitStatementIf(self, ctx: LanguageParser.StatementIfContext):
        conditional = self.visitExpression(ctx.expression())
        if conditional.type is not Type.BOOL:
            raise TypeMismatchException("If conditions must be type boolean", None, conditional.type, Type.BOOL)

        try:
            self._stack.push(Frame())
            if conditional.value:
                return self.visitCodeBlock(ctx.codeBlock())
            elif ctx.statementElse() is not None:
                return self.visitCodeBlock(ctx.statementElse().codeBlock())
        finally:
            self._stack.pop()

    def visitCodeBlock(self, ctx: LanguageParser.CodeBlockContext):
        stmts = ctx.statement()
        if isinstance(stmts, list):
            return self.run_returnable(stmts)

        return self.visitStatement(stmts)

    def visitStatementWhile(self, ctx: LanguageParser.StatementWhileContext):
        self._stack.push(Frame())

        try:
            while True:
                conditional = self.visitExpression(ctx.expression())
                if conditional.type is not Type.BOOL:
                    raise TypeMismatchException("If conditions must be type boolean", None, conditional.type, Type.BOOL)
                if conditional.value:
                    ret = self.visitCodeBlock(ctx.codeBlock())
                    if ret is not None:
                        return ret
                else:
                    return None
        finally:
            self._stack.pop()

    def visitStatementReturn(self, ctx: LanguageParser.StatementReturnContext):
        return self.visitExpression(ctx.expression())

    def visitExpression(self, ctx: LanguageParser.ExpressionContext):
        return self.visitExpressionOr(ctx.expressionOr())

    def visitExpressionOr(self, ctx: LanguageParser.ExpressionOrContext):

        if ctx.OR_OP() is not None:
            operand_one = self.visitExpressionOr(ctx.expressionOr())
            operand_two = self.visitExpressionAnd(ctx.expressionAnd())

            if operand_one.type is not Type.BOOL or operand_two.type is not Type.BOOL:
                raise TypeMismatchException("The or operator (||) can only be applied to values of type BOOL.", [])

            return Value(Type.BOOL, operand_one.value or operand_two.value)

        return self.visitExpressionAnd(ctx.expressionAnd())

    def visitExpressionAnd(self, ctx: LanguageParser.ExpressionAndContext):

        if ctx.AND_OP() is not None:
            operand_one = self.visitExpressionAnd(ctx.expressionAnd())
            operand_two = self.visitExpressionEquality(ctx.expressionEquality())

            if operand_one.type is not Type.BOOL or operand_two.type is not Type.BOOL:
                raise TypeMismatchException("The and operator (&&) can only be applied to values of type BOOL.", [])

            return Value(Type.BOOL, operand_one.value and operand_two.value)

        return self.visitExpressionEquality(ctx.expressionEquality())

    def visitExpressionEquality(self, ctx: LanguageParser.ExpressionEqualityContext):

        if ctx.EQ_OP() or ctx.NEQ_OP():
            operand_one = self.visitExpressionEquality(ctx.expressionEquality())
            operand_two = self.visitExpressionRelational(ctx.expressionRelational())

            if ctx.EQ_OP():
                result = operand_one.value == operand_two.value
            else:  # NOT EQ
                result = operand_one.value != operand_two.value

            return Value(Type.BOOL, result)

        return self.visitExpressionRelational(ctx.expressionRelational())

    def visitExpressionRelational(self, ctx: LanguageParser.ExpressionRelationalContext):

        expression_additive = ctx.expressionAdditive()

        if ctx.LT_OP() or ctx.GT_OP() or ctx.LTOE_OP() or ctx.GTOE_OP():
            operand_one = self.visitExpressionRelational(ctx.expressionRelational())
            operand_two = self.visitExpressionAdditive(expression_additive)

            if operand_one.type is not Type.NUMBER or operand_two.type is not Type.NUMBER:
                raise TypeMismatchException("The relational operators can only be applied to values of type NUMBER.")

            if ctx.LT_OP():
                result = operand_one.value < operand_two.value
            elif ctx.GT_OP():
                result = operand_one.value > operand_two.value
            elif ctx.LTOE_OP():
                result = operand_one.value <= operand_two.value
            elif ctx.GTOE_OP():
                result = operand_one.value >= operand_two.value
            else:
                raise Exception()

            return Value(Type.BOOL, result)

        return self.visitExpressionAdditive(expression_additive)

    def visitExpressionAdditive(self, ctx: LanguageParser.ExpressionAdditiveContext):
        if ctx.ADD_OP() or ctx.SUB_OP():
            operand_one = self.visitExpressionAdditive(ctx.expressionAdditive())
            operand_two = self.visitExpressionMultiplicative(ctx.expressionMultiplicative())

            if operand_one.type is not Type.NUMBER or operand_two.type is not Type.NUMBER:
                raise TypeMismatchException("The additive operators can only be applied to values of type NUMBER.")

            if ctx.ADD_OP():
                result = operand_one.value + operand_two.value
            else:  # SUB
                result = operand_one.value - operand_two.value

            return Value(Type.NUMBER, result)

        return self.visitExpressionMultiplicative(ctx.expressionMultiplicative())

    def visitExpressionMultiplicative(self, ctx: LanguageParser.ExpressionMultiplicativeContext):
        if ctx.MUL_OP() or ctx.DIV_OP() or ctx.MOD_OP() or ctx.EXP_OP():
            operand_one = self.visitExpressionMultiplicative(ctx.expressionMultiplicative())
            operand_two = self.visitExpressionUnary(ctx.expressionUnary())

            if operand_one.type is not Type.NUMBER or operand_two.type is not Type.NUMBER:
                raise TypeMismatchException(
                    "The multiplicative operators can only be applied to values of type NUMBER.")

            if ctx.MUL_OP():
                result = operand_one.value * operand_two.value
            elif ctx.DIV_OP():
                result = operand_one.value / operand_two.value
            elif ctx.MOD_OP():
                result = operand_one.value % operand_two.value
            elif ctx.EXP_OP():
                result = operand_one.value ** operand_two.value
            else:
                raise Exception()

            return Value(Type.NUMBER, result)

        return self.visitExpressionUnary(ctx.expressionUnary())

    def visitExpressionUnary(self, ctx: LanguageParser.ExpressionUnaryContext):

        if ctx.NOT_OP():
            operand = self.visitExpressionPrimary(ctx.expressionPrimary())
            if operand.type is not Type.BOOL:
                raise TypeMismatchException("The not operator (!) can only be applied to values of type BOOL.")

            return Value(Type.BOOL, not operand.value)

        if ctx.TYPE():
            operand = self.visitExpressionPrimary(ctx.expressionPrimary())
            return Value(Type.STRING, operand.get_type_name())

        if ctx.DEC_OP():
            operand = self.visitExpressionPrimary(ctx.expressionPrimary())
            if operand.type is not Type.NUMBER:
                raise TypeMismatchException("The not dec (--) can only be applied to values of type NUMBER.")

            operand.value = operand.value - 1
            return operand

        if ctx.INC_OP():
            operand = self.visitExpressionPrimary(ctx.expressionPrimary())
            if operand.type is not Type.NUMBER:
                raise TypeMismatchException("The not dec (++) can only be applied to values of type NUMBER.")

            operand.value = operand.value + 1
            return operand

        return self.visitExpressionPrimary(ctx.expressionPrimary())

    def visitExpressionPrimary(self, ctx: LanguageParser.ExpressionPrimaryContext):

        expression_paren = ctx.expressionParenthesized()
        if expression_paren is not None:
            return self.visitExpressionParenthesized(expression_paren)

        expression_func = ctx.expressionFunction()
        if expression_func is not None:
            return self.visitExpressionFunction(expression_func)

        expression_var = ctx.expressionVariable()
        if expression_var is not None:
            return self.visitExpressionVariable(expression_var)

        expression_list = ctx.expressionList()
        if expression_list is not None:
            return self.visitExpressionList(expression_list)

        expression_map = ctx.expressionMap()
        if expression_map is not None:
            return self.visitExpressionMap(expression_map)

        expression_lit = ctx.expressionLiteral()
        if expression_lit is not None:
            return self.visitExpressionLiteral(expression_lit)

        field_access = ctx.expressionFieldAccess()
        if field_access is not None:
            raise Exception("Unsupported")

        method_access = ctx.expressionMethodAccess()
        if method_access is not None:
            raise Exception("Unsupported")

        bracket_access = ctx.expressionBracketAccess()
        if bracket_access is not None:
            subject = self.visitExpressionPrimary(ctx.expressionPrimary())
            if subject.type != Type.LIST and subject.type != Type.MAP:
                raise TypeMismatchException("[] applied to invalid value.")
            index = self.visitExpression(bracket_access.expression())
            if subject.type == Type.LIST and index.type != Type.NUMBER:
                raise TypeMismatchException("List index must be number", None, index.type, Type.Number)
            if subject.type == Type.LIST:
                value = subject.value[int(index.value)].value
            else:
                value = subject.value[index.value].value

            return Value(get_type_of(value), value)

    def visitExpressionParenthesized(self, ctx: LanguageParser.ExpressionParenthesizedContext):
        return self.visitExpression(ctx.expression())

    def visitExpressionFunction(self, ctx: LanguageParser.ExpressionFunctionContext):
        function_name = ctx.IDENTIFIER().getText()
        function = self._symbols.get_declared_function(function_name)
        if function is None:
            raise UnknownFunctionException(function_name, [])

        arguments = map(lambda expression: self.visitExpression(expression), ctx.arguments().expression())

        if isinstance(function, UserFunction):
            new_frame = Frame()
            new_frame.set_variables(zip(function.parameters, arguments))
            self._stack.push(new_frame)
            result = self.visitCodeBlock(function.code)
            self._stack.pop()
            return result

        return function.execute(arguments)

    def visitExpressionVariable(self, ctx: LanguageParser.ExpressionVariableContext):
        variable_name = ctx.IDENTIFIER().getText()
        found_variable = self._stack.find(variable_name)
        if found_variable is None:
            raise UnknownReferenceExcpetion(variable_name, [])

        return found_variable

    def visitExpressionList(self, ctx: LanguageParser.ExpressionListContext):
        new_array = []
        for expression in ctx.expression():
            new_array.append(self.visitExpression(expression))

        return Value(Type.LIST, new_array)

    def visitExpressionMap(self, ctx: LanguageParser.ExpressionMapContext):
        new_map = {}
        entries = ctx.expressionMapEntry()
        for entry in entries:
            expressions = entry.expression()
            key = self.visitExpression(expressions[0]).value
            val = self.visitExpression(expressions[1])
            new_map[key] = val

        return Value(Type.MAP, new_map)

    def visitExpressionLiteral(self, ctx: LanguageParser.ExpressionLiteralContext):
        return eval_expression_literal(ctx)


class Frame:

    def __init__(self):
        self._variables = {}

    def set_variable(self, name, value):
        self._variables[name] = value

    def get_variable(self, name):
        return self._variables.get(name)

    def set_variables(self, variables):
        for k, v in variables:
            self.set_variable(k, v)
