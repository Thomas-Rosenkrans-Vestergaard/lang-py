# Generated from Calculator.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CalculatorParser import CalculatorParser
else:
    from antlr.CalculatorParser import CalculatorParser

# This class defines a complete listener for a parse tree produced by CalculatorParser.
class CalculatorListener(ParseTreeListener):

    # Enter a parse tree produced by CalculatorParser#program.
    def enterProgram(self, ctx:CalculatorParser.ProgramContext):
        pass

    # Exit a parse tree produced by CalculatorParser#program.
    def exitProgram(self, ctx:CalculatorParser.ProgramContext):
        pass


    # Enter a parse tree produced by CalculatorParser#statement.
    def enterStatement(self, ctx:CalculatorParser.StatementContext):
        pass

    # Exit a parse tree produced by CalculatorParser#statement.
    def exitStatement(self, ctx:CalculatorParser.StatementContext):
        pass


    # Enter a parse tree produced by CalculatorParser#command.
    def enterCommand(self, ctx:CalculatorParser.CommandContext):
        pass

    # Exit a parse tree produced by CalculatorParser#command.
    def exitCommand(self, ctx:CalculatorParser.CommandContext):
        pass


    # Enter a parse tree produced by CalculatorParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:CalculatorParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by CalculatorParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:CalculatorParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by CalculatorParser#signature.
    def enterSignature(self, ctx:CalculatorParser.SignatureContext):
        pass

    # Exit a parse tree produced by CalculatorParser#signature.
    def exitSignature(self, ctx:CalculatorParser.SignatureContext):
        pass


    # Enter a parse tree produced by CalculatorParser#functionParameters.
    def enterFunctionParameters(self, ctx:CalculatorParser.FunctionParametersContext):
        pass

    # Exit a parse tree produced by CalculatorParser#functionParameters.
    def exitFunctionParameters(self, ctx:CalculatorParser.FunctionParametersContext):
        pass


    # Enter a parse tree produced by CalculatorParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:CalculatorParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by CalculatorParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:CalculatorParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by CalculatorParser#constantDeclaration.
    def enterConstantDeclaration(self, ctx:CalculatorParser.ConstantDeclarationContext):
        pass

    # Exit a parse tree produced by CalculatorParser#constantDeclaration.
    def exitConstantDeclaration(self, ctx:CalculatorParser.ConstantDeclarationContext):
        pass


    # Enter a parse tree produced by CalculatorParser#expression.
    def enterExpression(self, ctx:CalculatorParser.ExpressionContext):
        pass

    # Exit a parse tree produced by CalculatorParser#expression.
    def exitExpression(self, ctx:CalculatorParser.ExpressionContext):
        pass


    # Enter a parse tree produced by CalculatorParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:CalculatorParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by CalculatorParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:CalculatorParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by CalculatorParser#multiplicativeOperator.
    def enterMultiplicativeOperator(self, ctx:CalculatorParser.MultiplicativeOperatorContext):
        pass

    # Exit a parse tree produced by CalculatorParser#multiplicativeOperator.
    def exitMultiplicativeOperator(self, ctx:CalculatorParser.MultiplicativeOperatorContext):
        pass


    # Enter a parse tree produced by CalculatorParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:CalculatorParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by CalculatorParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:CalculatorParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by CalculatorParser#additiveOperator.
    def enterAdditiveOperator(self, ctx:CalculatorParser.AdditiveOperatorContext):
        pass

    # Exit a parse tree produced by CalculatorParser#additiveOperator.
    def exitAdditiveOperator(self, ctx:CalculatorParser.AdditiveOperatorContext):
        pass


    # Enter a parse tree produced by CalculatorParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:CalculatorParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by CalculatorParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:CalculatorParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by CalculatorParser#parenthesizedExpression.
    def enterParenthesizedExpression(self, ctx:CalculatorParser.ParenthesizedExpressionContext):
        pass

    # Exit a parse tree produced by CalculatorParser#parenthesizedExpression.
    def exitParenthesizedExpression(self, ctx:CalculatorParser.ParenthesizedExpressionContext):
        pass


    # Enter a parse tree produced by CalculatorParser#functionExpression.
    def enterFunctionExpression(self, ctx:CalculatorParser.FunctionExpressionContext):
        pass

    # Exit a parse tree produced by CalculatorParser#functionExpression.
    def exitFunctionExpression(self, ctx:CalculatorParser.FunctionExpressionContext):
        pass


    # Enter a parse tree produced by CalculatorParser#functionArguments.
    def enterFunctionArguments(self, ctx:CalculatorParser.FunctionArgumentsContext):
        pass

    # Exit a parse tree produced by CalculatorParser#functionArguments.
    def exitFunctionArguments(self, ctx:CalculatorParser.FunctionArgumentsContext):
        pass


    # Enter a parse tree produced by CalculatorParser#variableExpression.
    def enterVariableExpression(self, ctx:CalculatorParser.VariableExpressionContext):
        pass

    # Exit a parse tree produced by CalculatorParser#variableExpression.
    def exitVariableExpression(self, ctx:CalculatorParser.VariableExpressionContext):
        pass


    # Enter a parse tree produced by CalculatorParser#literalExpression.
    def enterLiteralExpression(self, ctx:CalculatorParser.LiteralExpressionContext):
        pass

    # Exit a parse tree produced by CalculatorParser#literalExpression.
    def exitLiteralExpression(self, ctx:CalculatorParser.LiteralExpressionContext):
        pass


