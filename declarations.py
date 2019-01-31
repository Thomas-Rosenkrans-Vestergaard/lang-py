from value import Value, Type


class Field:

    def __init__(self, name, default_expression):
        self.name = name
        self.default_expression = default_expression


class Class:

    def __init__(self, name, constructor, methods, fields):
        self.name = name
        self.constructor = constructor
        self.methods = methods
        self.fields = fields


class Method:

    def __init__(self, parameters, code_block):
        self.parameters = parameters
        self.code = code_block


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
        raise Exception("Not implemented")


class SizeFunction(NativeFunction):

    def __init__(self):
        super().__init__("size")

    def execute(self, arguments):
        sum_size = 0
        for argument in arguments:
            sum_size = sum_size + self.size_of(argument)

        return Value(Type.NUMBER, sum_size)

    @staticmethod
    def size_of(value):
        return len(value.value)


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

    def __init__(self, functions=None, constants=None, classes=None):

        if functions is None:
            functions = {}
        if constants is None:
            constants = {}
        if classes is None:
            classes = {}

        self._functions = functions
        self._constants = constants
        self._classes = classes

        self.add_function(PrintFunction())
        self.add_function(PrintLineFunction())
        self.add_function(SizeFunction())

    def add_function(self, function):
        self._functions[function.name] = function

    def get_declared_function(self, name):
        return self._functions.get(name)

    def get_declared_constant(self, name):
        found = self._constants.get(name)
        return found and found.value

    def add_constant(self, constant):
        self._constants[constant.name] = constant

    def add_class(self, clazz):
        self._classes[clazz.name] = clazz

    def get_declared_class(self, class_name):
        return self._classes[class_name]
