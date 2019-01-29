from enum import Enum
from antlr.LanguageParser import *
from exceptions import InternalException


class Type(Enum):
    NUMBER = 0
    STRING = 1
    BOOL = 2
    NULL = 3
    LIST = 4
    MAP = 5


class Value:

    def __init__(self, type: Type, value):
        self.type = type
        self.value = value

    def to_string(self):
        if self.type == Type.BOOL:
            return "true" if self.value else "false"
        return str(self.value)

    def get_type_name(self):

        type_names = [
            "number",
            "string",
            "bool",
            "null",
            "list",
            "map",
        ]

        return type_names[self.type.value]


def eval_expression_literal(ctx: LanguageParser.ExpressionLiteralContext):
    bool_value = ctx.BOOL_VAL()
    string_value = ctx.STRING_VAL()
    number_value = ctx.NUMBER_VAL()
    null_value = ctx.NULL()

    if bool_value is not None:
        return bool_literal_to_value(bool_value)

    if string_value is not None:
        return string_literal_to_value(string_value)

    if number_value is not None:
        return number_literal_to_value(number_value)

    if null_value is not None:
        return Value(Type.NULL, None)

    raise InternalException("Unknown value type.", [])


def bool_literal_to_value(ctx):
    return Value(Type.BOOL, ctx.getText() == "true")


def string_literal_to_value(ctx):
    return Value(Type.STRING, ctx.getText()[1:-1])


def number_literal_to_value(ctx):
    return Value(Type.NUMBER, float(ctx.getText()))

