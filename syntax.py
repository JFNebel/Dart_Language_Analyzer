import ply.yacc as yacc
from lexer import tokens,erroresL
import os

'''
    REVISAR:
    SE DEFINIRÁ INICIALIZACION DE ENTEROS? int x; e int x=0;
    SE DEFINIRÁ INICIALIZACION DE BOOLEANOS? bool x=true; y bool x=false;
'''



erroresS=[]

# *********************** Expresión global (Allison Brito y Juan Nebel) *****************************

def p_expresion(p):
    '''expresion : lista
    | mapa
    | variable
    | expresionFor
    | expresionWhile
    | expresionIf
    | f_subtring
    | accPosString
    | incremento
    | decremento
    | print
    | funcion
    | concatenar
    | expresion expresion
    '''

# *********************** DECLARACIÓN DE VARIABLE (Juan Nebel) *****************************

def p_variable(p):
    '''variable : VAR ID EQUALS expresionVar PUNTCOM
                | VAR ID PUNTCOM
                | VAR ID EQUALS expresionBool PUNTCOM'''

def p_valorVar(p):
    '''valorVar : NUMBER
                | DOUBLE
                | CADENA'''


def p_expresionVar(p):
    '''expresionVar : valorVar
                    | ID 
                    | expresionVar operadorA expresionVar'''

# *********************** ESTRUCTURA FOR (Juan Nebel) *****************************

def p_expresionFor(p):
    'expresionFor : FOR LPAREN forParameters RPAREN LCURLYB expresion RCURLYB'   

def p_forParameters(p):
    'forParameters : forIterator PUNTCOM forCondition PUNTCOM forAction'

def p_forIterator(p):
    '''forIterator : INT ID EQUALS NUMBER
                   | ID EQUALS NUMBER'''

def p_forCondition(p):
    '''forCondition : ID MAYORQUE NUMBER 
                    | ID MENORQUE NUMBER '''

def p_forAction(p):
    '''forAction : ID INCREMENTO  
                 | ID DECREMENTO
                 | INCREMENTO ID
                 | DECREMENTO ID'''

# *********************** ESTRUCTURA WHILE (Juan Nebel) *****************************

def p_expresionWhile(p):
    'expresionWhile : WHILE LPAREN expresionBool RPAREN LCURLYB expresion RCURLYB'

# *********************** ESTRUCTURA IF (Juan Nebel) *****************************

def p_expresionIf(p):
    'expresionIf : IF LPAREN expresionBool RPAREN LCURLYB expresion RCURLYB'

# *********************** REGLAS BOOL (Allison Brito y Juan Nebel) *****************************

def p_expresionBool(p):
    '''expresionBool : booleano
                     | ID comparador ID
                     | ID comparador NUMBER
                     | NUMBER comparador ID
                     | NUMBER comparador NUMBER
                     | NOT ID
                     | expresionBool comparador expresionBool
                     | expresionBool EQUIVAL expresionBool''' #No estoy seguro porque no puedo concatenar

def p_booleano(p):
    '''booleano : TRUE
                | FALSE'''

def p_comparador(p):
    '''comparador : MAYORQUE 
                  | MENORQUE
                  | EQUIVAL
                  | MINEQ
                  | MAYEQ
                  | NOEQUIVAL
                  | AND
                  | OR'''



# *********************** ED LISTA (Allison Brito) *****************************
#Regla de expresion de lista
def p_lista(p):
    '''lista : expLista
             | add_lista
             | replace
    '''
#Inicializacion de una lista
def p_expLista(p):
    '''expLista : VAR ID EQUALS NEW LISTA LPAREN inicializaLista RPAREN PUNTCOM
                | VAR ID EQUALS LCORCHETE elementosLista RCORCHETE PUNTCOM
    '''
#Valor que se le asigna al momento de declarar el # de elementos de un mapa
def p_inicializaLista(p):
    '''inicializaLista  : NUMBER
                        | 
    '''

#Agregar elementos a una lista
def p_add_lista(p):
    '''add_lista : ID LCORCHETE NUMBER RCORCHETE EQUALS num_cadena PUNTCOM
                 | ID PTO ADD LPAREN elementoAddLista RPAREN PUNTCOM
    '''
def p_elementoAddLista(p):
    '''elementoAddLista : num_cadena
                        | booleano
    '''
#Toma el valor de un numero o de un string con comillas incluido
def p_num_cadena(p):
    '''num_cadena : NUMBER
                | CADENA'''

#Recursividad al agregar elementos de una lista
def p_elementosLista(p):
    '''elementosLista : CADENA
                      | NUMBER
                      | CADENA COMA elementosLista
                      | NUMBER COMA elementosLista
                      | 
    '''

#Reemplazar elementos de una lista
def p_replace(p):
    '''replace : ID PTO REPLACE LPAREN NUMBER COMA NUMBER COMA LCORCHETE NUMBER RCORCHETE RPAREN PUNTCOM
    '''

# *********************** ED MAPA (Allison Brito) *****************************
#Operaciones en un mapa: inicializar y agregar elemento
def p_mapa(p):
    '''mapa : expMapa
            | add_mapa
            | update_mapa
            | add_mapa_putIfAbsent
    '''
#Inicializacion de un mapa
def p_expMapa(p):
    '''expMapa : VAR ID EQUALS NEW MAPA LPAREN RPAREN PUNTCOM
               | MAPA ID EQUALS LCURLYB elementosMapa RCURLYB PUNTCOM
    '''

