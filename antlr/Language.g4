grammar Language;

program
    :   (declaration)*
        (statement)*
        EOF
    ;

declaration
    :   declarationFunction
    |   declarationConstant
    ;

declarationConstant
    :   CONST IDENTIFIER ASSIGN_OP expressionLiteral SEMI
    ;

declarationFunction
    :   FUNC functionSignature codeBlock
    ;

functionSignature
    :   IDENTIFIER functionParameters?
    ;

functionParameters
    :   PAREN_OPEN
        (IDENTIFIER (COMMA IDENTIFIER)*)?
        PAREN_CLOSE
    ;

statement
    :   statementVariableDeclaration
    |   statementAssignment
    |   statementReturn
    |   statementIf
    |   statementFor
    |   statementWhile
    |   statementExpression
    ;

statementVariableDeclaration
    :   VAR IDENTIFIER ASSIGN_OP expression SEMI
    ;

statementAssignment
    :   IDENTIFIER ASSIGN_OP expression SEMI
    ;

statementReturn
    :   RETURN expression SEMI
    ;

statementIf
    :   IF PAREN_OPEN expression PAREN_CLOSE codeBlock
        statementElse?
    ;

statementElse
    :   ELSE codeBlock
    ;

statementFor
    :   FOR PAREN_OPEN
            statementVariableDeclaration
            statementExpression
            expression
            PAREN_CLOSE
            codeBlock
    ;

statementWhile
    :   WHILE PAREN_OPEN expression PAREN_CLOSE codeBlock
    ;

codeBlock
    :   (CURLY_OPEN statement* CURLY_CLOSE) | statement
    ;

statementExpression
    :   expression SEMI
    ;

expression
    :   expressionOr
    ;

expressionOr
    :   expressionAnd
    |   expressionOr OR_OP expressionAnd
    ;

expressionAnd
    :   expressionEquality
    |   expressionAnd AND_OP expressionEquality
    ;

expressionEquality
    :   expressionRelational
    |   expressionEquality EQ_OP expressionRelational
    |   expressionEquality NEQ_OP expressionRelational
    ;

expressionRelational
    :   expressionAdditive
    |   expressionRelational LT_OP expressionAdditive
    |   expressionRelational LTOE_OP expressionAdditive
    |   expressionRelational GT_OP expressionAdditive
    |   expressionRelational GTOE_OP expressionAdditive
    ;


expressionAdditive
    :   expressionMultiplicative
    |   expressionAdditive ADD_OP expressionMultiplicative
    |   expressionAdditive SUB_OP expressionMultiplicative
    ;

expressionMultiplicative
    :   expressionUnary
    |   expressionMultiplicative MUL_OP expressionUnary
    |   expressionMultiplicative DIV_OP expressionUnary
    |   expressionMultiplicative MOD_OP expressionUnary
    |   expressionMultiplicative EXP_OP expressionUnary
    ;

expressionUnary
    :   expressionPrimary
    |   NOT_OP expressionPrimary
    |   TYPE expressionPrimary
    |   DEC_OP expressionPrimary
    |   INC_OP expressionPrimary
    |   expressionPrimary DEC_OP
    |   expressionPrimary INC_OP
    ;

expressionPrimary
    :   expressionParenthesized
    |   expressionFunction
    |   expressionVariable
    |   expressionList
    |   expressionMap
    |   expressionLiteral
    |   expressionPrimary expressionDotAccess
    |   expressionPrimary expressionArrayAccess
    ;

expressionDotAccess
    :   DOT IDENTIFIER
    ;

expressionArrayAccess
    :   BRACK_OPEN expression BRACK_CLOSE
    ;

expressionList
    :   BRACK_OPEN
        (expression (COMMA expression)* COMMA?)?
        BRACK_CLOSE
    ;

expressionMap
    :   CURLY_OPEN
        (expressionMapEntry (COMMA expressionMapEntry)* COMMA?)?
        CURLY_CLOSE
    ;

expressionMapEntry
    :   IDENTIFIER COLON expression
    ;

expressionParenthesized
    :   PAREN_OPEN expression PAREN_CLOSE
    ;

expressionFunction
    :   IDENTIFIER functionArguments
    ;

functionArguments
    :   PAREN_OPEN
        (expression (COMMA expression)*)?
        PAREN_CLOSE
    ;

expressionVariable
    :   IDENTIFIER
    ;

expressionLiteral
    :   NUMBER_VAL
    |   STRING_VAL
    |   BOOL_VAL
    |   NULL
    ;

NUMBER_VAL   : [0-9]+ ('.' [0-9]+)?;
STRING_VAL   : QUOTE (ESCAPED_CHAR | ~['])* QUOTE;
ESCAPED_CHAR :   '\\' .;
BOOL_VAL     : TRUE | FALSE;

ASSIGN_OP : '=';
COMMA     : ',';
ADD_OP    : '+';
SUB_OP    : '-';
MUL_OP    : '*';
DIV_OP    : '/';
MOD_OP    : '%';
EXP_OP    : '^';
AND_OP    : '&&';
OR_OP     : '||';
LT_OP     : '<';
GT_OP     : '>';
LTOE_OP   : '<=';
GTOE_OP   : '>=';
EQ_OP     : '==';
NEQ_OP    : '!=';
NOT_OP    : '!';
DEC_OP    : '--';
INC_OP    : '++';

TYPE   : 'type';
VAR    : 'var';
CONST  : 'const';
FUNC   : 'func';
WHILE  : 'while';
FOR    : 'for';
RETURN : 'return';
IF     : 'if';
ELSE   : 'else';
TRUE   : 'true';
FALSE  : 'false';
NULL   : 'null';

PAREN_OPEN  : '(';
PAREN_CLOSE : ')';
CURLY_OPEN  : '{';
CURLY_CLOSE : '}';
BRACK_OPEN  : '[';
BRACK_CLOSE : ']';
QUOTE       : '\'';
SEMI        : ';';
COLON       : ':';
DOT         : '.';

IDENTIFIER : [a-zA-Z_][a-zA-Z0-9_]*;
WHITESPACE : [ \t\r\n]+ -> skip;
COMMENT    : ('#' [.]* '\n') -> skip;