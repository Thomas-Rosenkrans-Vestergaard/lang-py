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


class TypeMismatchException(RuntimeException):

    def __init__(self, user_message, code=None, found=None, expected=None):
        super().__init__(user_message, code)
        self.type_one = found
        self.type_two = expected


class CodePiece:

    def __init__(self, description, code):
        self.description = description
        self.code = code