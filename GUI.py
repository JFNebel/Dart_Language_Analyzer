import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from lexer import lexer, erroresL
from syntax import parser,erroresS



'''
ToolBar
Supuestamente los "SLOTS" son respuestas que se disparan cuando detectan la signal asociada a esta
'''

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Esto determina las dimensiones de la ventana:
        self.resize(720, 600)

        # Aquí cargamos lo que denominamos "señales"
        # Conectamos señales (izq) a slots (derecha)
        #self.windowTitleChanged.connect(self.onWindowTitleChange)

        # Esto determina el título de la ventana
        self.setWindowTitle("Analizador Léxico y Sintáctico de Dart")

        # Aquí ponemos los Widgets que queramos
        label1 = QLabel("ToolBar") 
        label1.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label1) # Esto lo necesitamos para el slot de button_lexer


        #Creación del Toolbar
        toolbar = QToolBar("Mi primer toolbar")
        toolbar.setIconSize(QSize(64, 64))
        self.addToolBar(toolbar)
        self.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        # Acciones del toolbar
        button_lexer = QAction(QIcon("LexerIcon.png"), "Analizador léxico", self)
        button_lexer.setStatusTip("Lex") # Esto es el estado que se va a mostrar en la barra de estados que haremos luego
        button_lexer.triggered.connect(lambda x: self.onMyToolbarButtonLexico(x, label = label1))
        toolbar.addAction(button_lexer) # Esto añade el botón del lexer

        toolbar.addSeparator() #Separa los íconos

        button_syntax = QAction(QIcon("Syntax.png"), "Analizador sintáctico", self)
        button_syntax.setStatusTip("Syntax") # Esto es el estado que se va a mostrar en la barra de estados que haremos luego
        button_syntax.triggered.connect(lambda x: self.onMyToolbarButtonSyntax(x, label = label1))
        toolbar.addAction(button_syntax) # Esto añade el botón del lexer


        #Text Area Input
        self.input = QPlainTextEdit(self)
        self.input.move(0,95)
        self.input.resize(360,480)


        # Text Area Output
        self.output = QPlainTextEdit(self)
        self.output.insertPlainText("Aquí verás tu resultado!\n")
        self.output.move(360,95)
        self.output.resize(360,480)
        self.output.setReadOnly(True)

        # Añadir más widgets
        # toolbar.addWidget(QLabel("FIN?"))


        # Convertir a chequeables nuestras acctiones (lo que sea que eso signifique
        button_lexer.setCheckable(True)
        button_syntax.setCheckable(True)




        # Creamos la barra de estado
        self.setStatusBar(QStatusBar(self))

        # Aquí decimos cual será nuestro Widget central (lo que sea que eso signifique)
        self.setCentralWidget(label1)


    # Aquí definimos los comportanmientos (slots) que utilizamos en la sección se signals
    # Nota el nivel de sangría
    
    # El slot del lexer
    def onMyToolbarButtonLexico(self, s, label):
        erroresL.clear()
        self.output.setPlainText("")
        
        #print("Se activa el lexer ")
        data = self.input.toPlainText()
        #print(data)

        lexer.input(data)
        while True:
            tok = lexer.token()
            if not tok:
                break  # No more input

        self.output.insertPlainText("Errores léxicos detectados: " + str (len(erroresL)) + "\n")
        for i in erroresL:
            self.output.insertPlainText(i + "\n")

        # self.output.setPlainText(input)

    #El slot del parser/sintactico
    def onMyToolbarButtonSyntax(self, s, label):
        erroresS.clear()
        self.output.setPlainText("")
        #print("Se activa el slot del syntax ",s )
        dataT = self.input.toPlainText()
        #print("esto es data"+dataT)
        dataT=dataT.split("\r\n")
        for data in dataT:
            # if len(data)==0:
            #     self.output.insertPlainText("No ha ingresado texto" + "\n")
            # else:
            #     result = parser.parse(data)
            #     print(result)
            result = parser.parse(data)
        self.output.insertPlainText("Errores sintácticos detectados: " + str (len(erroresS)) + "\n")
        for i in erroresS:
            self.output.insertPlainText(i)

        

# Aquí ha terminado la clase que definimos

# Aquí pasamos a instanciar la apliación (nota el nivel de sangría)
app = QApplication(sys.argv)



# Aquí instanciamos window y hacemos que se muestre. Corremos la app
window = MainWindow()
window.show()
app.exec_()


print("Ha terminado la app")
