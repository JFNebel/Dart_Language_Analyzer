# Dart_Lexical_Analyzer (README SERÁ ACTUALIZADO PARA ACOMODARSE A LA NUEVA FUNCIONALIDAD PARA EL AVANCE FINAL)
Este proyecto escrito en Python simula lo que un analizador léxico básico del Dart haría al momento de analizar cadenas de caracteres. Esto lo logra a travez del uso de la librería PLY. Las frases a analizar se encuentran en el archivo aparte código.txt, estas serán leídas por lexer.py y por consola se mostraran los tokens que el lexer ha reconocido como parte del lenguaje a partir de los lexemas con los que fue alimentado. 

## Dependencias 

- Python3 o más reciente 
- PLY
```
pip install ply
```

### USO:
Se lo puede correr con cualquier IDE configurado como un ambiente de desarrollo para python o directamente desde consola al ir al directorio del proyecto:
```
python3 lexer.py 
```
### Resultados tipicos:<br/>

```
# La cadena es: 'for(int i = 0; i < 10; i++){}'

LexToken(FOR,'for',1,0)
LexToken(LPAREN,'(',1,3)
LexToken(INT,'int',1,4)
LexToken(ID,'i',1,8)
LexToken(EQUALS,'=',1,10)
LexToken(NUMBER,'0',1,12)
LexToken(PUNTCOM,';',1,13)
LexToken(ID,'i',1,15)
LexToken(MENORQUE,'<',1,17)
LexToken(NUMBER,'10',1,19)
LexToken(PUNTCOM,';',1,21)
LexToken(ID,'i',1,23)
LexToken(INCREMENTO,'++',1,24)
LexToken(RPAREN,')',1,26)
LexToken(LCURLYB,'{',1,27)
LexToken(RCURLYB,'}',1,28)
```



### Especificaciones:<br/>
1) El programa lexer.py necesita del archivo código.txt en su mismo directorio.
2) El archivo código.txt debe tener una frase por línea

### Backlog:<br/>
1) Implementar las retroalimentaciones dades del Avance 3.
2) Actualizar readme
3) Crear módulos para mejorar la organización de archivos del proyecto.

## Autores
- Juan Nebel Dunn
- Allison Brito
