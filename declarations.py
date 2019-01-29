from antlr.LanguageListener import *
from antlr.LanguageVisitor import *
from value import eval_expression_literal


class Constant:

    def __init__(self, name, value, node):
        self.name = name
        self.value = value
        self.node = node


class UserFunction:

    def __init__(self, name, parameters, code):
        self.name = name
        self.parameters = parameters
        self.code = code


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
            print(argument.to_string(), end="")


class PrintLineFunction(NativeFunction):

    def __init__(self):
        super().__init__("print_ln")

    def execute(self, arguments):
        for argument in arguments:
            print(str(argument.to_string()))


class SymbolTable:

    def __init__(self, functions=None, constants=None):

        if functions is None:
            functions = {}
        if constants is None:
            constants = {}

        self._functions = functions
        self._constants = constants

        self.add_function(PrintFunction())
        self.add_function(PrintLineFunction())

    def add_function(self, function):
        self._functions[function.name] = function

    def get_declared_functions(self):
        return self._functions

    def get_declared_constants(self):
        return self._constants

    def get_declared_function(self, name):
        return self._functions.get(name)

    def get_declared_constant(self, name):
        found = self._constants.get(name)
        return found and found.value

    def add_constant(self, constant):
        self._constants[constant] = constant
