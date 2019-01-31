class LanguageException(Exception):

    def __init__(self, user_message, code):
        self.user_message = user_message


class InternalException(LanguageException):

    def __init__(self, user_message, code):
        super().__init__(user_message, code)


class ProgramException(LanguageException):

    def __int__(self, user_message, code):
        super().__init__(user_message)
        self.code = code


class SyntaxException(ProgramException):

    def __int__(self, user_message, code):
        super().__init__(user_message, code)


class RuntimeException(ProgramException):

    def __init__(self, user_message, code):
        super().__init__(user_message, code)


class VariableRedeclarationException(ProgramException):

    def __init__(self, variable_name, code):
        super().__init__("Cannot redeclare variable " + variable_name, code)


class UnknownReferenceExcpetion(RuntimeException):
    def __init__(self, variable_name, code):
        super().__init__("Reference with name " + variable_name + " not in scope", code)


class UnknownFunctionException(RuntimeException):

    def __init__(self, function_name, code):
        super().__init__("Unknown function with name " + function_name, code)


class UnknownClassException(RuntimeException):

    def __init__(self, class_name, code=None):
        super().__init__("Unknown class with name " + class_name, code)


class TypeMismatchException(RuntimeException):

    def __init__(self, user_message, code=None, found=None, expected=None):
        super().__init__(user_message, code)
        self.type_one = found
        self.type_two = expected


class NullPointerException(RuntimeException):

    def __init__(self, user_message, code=None):
        super().__init__(user_message, code)


class UnknownMethodException(RuntimeException):

    def __init__(self, value, method_name, code=None):
        super().__init__("Type " + value.get_type_name() + " does not have method " + method_name)
        self.value = value
        self.method_name = method_name
        self.code = code


class UnknownFieldException(RuntimeException):

    def __init__(self, value, field_name, code=None):
        super().__init__("Type " + value.get_type_name() + " does not have field " + field_name, code)
        self.value = value
        self.field_name = field_name
        self.code = code
