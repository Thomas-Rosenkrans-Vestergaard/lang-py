from antlr.LanguageVisitor import *
from declarations import SymbolTable
from exceptions import VariableRedeclarationException, TypeMismatchException, \
    UnknownFunctionException, UnknownReferenceExcpetion
from value import eval_expression_literal, Type, Value
from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker

from antlr.LanguageLexer import LanguageLexer
from antlr.LanguageParser import LanguageParser
from declarations import SymbolTablePopulator


class ProgramExecutor:

    def execute(self, code_text):
        lexer = LanguageLexer(InputStream(code_text))
        stream = CommonTokenStream(lexer)
        parser = LanguageParser(stream)
        populator = SymbolTablePopulator()
        walker = ParseTreeWalker()
        tree = parser.program()
        walker.walk(populator, tree)
        symbol_table = populator.get_table()

        print("functions")
        for name, func in symbol_table.get_declared_functions().items():
            print(func.name)
            print(func.arguments)
            print(func.code)

        print("constants")
        for name, constant in symbol_table.get_declared_constants().items():
            print("{}, {}, {}".format(name, constant.value.type, constant.value.value))

        print("exec")
        executor = StatementExecutor(symbol_table, RuntimeStack())
        executor.visitProgram(tree)


class RuntimeStack:

    def __init__(self, initial_frames=[]):
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


