'''
Grupo Dart 2
Integrantes: Allison Brito y Juan Fco. Nebel
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
    'true'         : 'TRUE',
    'false'        : 'FALSE',
    'while'        : 'WHILE',
    'new'          : 'NEW',
    'List'         : 'LISTA',
    'add'          : 'ADD',
    'if'           : 'IF',
    'Map'          : 'MAPA',
    'putIfAbsent'  : 'PUT',
    'update'       : 'UPDATE',
    'print'        : 'PRINT',
    'substring'    : 'SUBSTRING',
    'void'         : 'VOID'
}

# Lista de tokens
tokens = [
    'NUMBER',
    'INCREMENTO',
    'DECREMENTO',
    'EQUIVAL',
    'MAYEQ',
    'MINEQ',
    'DOUBLE',
    'ID',
    'PLUS',
    'PTO',
    'MINUS',
    'CADENA',
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
    'DOSPTO',
    'RCURLYB',
    'LCURLYB',
    # 'COMILLAD',
    # 'COMILLAS',
#   'COMILLATD',
#   'COMIILLATS',
    'COMA',
    'AND',
    'OR',
    'NOT'
] + list(reservadas.values())
    
#Expresiones regulares:
t_VAR        = r'\bvar\b'
t_IF         = r'\bif\b'
t_FOR        = r'\bfor\b'
t_INT        = r'\bint\b'
t_WHILE      = r'\bwhile\b'
t_TRUE       = r'\btrue\b'
t_FALSE      = r'\bfalse\b'
t_VARDOUBLE  = r'\bdouble\b'
t_VARBOOL    = r'\bbool\b'
t_LISTA      = r'\bList\b'
t_MAPA       = r'\bMap\b'
t_SUBSTRING  = r'\bsubstring\b'
t_ADD        = r'\badd\b'
t_VOID       = r'\bvoid\b'
t_INCREMENTO = r"\+\+"
t_DECREMENTO = r'\-\-'
t_EQUIVAL    = r'=='
t_MAYEQ      = r'>='
t_MINEQ      = r'<='
t_PLUS       = r'\+'
t_RCURLYB    = r'\}'
t_LCURLYB    = r'\{'
t_MINUS      = r'\-'
t_TIMES      = r'\*'
t_DIVIDE     = r'\/'
t_DIVIDE_E   = r'\~\/'
t_LPAREN     = r'\('
t_RPAREN     = r'\)'
t_LCORCHETE  = r'\['
# t_COMILLAD   = r'\"'
# t_COMILLAS   = r'\''
t_COMA       = r'\,'
t_RCORCHETE  = r'\]'
t_MAYORQUE   = r'>'
t_MENORQUE   = r'<'
t_EQUALS     = r'='
t_PUNTCOM    = r'\;'
t_DOSPTO     = r':'
t_AND        = r'\&\&'
t_OR         = r'\|\|'
t_NOT        = r'\!'
#t_COMIILLATS = r'\'\'\''
#t_COMILLATD  = r'\"\"\"'
t_PUT        = r'\bputIfAbsent\b'
t_UPDATE     = r'\bupdate\b'
t_PTO        = r'\.'
t_PRINT      = r'\bprint\b'
t_CADENA     = r'(\'|\")[\w\s\?#$%&()=|°¬!]*(\'|\")'

t_ignore     = r'     '  # ignore espacio o tab, usar caracteres \t saca un warning

#Numeros decimales
def t_DOUBLE(t):
    r'[0-9]+\.[0-9]+'
    t.type = reservadas.get(t.value, 'DOUBLE')
    return t

#Numeros enteros
def t_NUMBER(t):
    r'\d+'
    t.type = reservadas.get(int(t.value), 'NUMBER')
    return t

#Salto de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#Id(variables)
def t_ID(t):
    r'\$?[\w]+'
    t.type = reservadas.get(str(t.value),'ID')    # Check for reserved words
    return t


# Manejo de errores
def t_error(t):
    print("No es reconocido '%s'" % t.value[0])
    t.lexer.skip(1)

# Construyendo al lexer
lexer = lex.lex()



archivo = 'codigoAlg.txt'
fichero= open(os.getcwd()+str('//') +archivo,'r+',encoding="utf8")

for data in fichero.readlines():
    if(data[0]!='#'):
        print("\n") #Deja un espacio entre frases
        print("*************************************************************")
        print("La frase a analizar es: ", data)
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
