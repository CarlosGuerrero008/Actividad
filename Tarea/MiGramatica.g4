grammar MiGramatica;

programa: (sentencia ';'?)+ EOF ;

sentencia
    : ifElseStmt  
    | asignacion
    | forStmt
    | bloque
    ;

forStmt
    : 'for' '(' 
      (asignacion | declaracion)? ';' 
      condicion? ';' 
      expresionIncremento? 
      ')' cuerpo=sentencia # ForLoopRule
    ;

declaracion
    : tipo ID '=' expr # DeclaracionRule
    ;

tipo
    : 'int' | 'float' | 'var' # TipoRule
    ;

bloque: '{' (sentencia ';'?)* '}' ;

ifElseStmt
    : 'if' '(' condicion ')' thenPart=sentencia ('else' elsePart=sentencia)? # IfElseRule
    ;

condicion
    : expr op=('>' | '<' | '==' | '!=' | '>=' | '<=') expr # CondicionRule
    | expr # SoloExpresion
    ;

asignacion
    : ID '=' expr ';'? # AssignRule
    ;

expresionIncremento
    : ID '++' # IncrementoRule
    | ID '--' # DecrementoRule
    | ID '=' expr # AsignacionIncrRule
    ;

expr
    : expr op=('*'|'/') expr     # MulDivRule
    | expr op=('+'|'-') expr     # AddSubRule
    | INT                        # IntRule
    | ID                         # VariableRule
    | '(' expr ')'               # ParensRule
    ;

ID  : [a-zA-Z_][a-zA-Z_0-9]* ;
INT : [0-9]+ ;
WS  : [ \t\r\n]+ -> skip ;