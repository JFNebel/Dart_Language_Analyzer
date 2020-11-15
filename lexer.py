'''
Grupo Dart 2
Integrantes: Allison Brito y Juan Fco. Nebel

TODO: 
1) Crear sección de leído del archivo de ejemplos (ver linea 71)
2) Agregar y validar 1 estructura de datos

'''

import ply.lex as lex

# Diccionario de palabras reservadas
reservadas = {
    'for'    : 'FOR',
    'var'    : 'VAR',
    'int'    : 'INT',
    'double' : 'DOUBLE'
}

# Lista de tokens
tokens = [
    'NUMBER',
    'INCREMENTO',
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
] + list(reservadas.values())
    
#Expresiones regulares:
t_ignore     = r' |    '  # ignore espacio o tab, usar caracteres \t saca un warning
t_VAR        = r'\bvar\b'
t_FOR        = r'\bfor\b'
t_INT        = r'\bint\b'
t_DOUBLE     = r'\bdouble\b'
t_NUMBER     = r'\b\d+\b'
t_ID         = r'\b\w+\b'
t_PLUS       = r'\+'
t_INCREMENTO = r'\+\+'
t_RCURLYB    = r'\}'
t_LCURLYB    = r'\{'
t_MINUS      = r'-'
t_TIMES      = r'\*'
t_DIVIDE     = r'\/' 
t_LPAREN     = r'\('
t_RPAREN     = r'\)'
t_MAYORQUE   = r'>'
t_MENORQUE   = r'<'
t_EQUALS     = r'\='
t_PUNTCOM    = r'\;'

# Manejo de errores
def t_error(t):
    print("No es reconocido '%s'" % t.value[0])
    t.lexer.skip(1)

# Construyendo al lexer
lexer = lex.lex()

# Data a analizar
#TODO: Crear sección de lectura del archivo código.txt
data =  'for(int i = 0; i < 10; i++){}'
 
# Darle el input al lexer
lexer.input(data)

# Iteración de tokens
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)
