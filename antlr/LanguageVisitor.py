# Generated from Language.g4 by ANTLR 4.7.2
from antlr4 import *
from .LanguageParser import LanguageParser

# This class defines a complete generic visitor for a parse tree produced by LanguageParser.

class LanguageVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LanguageParser#program.
    def visitProgram(self, ctx:LanguageParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#declaration.
    def visitDeclaration(self, ctx:LanguageParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#declarationConstant.
    def visitDeclarationConstant(self, ctx:LanguageParser.DeclarationConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#declarationFunction.
    def visitDeclarationFunction(self, ctx:LanguageParser.DeclarationFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#functionSignature.
    def visitFunctionSignature(self, ctx:LanguageParser.FunctionSignatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#functionParameters.
    def visitFunctionParameters(self, ctx:LanguageParser.FunctionParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#statement.
    def visitStatement(self, ctx:LanguageParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#statementVariableDeclaration.
    def visitStatementVariableDeclaration(self, ctx:LanguageParser.StatementVariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#statementAssignment.
    def visitStatementAssignment(self, ctx:LanguageParser.StatementAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#statementReturn.
    def visitStatementReturn(self, ctx:LanguageParser.StatementReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#statementIf.
    def visitStatementIf(self, ctx:LanguageParser.StatementIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#statementElse.
    def visitStatementElse(self, ctx:LanguageParser.StatementElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#statementFor.
    def visitStatementFor(self, ctx:LanguageParser.StatementForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#statementWhile.
    def visitStatementWhile(self, ctx:LanguageParser.StatementWhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#codeBlock.
    def visitCodeBlock(self, ctx:LanguageParser.CodeBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#statementExpression.
    def visitStatementExpression(self, ctx:LanguageParser.StatementExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#expression.
    def visitExpression(self, ctx:LanguageParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#expressionOr.
    def visitExpressionOr(self, ctx:LanguageParser.ExpressionOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#expressionAnd.
    def visitExpressionAnd(self, ctx:LanguageParser.ExpressionAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#expressionEquality.
    def visitExpressionEquality(self, ctx:LanguageParser.ExpressionEqualityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#expressionRelational.
    def visitExpressionRelational(self, ctx:LanguageParser.ExpressionRelationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#expressionAdditive.
    def visitExpressionAdditive(self, ctx:LanguageParser.ExpressionAdditiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#expressionMultiplicative.
    def visitExpressionMultiplicative(self, ctx:LanguageParser.ExpressionMultiplicativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#expressionUnary.
    def visitExpressionUnary(self, ctx:LanguageParser.ExpressionUnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#expressionPrimary.
    def visitExpressionPrimary(self, ctx:LanguageParser.ExpressionPrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#expressionFieldAccess.
    def visitExpressionFieldAccess(self, ctx:LanguageParser.ExpressionFieldAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#expressionMethodAccess.
    def visitExpressionMethodAccess(self, ctx:LanguageParser.ExpressionMethodAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#expressionBracketAccess.
    def visitExpressionBracketAccess(self, ctx:LanguageParser.ExpressionBracketAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#expressionList.
    def visitExpressionList(self, ctx:LanguageParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#expressionMap.
    def visitExpressionMap(self, ctx:LanguageParser.ExpressionMapContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#expressionMapEntry.
    def visitExpressionMapEntry(self, ctx:LanguageParser.ExpressionMapEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#expressionParenthesized.
    def visitExpressionParenthesized(self, ctx:LanguageParser.ExpressionParenthesizedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#expressionFunction.
    def visitExpressionFunction(self, ctx:LanguageParser.ExpressionFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#arguments.
    def visitArguments(self, ctx:LanguageParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#expressionVariable.
    def visitExpressionVariable(self, ctx:LanguageParser.ExpressionVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#expressionLiteral.
    def visitExpressionLiteral(self, ctx:LanguageParser.ExpressionLiteralContext):
        return self.visitChildren(ctx)



del LanguageParser