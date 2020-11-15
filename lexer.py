'''
Grupo Dart 2
Integrantes: Allison Brito y Juan Fco. Nebel

TODO: 
1) Aun no reconoce le + solo, chequear ejemplo de suma
    a) Esto solo ocurre cuando el + está entre espacios
    b) Crear sección de leído del archivo de ejemplos 
    c) Agregar y validar 1 estructura de control

'''
import os
import ply.lex as lex

# Diccionario de palabras reservadas
reservadas = {
    'for'          : 'FOR',
    'var'          : 'VAR',
    'int'          : 'INT',
    'double'       : 'VARDOUBLE',
    'bool'         : 'VARBOOL',
    'while'        : 'WHILE',
    'new'          : 'NEW',
    'List'         : 'LISTA',
    'Map'          : 'MAPA',
    'putIfAbsent'  : 'PUT',
    'update'       : 'UPDATE',
    'print'        : 'PRINT',
}

# Lista de tokens
tokens = [
    'NUMBER',
    'INCREMENTO',
    'DECREMENTO',
    'BOOLEANO',
    'DOUBLE',
    'ID',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'DIVIDE_E',
    'LPAREN',
    'RPAREN',
    'LCORCHETE',
    'RCORCHETE',
    'MAYORQUE',
    'MENORQUE',
    'EQUALS',
    'PUNTCOM',
    'RCURLYB',
    'LCURLYB',
    'COMILLAD',
    'COMILLAS',
    'COMA',
    'AND',
    'OR',
    'NOT'
] + list(reservadas.values())
    
#Expresiones regulares:
t_VAR        = r'\bvar\b'
t_FOR        = r'\bfor\b'
t_INT        = r'\bint\b'
t_WHILE      = r'\bwhile\b'
t_VARDOUBLE  = r'\bdouble\b'
t_VARBOOL    = r'\bbool\b'
t_BOOLEANO   = r'\b(true|false)\b'
t_LISTA      = r'\bList\b'
t_MAPA       = r'\bMap\b'
t_INCREMENTO = r"\+\+"
t_DECREMENTO = r'\-\-'
t_PLUS       = r'\+'
t_RCURLYB    = r'\}'
t_LCURLYB    = r'\{'
t_MINUS      = r'-'
t_TIMES      = r'\*'
t_DIVIDE     = r'\/'
t_DIVIDE_E   = r'\~\/'
t_LPAREN     = r'\('
t_RPAREN     = r'\)'
t_LCORCHETE  = r'\['
t_COMILLAD   = r'\"'
t_COMILLAS   = r'\''
t_COMA       = r'\,'
t_RCORCHETE  = r'\]'
t_MAYORQUE   = r'>'
t_MENORQUE   = r'<'
t_EQUALS     = r'\='
t_PUNTCOM    = r'\;'
t_AND        = r'\&\&'
t_OR         = r'\|\|'
t_NOT   = r'\!'
t_PUT        = r'\b\.putIfAbsent\b'
t_UPDATE     = r'\b\.update\b'
t_PRINT      = r'\bprint\b'

t_ignore     = r'     '  # ignore espacio o tab, usar caracteres \t saca un warning

#Numeros decimales
def t_DOUBLE(t):
    r'[0-9]+\.[0-9]+'
    t.type = reservadas.get(t.value, 'DOUBLE')
    return t

#Numeros enteros
def t_NUMBER(t):
    r'[\d]+'
    t.type = reservadas.get(t.value, 'NUMBER')
    return t


#Id(variables)
def t_ID(t):
    r'\$?[\w]+'
    t.type = reservadas.get(t.value,'ID')    # Check for reserved words
    return t

# Manejo de errores
def t_error(t):
    print("No es reconocido '%s'" % t.value[0])
    t.lexer.skip(1)

# Construyendo al lexer
lexer = lex.lex()
lista_archivos=["test_Allison_Brito.txt","test_Juan_Nebel.txt"]
for archivo in lista_archivos:
    fichero= open(os.getcwd()+str('\\') +archivo,'r+',encoding="utf8")
    for data in fichero.readlines():
        # Darle el input al lexer
        if len(data)==0:
            break
        else:
            lexer.input(data)
            # Iteración de tokens
            while True:
                tok = lexer.token()
                if not tok:
                    break  # No more input
                print(tok)
