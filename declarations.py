from antlr.LanguageListener import *
from antlr.LanguageVisitor import *
from value import eval_expression_literal


class Constant:

    def __init__(self, name, value, node):
        self.name = name
        self.value = value
        self.node = node


class UserFunction:

    def __init__(self, name, arguments, code):
        self.name = name
        self.arguments = arguments
        self.code = code

    def execute(self, arguments):
        pass


class NativeFunction:

    def __init__(self, name):
        self.name = name

    def execute(self, arguments):
        pass


class PrintFunction(NativeFunction):

    def __init__(self):
        super().__init__("print")

    def execute(self, arguments):
        for argument in arguments:
            print(argument.value)


class PrintLineFunction(NativeFunction):

    def __init__(self):
        super().__init__("print_ln")

    def execute(self, arguments):
        for argument in arguments:
            print(str(argument.value) + "\n")

class SymbolTable:

    def __init__(self, functions=None, constants=None):

        if functions is None:
            functions = {}
        if constants is None:
            constants = {}

        self._functions = functions
        self._constants = constants

    def get_declared_functions(self):
        return self._functions

    def get_declared_constants(self):
        return self._constants

    def get_declared_function(self, name):
        return self._functions.get(name)

    def get_declared_constant(self, name):
        found = self._constants.get(name)
        return found and found.value


class SymbolTablePopulator(LanguageListener):

    def __init__(self):
        self._functions = {}
        self._constants = {}

    def enterDeclarationFunction(self, ctx: LanguageParser.DeclarationFunctionContext):
        name = ctx.functionSignature().IDENTIFIER()
        self._functions[name] = UserFunction(name, self._get_function_arguments(ctx), self._get_function_code(ctx))

    @staticmethod
    def _get_function_arguments(ctx: LanguageParser.DeclarationFunctionContext):
        identifiers = ctx.functionSignature().functionParameters().IDENTIFIER()
        return list(map(lambda i: i.getText(), identifiers))

    @staticmethod
    def _get_function_code(ctx: LanguageParser.DeclarationFunctionContext):
        return ctx.functionBody()

    def enterDeclarationConstant(self, ctx: LanguageParser.DeclarationConstantContext):
        name = ctx.IDENTIFIER().getText()
        value = eval_expression_literal(ctx.expressionLiteral())
        self._constants[name] = Constant(name, value, ctx)

    def get_table(self):
        return SymbolTable(self._functions, self._constants)
