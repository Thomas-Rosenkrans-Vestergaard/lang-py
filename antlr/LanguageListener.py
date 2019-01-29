# Generated from Language.g4 by ANTLR 4.7.2
from antlr4 import *
from .LanguageParser import LanguageParser

# This class defines a complete listener for a parse tree produced by LanguageParser.
class LanguageListener(ParseTreeListener):

    # Enter a parse tree produced by LanguageParser#program.
    def enterProgram(self, ctx:LanguageParser.ProgramContext):
        pass

    # Exit a parse tree produced by LanguageParser#program.
    def exitProgram(self, ctx:LanguageParser.ProgramContext):
        pass


    # Enter a parse tree produced by LanguageParser#declaration.
    def enterDeclaration(self, ctx:LanguageParser.DeclarationContext):
        pass

    # Exit a parse tree produced by LanguageParser#declaration.
    def exitDeclaration(self, ctx:LanguageParser.DeclarationContext):
        pass


    # Enter a parse tree produced by LanguageParser#declarationConstant.
    def enterDeclarationConstant(self, ctx:LanguageParser.DeclarationConstantContext):
        pass

    # Exit a parse tree produced by LanguageParser#declarationConstant.
    def exitDeclarationConstant(self, ctx:LanguageParser.DeclarationConstantContext):
        pass


    # Enter a parse tree produced by LanguageParser#declarationFunction.
    def enterDeclarationFunction(self, ctx:LanguageParser.DeclarationFunctionContext):
        pass

    # Exit a parse tree produced by LanguageParser#declarationFunction.
    def exitDeclarationFunction(self, ctx:LanguageParser.DeclarationFunctionContext):
        pass


    # Enter a parse tree produced by LanguageParser#functionBody.
    def enterFunctionBody(self, ctx:LanguageParser.FunctionBodyContext):
        pass

    # Exit a parse tree produced by LanguageParser#functionBody.
    def exitFunctionBody(self, ctx:LanguageParser.FunctionBodyContext):
        pass


    # Enter a parse tree produced by LanguageParser#functionSignature.
    def enterFunctionSignature(self, ctx:LanguageParser.FunctionSignatureContext):
        pass

    # Exit a parse tree produced by LanguageParser#functionSignature.
    def exitFunctionSignature(self, ctx:LanguageParser.FunctionSignatureContext):
        pass


    # Enter a parse tree produced by LanguageParser#functionParameters.
    def enterFunctionParameters(self, ctx:LanguageParser.FunctionParametersContext):
        pass

    # Exit a parse tree produced by LanguageParser#functionParameters.
    def exitFunctionParameters(self, ctx:LanguageParser.FunctionParametersContext):
        pass


    # Enter a parse tree produced by LanguageParser#statement.
    def enterStatement(self, ctx:LanguageParser.StatementContext):
        pass

    # Exit a parse tree produced by LanguageParser#statement.
    def exitStatement(self, ctx:LanguageParser.StatementContext):
        pass


    # Enter a parse tree produced by LanguageParser#statementVariableDeclaration.
    def enterStatementVariableDeclaration(self, ctx:LanguageParser.StatementVariableDeclarationContext):
        pass

    # Exit a parse tree produced by LanguageParser#statementVariableDeclaration.
    def exitStatementVariableDeclaration(self, ctx:LanguageParser.StatementVariableDeclarationContext):
        pass


    # Enter a parse tree produced by LanguageParser#statementReturn.
    def enterStatementReturn(self, ctx:LanguageParser.StatementReturnContext):
        pass

    # Exit a parse tree produced by LanguageParser#statementReturn.
    def exitStatementReturn(self, ctx:LanguageParser.StatementReturnContext):
        pass


    # Enter a parse tree produced by LanguageParser#statementIf.
    def enterStatementIf(self, ctx:LanguageParser.StatementIfContext):
        pass

    # Exit a parse tree produced by LanguageParser#statementIf.
    def exitStatementIf(self, ctx:LanguageParser.StatementIfContext):
        pass


    # Enter a parse tree produced by LanguageParser#statementElse.
    def enterStatementElse(self, ctx:LanguageParser.StatementElseContext):
        pass

    # Exit a parse tree produced by LanguageParser#statementElse.
    def exitStatementElse(self, ctx:LanguageParser.StatementElseContext):
        pass


    # Enter a parse tree produced by LanguageParser#statementFor.
    def enterStatementFor(self, ctx:LanguageParser.StatementForContext):
        pass

    # Exit a parse tree produced by LanguageParser#statementFor.
    def exitStatementFor(self, ctx:LanguageParser.StatementForContext):
        pass


    # Enter a parse tree produced by LanguageParser#statementWhile.
    def enterStatementWhile(self, ctx:LanguageParser.StatementWhileContext):
        pass

    # Exit a parse tree produced by LanguageParser#statementWhile.
    def exitStatementWhile(self, ctx:LanguageParser.StatementWhileContext):
        pass


    # Enter a parse tree produced by LanguageParser#codeBlock.
    def enterCodeBlock(self, ctx:LanguageParser.CodeBlockContext):
        pass

    # Exit a parse tree produced by LanguageParser#codeBlock.
    def exitCodeBlock(self, ctx:LanguageParser.CodeBlockContext):
        pass


    # Enter a parse tree produced by LanguageParser#statementExpression.
    def enterStatementExpression(self, ctx:LanguageParser.StatementExpressionContext):
        pass

    # Exit a parse tree produced by LanguageParser#statementExpression.
    def exitStatementExpression(self, ctx:LanguageParser.StatementExpressionContext):
        pass


    # Enter a parse tree produced by LanguageParser#expression.
    def enterExpression(self, ctx:LanguageParser.ExpressionContext):
        pass

    # Exit a parse tree produced by LanguageParser#expression.
    def exitExpression(self, ctx:LanguageParser.ExpressionContext):
        pass


    # Enter a parse tree produced by LanguageParser#expressionOr.
    def enterExpressionOr(self, ctx:LanguageParser.ExpressionOrContext):
        pass

    # Exit a parse tree produced by LanguageParser#expressionOr.
    def exitExpressionOr(self, ctx:LanguageParser.ExpressionOrContext):
        pass


    # Enter a parse tree produced by LanguageParser#expressionAnd.
    def enterExpressionAnd(self, ctx:LanguageParser.ExpressionAndContext):
        pass

    # Exit a parse tree produced by LanguageParser#expressionAnd.
    def exitExpressionAnd(self, ctx:LanguageParser.ExpressionAndContext):
        pass


    # Enter a parse tree produced by LanguageParser#expressionEquality.
    def enterExpressionEquality(self, ctx:LanguageParser.ExpressionEqualityContext):
        pass

    # Exit a parse tree produced by LanguageParser#expressionEquality.
    def exitExpressionEquality(self, ctx:LanguageParser.ExpressionEqualityContext):
        pass


    # Enter a parse tree produced by LanguageParser#expressionRelational.
    def enterExpressionRelational(self, ctx:LanguageParser.ExpressionRelationalContext):
        pass

    # Exit a parse tree produced by LanguageParser#expressionRelational.
    def exitExpressionRelational(self, ctx:LanguageParser.ExpressionRelationalContext):
        pass


    # Enter a parse tree produced by LanguageParser#expressionMultiplicative.
    def enterExpressionMultiplicative(self, ctx:LanguageParser.ExpressionMultiplicativeContext):
        pass

    # Exit a parse tree produced by LanguageParser#expressionMultiplicative.
    def exitExpressionMultiplicative(self, ctx:LanguageParser.ExpressionMultiplicativeContext):
        pass


    # Enter a parse tree produced by LanguageParser#expressionAdditive.
    def enterExpressionAdditive(self, ctx:LanguageParser.ExpressionAdditiveContext):
        pass

    # Exit a parse tree produced by LanguageParser#expressionAdditive.
    def exitExpressionAdditive(self, ctx:LanguageParser.ExpressionAdditiveContext):
        pass


    # Enter a parse tree produced by LanguageParser#expressionUnary.
    def enterExpressionUnary(self, ctx:LanguageParser.ExpressionUnaryContext):
        pass

    # Exit a parse tree produced by LanguageParser#expressionUnary.
    def exitExpressionUnary(self, ctx:LanguageParser.ExpressionUnaryContext):
        pass


    # Enter a parse tree produced by LanguageParser#expressionPrimary.
    def enterExpressionPrimary(self, ctx:LanguageParser.ExpressionPrimaryContext):
        pass

    # Exit a parse tree produced by LanguageParser#expressionPrimary.
    def exitExpressionPrimary(self, ctx:LanguageParser.ExpressionPrimaryContext):
        pass


    # Enter a parse tree produced by LanguageParser#expressionDotAccess.
    def enterExpressionDotAccess(self, ctx:LanguageParser.ExpressionDotAccessContext):
        pass

    # Exit a parse tree produced by LanguageParser#expressionDotAccess.
    def exitExpressionDotAccess(self, ctx:LanguageParser.ExpressionDotAccessContext):
        pass


    # Enter a parse tree produced by LanguageParser#expressionArrayAccess.
    def enterExpressionArrayAccess(self, ctx:LanguageParser.ExpressionArrayAccessContext):
        pass

    # Exit a parse tree produced by LanguageParser#expressionArrayAccess.
    def exitExpressionArrayAccess(self, ctx:LanguageParser.ExpressionArrayAccessContext):
        pass


    # Enter a parse tree produced by LanguageParser#expressionList.
    def enterExpressionList(self, ctx:LanguageParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by LanguageParser#expressionList.
    def exitExpressionList(self, ctx:LanguageParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by LanguageParser#expressionMap.
    def enterExpressionMap(self, ctx:LanguageParser.ExpressionMapContext):
        pass

    # Exit a parse tree produced by LanguageParser#expressionMap.
    def exitExpressionMap(self, ctx:LanguageParser.ExpressionMapContext):
        pass


    # Enter a parse tree produced by LanguageParser#expressionMapEntry.
    def enterExpressionMapEntry(self, ctx:LanguageParser.ExpressionMapEntryContext):
        pass

    # Exit a parse tree produced by LanguageParser#expressionMapEntry.
    def exitExpressionMapEntry(self, ctx:LanguageParser.ExpressionMapEntryContext):
        pass


    # Enter a parse tree produced by LanguageParser#expressionParenthesized.
    def enterExpressionParenthesized(self, ctx:LanguageParser.ExpressionParenthesizedContext):
        pass

    # Exit a parse tree produced by LanguageParser#expressionParenthesized.
    def exitExpressionParenthesized(self, ctx:LanguageParser.ExpressionParenthesizedContext):
        pass


    # Enter a parse tree produced by LanguageParser#expressionFunction.
    def enterExpressionFunction(self, ctx:LanguageParser.ExpressionFunctionContext):
        pass

    # Exit a parse tree produced by LanguageParser#expressionFunction.
    def exitExpressionFunction(self, ctx:LanguageParser.ExpressionFunctionContext):
        pass


    # Enter a parse tree produced by LanguageParser#functionArguments.
    def enterFunctionArguments(self, ctx:LanguageParser.FunctionArgumentsContext):
        pass

    # Exit a parse tree produced by LanguageParser#functionArguments.
    def exitFunctionArguments(self, ctx:LanguageParser.FunctionArgumentsContext):
        pass


    # Enter a parse tree produced by LanguageParser#expressionVariable.
    def enterExpressionVariable(self, ctx:LanguageParser.ExpressionVariableContext):
        pass

    # Exit a parse tree produced by LanguageParser#expressionVariable.
    def exitExpressionVariable(self, ctx:LanguageParser.ExpressionVariableContext):
        pass


    # Enter a parse tree produced by LanguageParser#expressionLiteral.
    def enterExpressionLiteral(self, ctx:LanguageParser.ExpressionLiteralContext):
        pass

    # Exit a parse tree produced by LanguageParser#expressionLiteral.
    def exitExpressionLiteral(self, ctx:LanguageParser.ExpressionLiteralContext):
        pass