#Recursividad al agregar elementos de un mapa
def p_elementosMapa(p):
    '''elementosMapa : num_cadena DOSPTO num_cadena
                     | num_cadena DOSPTO num_cadena COMA elementosMapa
    '''

#Agrega a la ED mapa
def p_add_mapa(p):
    '''add_mapa : ID LCORCHETE num_cadena RCORCHETE EQUALS num_cadena PUNTCOM
    '''

def p_add_mapa_putIfAbsent(p):
    '''add_mapa_putIfAbsent : ID PTO PUT LPAREN num_cadena COMA LPAREN RPAREN EQUALS MAYORQUE num_cadena RPAREN PUNTCOM
    '''
#Actualizar valor del mapa
def p_update_mapa(p):
    '''update_mapa : ID PTO UPDATE LPAREN CADENA COMA LPAREN VAR ID RPAREN EQUALS MAYORQUE CADENA COMA IFABSENT DOSPTO LPAREN RPAREN EQUALS MAYORQUE CADENA RPAREN PUNTCOM
    '''
# *********************** OPERADORES ARITMETICOS (Allison Brito) *****************************
def p_operadorA(p):
    '''operadorA : PLUS
                 | MINUS
                 | TIMES
                 | DIVIDE
                 | DIVIDE_E
    '''
# *********************** OPERADORES INCREMENTO Y DECREMENTO (Allison Brito) *****************************
def p_incremento(p):
    'incremento : ID INCREMENTO PUNTCOM'

def p_decremento(p):
    'decremento : ID DECREMENTO PUNTCOM'

# *********************** OBTENER SUBSTRING DE STRING (Allison Brito) *****************************
#Metodo substing de un string
def p_f_subtring(p):
    '''f_subtring : VAR ID EQUALS ID PTO SUBSTRING LPAREN NUMBER COMA NUMBER RPAREN PUNTCOM
    '''
def p_accPosString(p):
    '''accPosString : VAR ID EQUALS ID LCORCHETE NUMBER RCORCHETE PUNTCOM
    '''
# *********************** IMPRIMIR VARIABLES/DATO (Allison Brito) *****************************
#Imprimir datos
def p_print(p):
    '''print : PRINT LPAREN printVal RPAREN PUNTCOM
    '''
#Datos que puede tomar al imprimir
def p_printVal(p):
    '''printVal : ID
                | valorVar
                | expresionBool
    '''

# *********************** FUNCION (Allison Brito) *****************************
#Construir una funcion
def p_funcion(p):
    '''funcion : VOID ID LPAREN parametroFuncion RPAREN final_key
    '''

def p_parametroFuncion(p):
    '''parametroFuncion : VAR ID
                        | 
    '''

def p_final_key(p):
    '''final_key : LCURLYB expresion RCURLYB
    '''

def p_concatenar(p):
    '''concatenar : VAR ID EQUALS concatenarRecursivo PUNTCOM
    '''

def p_concatenarRecursivo(p):
    '''concatenarRecursivo : CADENA PLUS CADENA
                           | PLUS CADENA
                           | CADENA PLUS concatenarRecursivo
    '''

def p_error(p):

    erroresS.append("Error sintactico al definir: " + str(p)+"\n")
    



parser = yacc.yacc()

# data = '''
# for(int i=0; i<10;i++){
#  var 3!;
# var 4!;
# }
# for(int i = 0; i < 10; i++){
#      var x = 20;
#      var y = 30;
#      if(x>y){
#          var z = x + y;
#      }
# '''

data=  '''
double salaraio =10.425*horas;
int x;
int x=0;
bool resig=true;
void reg(var r){
 if(!r){
 var r=true;
}
}
var s1='g';
var $e="f";
void main(){
 var l= new List();
l.add(33);
var mapa = new Map();
det['g']='g';
}
var p='Concateno1' + 'conca1';
var s=string[3];
var string ="Hola mundo!";
var newString = string.substring(0,3);
if(2==2){
    var string ="Hola mundo!";
}
if(2!=2){
    var string ="Hola mundo!";
}
if(2>3){
    var string ="Hola mundo!";
}
if(2<3){
var string ="Hola mundo!";
}
if(2>=3){
var string ="Hola mundo!";
}
if(2<=4){
var string ="Hola mundo!";
}
if(!h){
var string ="Hola mundo!";
}
if(d&&g){
var string ="Hola mundo!";
}
if(!e || !q){
var string ="Hola mundo!";
}
print("1");
for(int i =0;i<10;i++){
    var string ="Hola mundo!";
}
var num=0;
while(num<10){
print(num);
num++;
}
while(num<10 || n==0 && p!=2){
print(num);
num++;
}
var lista=["h"];
list.add('Mundo!');
var lista = [2,3,4];
lista.replaceRange(1,3,[99]);
Map mapa = {1:"Hola", "2":3};
mapa.putIfAbsent(3,() =>'! ');
m.update("1j", (var val) => "Jim", ifAbsent: () => "Jane");
var l=[];
    '''
#result = parser.parse(data)
#print("*************************************************************")
#print("La frase a analizar es: ", data)
#print(erroresS)
#print("Todavia hay "+str(len(erroresS)) + " errores en el sintactico")



# archivo = 'codigoAlg.txt'
# fichero= open(os.getcwd()+str('//') +archivo,'r+',encoding="utf8")
# for data in fichero.readlines():
#     if(data[0]!='#'):
#         print("\n") #Deja un espacio entre frases
#         print("*************************************************************")
#         print("La frase a analizar es: ", data)
        
#         # Darle el input al parser
#         if len(data)==0:
#             break
#         else:
#             result = parser.parse(data)
#             print(result)
