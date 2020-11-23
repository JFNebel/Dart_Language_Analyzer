import ply.yacc as yacc
from lexer import tokens

#Allison Brito
def p_expresion(p):
    '''expresion : expresionA
    | lista
    | expresionBool
    | mapa
    | icadena
    | concatenacion
    | incremento
    | decremento
    '''

def p_expresionA(p):
    'expresionA : valor operadorA valor'
   # p[0] = p[1] + p[3]


def p_expresionBool(p):
    'expresionBool : VARBOOL ID EQUALS booleano pto_coma' 

def p_booleano(p):
    '''booleano : TRUE
    | FALSE'''

#Regla de expresion de lista
def p_lista(p):
    '''lista : expLista
    | add_lista
    '''
#Inicializacion de una lista
def p_expLista(p):
    '''expLista : VAR ID EQUALS NEW LISTA LPAREN NUMBER RPAREN pto_coma
        | VAR ID EQUALS NEW LISTA LPAREN RPAREN pto_coma
        | VAR ID EQUALS LCORCHETE elementosLista RCORCHETE pto_coma
        '''

#Agregar elementos a una lista
def p_add_lista(p):
    '''add_lista : ID LCORCHETE NUMBER RCORCHETE EQUALS NUMBER pto_coma
    |   ID PTO ADD LPAREN NUMBER RPAREN pto_coma
    | ID PTO ADD LPAREN ID RPAREN pto_coma
    '''
#Recursividad al agregar elementos de una lista ID debe cambiarse por CADENA
def p_elementosLista(p):
    '''elementosLista : COMILLAS ID COMILLAS
        | COMILLAS ID COMILLAS COMA elementosLista
        | COMILLAS NUMBER COMILLAS
        | COMILLAS NUMBER COMILLAS COMA elementosLista
        | 
    '''
#Operaciones en un mapa: inicializar y agregar elemento
def p_mapa(p):
    '''mapa : expMapa
    | add_mapa
    '''
#Inicializacion de un mapa
def p_expMapa(p):
    '''expMapa : VAR ID EQUALS NEW MAPA LPAREN RPAREN pto_coma
    | MAPA ID EQUALS LCURLYB elementosMapa RCURLYB pto_coma
    '''

#Recursividad al agregar elementos de un mapa valor debe cambiarse POR CADENA, valor llama a ID y NUMBER solo necesitamos a number
def p_elementosMapa(p):
    '''elementosMapa : COMILLAS valor COMILLAS DOSPTO COMILLAS valor COMILLAS
    | COMILLAS valor COMILLAS DOSPTO COMILLAS valor COMILLAS COMA elementosMapa
    | COMILLAS valor COMILLAS DOSPTO NUMBER
    | COMILLAS valor COMILLAS DOSPTO NUMBER COMA elementosMapa
    | NUMBER DOSPTO COMILLAS valor COMILLAS 
    | NUMBER DOSPTO COMILLAS valor COMILLAS COMA elementosMapa
    | NUMBER DOSPTO NUMBER
    | NUMBER DOSPTO NUMBER COMA elementosMapa
    '''

#Agrega a la ED mapa ID DEBE CAMBIARSE POR CADENA, DEBE DEINIRISE LA REGLA EN EL LEXER
def p_add_mapa(p):
    '''add_mapa : ID LCORCHETE COMILLAS ID COMILLAS RCORCHETE EQUALS COMILLAS ID COMILLAS pto_coma
    '''

def p_operadorA(p):
    '''operadorA : PLUS
    | MINUS
    | TIMES
    | DIVIDE
    | DIVIDE_E
    '''

def p_incremento(p):
    'incremento : ID INCREMENTO pto_coma'

def p_decremento(p):
    'decremento : ID DECREMENTO pto_coma'

#Cadenas con comilla simple, doble y triple ID debe cambiarse por CADENA
def p_i_cadena(p):
    '''icadena : VAR ID EQUALS cadenas pto_coma
    '''

def p_valor(p):
    '''valor : ID 
    | NUMBER
    '''
#Metodo substing de un string
def p_concatenacion(p):
    '''concatenacion : VAR ID EQUALS ID PTO SUBSTRING LPAREN NUMBER COMA NUMBER RPAREN pto_coma
    '''

def p_cadenas(p):
    '''cadenas : COMILLAS ID COMILLAS
    | COMILLAD ID COMILLAD
    | COMIILLATS ID COMIILLATS
    | COMILLATD ID COMILLATD
    '''
#regla de punto y coma
def p_pto_coma(p):
    'pto_coma : PUNTCOM'
   
def p_error(p):
    print(p)
 # Build the parser
parser = yacc.yacc()
 
while True:
    try:
        s = input('Ingrese el codigo > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)