class StatementExecutor(LanguageVisitor):

    def __init__(self, symbols: SymbolTable, stack: RuntimeStack):
        self._symbols = symbols
        self._stack = stack
        self._stack.push(Frame())

    def visitProgram(self, ctx: LanguageParser.ProgramContext):
        for statement in ctx.statement():
            result = self.visitStatement(statement)
            if result is not None:
                return result

    def visitFunctionBody(self, ctx: LanguageParser.FunctionBodyContext):
        for statement in ctx.statement():
            result = self.visitStatement(statement)
            if result is not None:
                return result

    def visitStatementExpression(self, ctx: LanguageParser.StatementExpressionContext):
        self.visitExpression(ctx.expression())

    def visitStatementVariableDeclaration(self, ctx: LanguageParser.StatementVariableDeclarationContext):
        variable_name = ctx.IDENTIFIER().getText()
        if self._stack.find(variable_name) is not None:
            raise VariableRedeclarationException([], [])

        self._stack.peek().set_variable(variable_name, self.visitExpression(ctx.expression()))

    def visitStatementFor(self, ctx: LanguageParser.StatementForContext):
        self.visitStatementVariableDeclaration(ctx.statementVariableDeclaration())
        self._stack.pop()

    def visitStatementIf(self, ctx: LanguageParser.StatementIfContext):
        conditional = self.visitExpression(ctx.expression())
        if conditional.type is not Type.BOOL:
            raise TypeMismatchException("If conditions must be type boolean", None, conditional.type, Type.BOOL)

        self._stack.push(Frame())
        if conditional.value:
            self.visitCodeBlock(ctx.codeBlock())
        elif ctx.statementElse() is not None:
            self.visitStatement(ctx.statementElse().codeBlock())
        self._stack.pop()

    def visitStatementWhile(self, ctx: LanguageParser.StatementWhileContext):
        self._stack.push(Frame())

        while True:
            conditional = self.visitExpression(ctx.expression())
            if conditional.type is not Type.BOOL:
                raise TypeMismatchException("If conditions must be type boolean", None, conditional.type, Type.BOOL)
            
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
            elif ctx.NEQ_OP():
                result = operand_one.value != operand_two.value

            return Value(Type.BOOL, result)

        return self.visitExpressionRelational(ctx.expressionRelational())

    def visitExpressionRelational(self, ctx: LanguageParser.ExpressionRelationalContext):

        expression_multiplicative = ctx.expressionMultiplicative()

        if ctx.LT_OP() or ctx.GT_OP() or ctx.LTOE_OP() or ctx.GTOE_OP():
            operand_one = self.visitExpressionRelational(ctx.expressionRelational())
            operand_two = self.visitExpressionMultiplicative(expression_multiplicative)

            if operand_one.type is not Type.NUMBER or operand_two.type is not Type.NUMBER:
                raise TypeMismatchException("The relational operators can only be applied to values of type NUMBER.",
                                            [])

            if ctx.LT_OP():
                result = operand_one.value < operand_two.value
            elif ctx.GT_OP():
                result = operand_one.value > operand_two.value
            elif ctx.LTOE_OP():
                result = operand_one.value <= operand_two.value
            elif ctx.GTOE_OP():
                result = operand_one.value >= operand_two.value

            return Value(Type.BOOL, result)

        return self.visitExpressionMultiplicative(expression_multiplicative)


    def visitExpressionMultiplicative(self, ctx: LanguageParser.ExpressionMultiplicativeContext):
        if ctx.MUL_OP() or ctx.DIV_OP() or ctx.MOD_OP() or ctx.EXP_OP():
            operand_one = self.visitExpressionMultiplicative(ctx.expressionMultiplicative())
            operand_two = self.visitExpressionAdditive(ctx.expressionAdditive())

            if operand_one.type is not Type.NUMBER or operand_two.type is not Type.NUMBER:
                raise TypeMismatchException(
                    "The multiplicative operators can only be applied to values of type NUMBER.", [])

            if ctx.MUL_OP():
                result = operand_one.value * operand_two.value
            elif ctx.DIV_OP():
                result = operand_one.value / operand_two.value
            elif ctx.MOD_OP():
                result = operand_one.value % operand_two.value
            elif ctx.EXP_OP():
                result = operand_one.value ** operand_two.value

            return Value(Type.NUMBER, result)

        return self.visitExpressionAdditive(ctx.expressionAdditive())


    def visitExpressionAdditive(self, ctx: LanguageParser.ExpressionAdditiveContext):
        if ctx.ADD_OP() or ctx.SUB_OP():
            operand_one = self.visitExpressionAdditive(ctx.expressionAdditive())
            operand_two = self.visitExpressionUnary(ctx.expressionUnary())

            if operand_one.type is not Type.NUMBER or operand_two.type is not Type.NUMBER:
                raise TypeMismatchException("The additive operators can only be applied to values of type NUMBER.",
                                            [])

            if ctx.ADD_OP():
                result = operand_one.value + operand_two.value
            elif ctx.SUB_OP():
                result = operand_one.value - operand_two.value

            return Value(Type.NUMBER, result)

        return self.visitExpressionUnary(ctx.expressionUnary())


    def visitExpressionUnary(self, ctx: LanguageParser.ExpressionUnaryContext):
        if ctx.NOT_OP():
            operand = self.visitExpressionPrimary(ctx.expressionPrimary())
            if operand.type is not Type.BOOL:
                raise TypeMismatchException("The not operator (!) can only be applied to values of type BOOL.", [])

            return Value(Type.BOOL, not operand.value)

        if ctx.TYPE():
            operand = self.visitExpressionPrimary(ctx.expressionPrimary())
            return "{}".format(operand.type)[5:]

        if ctx.DEC_OP():
            operand = self.visitExpressionPrimary(ctx.expressionPrimary())
            if operand.type is not Type.NUMBER:
                raise TypeMismatchException("The not dec (--) can only be applied to values of type NUMBER.", [])

            return Value(Type.BOOL, --operand.value)

        if ctx.INC_OP():
            operand = self.visitExpressionPrimary(ctx.expressionPrimary())
            if operand.type is not Type.NUMBER:
                raise TypeMismatchException("The not dec (++) can only be applied to values of type NUMBER.", [])

            return Value(Type.BOOL, ++operand.value)

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

        expression_lit = ctx.expressionList()
        if expression_lit is not None:
            return self.visitExpressionLiteral(expression_lit)

        expression_dot_acc = ctx.expressionDotAccess()
        if expression_dot_acc is not None:
            pass
            # return self.visitExpressionDotAccess(expression_dot_acc)

        expression_array_acc = ctx.expressionArrayAccess()
        if expression_array_acc is not None:
            pass
            # return self.visitExpressionArrayAccess(expression_array_acc)


    def visitExpressionParenthesized(self, ctx: LanguageParser.ExpressionParenthesizedContext):
        return self.visitExpression(ctx.expression())


    def visitExpressionFunction(self, ctx: LanguageParser.ExpressionFunctionContext):
        function_name = ctx.IDENTIFIER().getText()
        function = self._symbols.get_declared_function(function_name)
        if function is None:
            raise UnknownFunctionException(function_name, [])

        return


    def visitExpressionVariable(self, ctx: LanguageParser.ExpressionVariableContext):
        variable_name = ctx.IDENTIFIER().getText()
        found_variable = self._stack.find(variable_name)
        if found_variable is None:
            raise UnknownReferenceExcpetion(variable_name, [])
        return found_variable


    def visitExpressionList(self, ctx: LanguageParser.ExpressionListContext):
        new_array = []
        expressions = ctx.expression()
        for expression in expressions.items():
            new_array.append(self.visitExpression(expression))

        return Value(Type.LIST, new_array)


    def visitExpressionMap(self, ctx: LanguageParser.ExpressionMapContext):
        new_map = {}
        entries = ctx.expressionMapEntry()
        for entry in entries:
            key = entry.IDENTIFIER().getText()
            val = self.visitExpression(entry.expression())
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
        self._variables.get(name)
