grammar Calculator;

program
    :   (statement NL)+
        EOF
    ;

statement
    :   command
    |   functionDeclaration
    |   variableDeclaration
    |   constantDeclaration
    |   expression
    ;

command
    :   '!' IDENTIFIER functionArguments?
    ;


functionDeclaration
    :   DEF signature ASSIGN_OP expression
    ;


signature
    :   IDENTIFIER functionParameters?
    ;

functionParameters
    :   PAREN_OPEN
        (IDENTIFIER (COMMA IDENTIFIER)*)?
        PAREN_CLOSE
    ;


variableDeclaration
    :   IDENTIFIER ASSIGN_OP expression
    ;

constantDeclaration
    :   CONST IDENTIFIER ASSIGN_OP expression
    ;

expression
    :   multiplicativeExpression
    ;

multiplicativeExpression
    :   additiveExpression
    |   multiplicativeExpression multiplicativeOperator additiveExpression
    ;

multiplicativeOperator
    :   MUL_OP
    |   DIV_OP
    ;

additiveExpression
    :   primaryExpression
    |   additiveExpression additiveOperator primaryExpression
    ;

additiveOperator
    :   ADD_OP
    |   SUB_OP
    ;

primaryExpression
    :   parenthesizedExpression
    |   functionExpression
    |   variableExpression
    |   literalExpression
    ;

parenthesizedExpression
    :   PAREN_OPEN multiplicativeExpression PAREN_CLOSE
    ;

functionExpression
    :   IDENTIFIER functionArguments
    ;

functionArguments
    :   PAREN_OPEN
        (expression (COMMA expression)*)?
        PAREN_CLOSE
    ;

variableExpression
    :   IDENTIFIER
    ;

literalExpression
    :   NUMBER
    ;


NUMBER: [0-9]+ ('.' [0-9]+)?;

ASSIGN_OP : '=';
COMMA : ',';

ADD_OP   : '+';
SUB_OP   : '-';
MUL_OP   : '*';
DIV_OP   : '/';

CONST : 'const';
DEF : 'def';

PAREN_OPEN : '(';
PAREN_CLOSE : ')';


ECHO : 'echo';

NL
    :   '\n'
    ;

IDENTIFIER
    :   [a-zA-Z_]+
    ;

WHITESPACE
    :   [ \t\r\n]+ -> skip
    ;

COMMENT    : ('#' [.]* '\n') -> skip;