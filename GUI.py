import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from lexer import lexer, errores



'''
ToolBar
Supuestamente los "SLOTS" son respuestas que se disparan cuando detectan la signal asociada a esta
'''

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Esto determina las dimensiones de la ventana:
        self.resize(720, 600)

        # Supuestamente aquí se cargan preferencias (lo que sea que eso signifique)
        print("Aquí se cargan las configuraciones")


        # Aquí cargamos lo que denominamos "señales"
        # Conectamos señales (izq) a slots (derecha)
        self.windowTitleChanged.connect(self.onWindowTitleChange)
         
        self.windowTitleChanged.connect(lambda x: self.my_custom_fn())
        self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x))
        self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x, 25))


        # Esto determina el título de la ventana
        self.setWindowTitle("Este es el título de la ventana")

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
        self.output.insertPlainText("Aquí sale tu resultado rey!\n")
        self.output.move(360,95)
        self.output.resize(360,480)
        self.output.setReadOnly(True)

        # Añadir más widgets
        # toolbar.addWidget(QLabel("FIN?"))


        # Convertir a chequeables nuestras acctiones (lo que sea que eso signifique
        button_lexer.setCheckable(True)



        # Creamos la barra de estado
        self.setStatusBar(QStatusBar(self))

        # Aquí decimos cual será nuestro Widget central (lo que sea que eso signifique)
        self.setCentralWidget(label1)


    # Aquí definimos los comportanmientos (slots) que utilizamos en la sección se signals
    # Nota el nivel de sangría
    
    # El slot del lexer
    def onMyToolbarButtonLexico(self, s, label):
        errores.clear()
        self.output.setPlainText("")
        
        print("Se activa el lexer ")
        data = self.input.toPlainText()
        #print(data)

        lexer.input(data)
        while True:
            tok = lexer.token()
            if not tok:
                break  # No more input

        self.output.insertPlainText("Los errores detectados son: " + str (len(errores)) + "\n")
        for i in errores:
            self.output.insertPlainText(i + "\n")
            








        # self.output.setPlainText(input)



    def onMyToolbarButtonSyntax(self, s, label):
        print("Se activa el slot del syntax ",s )
        label.setText("Sintaxis finalizada")
        
    def onWindowTitleChange(self, s):
        print(s)

    def my_custom_fn(self, a = "Parametro por defecto", b = 5):
        print(a, b)

    def contextMenuEvent(self, event):
        print("Supuestamente esto debe imprimirse cuando hay un click derecho", event)


# Aquí ha terminado la clase que definimos

# Aquí pasamos a instanciar la apliación (nota el nivel de sangría)
app = QApplication(sys.argv)



# Aquí instanciamos window y hacemos que se muestre. Corremos la app
window = MainWindow()
window.show()
app.exec_()


print("Ha terminado la app")
