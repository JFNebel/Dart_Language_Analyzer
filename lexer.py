'''
Grupo Dart 2
Integrantes: Allison Brito y Juan Fco. Nebel
'''
import os
import ply.lex as lex

# Lista de errores

erroresL = []


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
    'ifAbsent'     : 'IFABSENT',
    'update'       : 'UPDATE',
    'print'        : 'PRINT',
    'substring'    : 'SUBSTRING',
    'void'         : 'VOID',
    'replaceRange' : 'REPLACE',
}

# Lista de tokens
tokens = [
    'NUMBER',
    'INCREMENTO',
    'DECREMENTO',
    'EQUIVAL',
    'NOEQUIVAL',
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
t_NOEQUIVAL  = r'!='
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
t_IFABSENT   = r'\bifAbsent\b'
t_PUT        = r'\bputIfAbsent\b'
t_UPDATE     = r'\bupdate\b'
t_REPLACE    = r'\breplaceRage\b'
t_PTO        = r'\.'
t_PRINT      = r'\bprint\b'
t_CADENA     = r'(\'|\")[\w\s\?#$%&()=|°¬!]*(\'|\")'

t_ignore     = r' \t'  # ignore espacio o tab, usar caracteres \t saca un warning

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
    erroresL.append("No es reconocido '%s'" % t.value[0])
    t.lexer.skip(1)

# Construyendo al lexer
lexer = lex.lex()




#Lee un string en data

# data = '''for(int i = 0; i < 10; i++){
#     var x = 20;
#     var y = 30;
#     if(x>y){
#         var z = x + y;
#     }
# }'''
# data='''
# for(int i=0; i<10;i++){
#  var 3!;
# var 4!;
# }
# '''
data='''
int x=0;
int x;
double salaraio =10.425*horas;
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
string[3];
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
'''
lexer.input(data)
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)

print("Errores lexicos: " +str(erroresL))

#Leee desde un archivo

# archivo = 'codigoAlg.txt'
# fichero= open(os.getcwd()+str('//') +archivo,'r+',encoding="utf8")

# for data in fichero.readlines():
#     if(data[0]!='#'):
#         print("\n") #Deja un espacio entre frases
#         print("*************************************************************")
#         print("La frase a analizar es: ", data)
#         # Darle el input al lexer
#         if len(data)==0:
#             break
#         else:
#             lexer.input(data)
#             # Iteración de tokens
#             while True:
#                 tok = lexer.token()
#                 if not tok:
#                     break  # No more input
#                 print(tok)

