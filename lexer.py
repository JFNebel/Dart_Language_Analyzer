# Grupo Dart 2 
import ply.lex as lex

reservadas = {
    'for'    : 'FOR',
    'var'    : 'VAR',
    'int'    : 'INT',
    'double' : 'DOUBLE'
}

tokens = (
    'NUMBER',
    'ID',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'MAYORQUE',
    'MENORQUE',
    'EQUALS',
    'PUNTCOM',
    'RCURLYB',
    'LCURLYB'
) + tuple(reservadas.values())

#Expresiones regulares:
t_VAR = r'^var$'
t_ignore = '^ \t$'
t_NUMBER = r'^\d+$'
t_PLUS = r'^\+$'
t_MINUS = r'^-$'
t_TIMES = r'^\*$'
t_DIVIDE = r'^\/$' 
t_LPAREN = r'^\($'
t_RPAREN = r'^\)$'
t_MAYORQUE = r'^>$'
t_MENORQUE = r'^<$'
t_ID = r'^\w+$'
t_EQUALS = r'^\=$'
t_PUNTCOM = r'^\;$'
t_FOR = r'^for$'
t_INT = r'^int$'
t_DOUBLE = r'^double$'

# Error handling rule
def t_error(t):
    print("No es reconocido '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# Test it out
data = '''var variable;'''

# Give the lexer some input
lexer.input(data)
# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)
