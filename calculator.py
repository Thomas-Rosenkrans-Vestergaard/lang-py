from antlr import *


class CalculatorException(Exception):

    def __init__(self, user_message):
        self.user_message = user_message


class SourceCodeException(CalculatorException):

    def __init__(self, user_message, code):
        super().__init__(user_message)
        self.code = code


class ParsingException(SourceCodeException):

    def __init__(self, user_message, code):
        super().__init__(user_message, code)


class SyntaxException(ParsingException):

    def __int__(self, user_message, code):
        super().__init__(user_message, code)


class ExecutionException(SourceCodeException):

    def __init__(self, user_message, code):
        super().__init__(user_message, code)


class CalculatorState:

    def __int__(self):
        self.functions = {}
        self.frames = []

    def new_frame(self, previous):


    def add_function(self, function):
        self.functions[function.name]


class Frame:

    def __init__(self, parent = None):
        self.parent = parent
        self.variables = {}
        self.constants = {}

    def set_constant(self, name, value):
        if self.constants.get(name) is not None:
            raise Exception("Cannot change constants")

        self.constants[name] = value

    def get_constant(self, name):
        if self.parent is None:
            return self.variables.get(name)

        return self.variables.get(name) or self.parent.get_constant(name)

    def set_variable(self, name, value):
        self.variables[name] = value

    def get_variable(self, name):
        pass

    def get_variables(self):
        pass

    def get_constants(self):
        pass


class Function:

    def __con


class SourceFunction(Function):
    pass


class PredefinedFunction(Function):
    pass


class Collector:
    pass


class Executor:
    pass
