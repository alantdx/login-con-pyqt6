import sys
from PyQt6.QtWidgets import (QApplication, QLabel,QWidget, 
QLineEdit, QPushButton, QMessageBox, QCheckBox, QDialog)
from PyQt6.QtGui import QFont, QPixmap #Esta mmda es pa imagenes
from registro import registrarusuarioview
from main import mainwindow

class Login(QWidget):

    def __init__(self):
        super().__init__()
        self.inicializar_ui()

    def inicializar_ui(self):
        self.setGeometry(100,100,350,250)
        self.setWindowTitle('Mi login')
        self.generar_formulario()
        self.show()

    def generar_formulario(self):
        self.is_logged = False

        user_label = QLabel(self)
        user_label.setText('Usuario:')
        user_label.setFont(QFont('Arial', 10))
        user_label.move(20,54)

        self.user_input = QLineEdit(self)
        self.user_input.resize(250, 24)
        self.user_input.move(90,50)

        password_label = QLabel(self)
        password_label.setText('Password:')
        password_label.setFont(QFont('Arial', 10))
        password_label.move(20,84)

        self.password_input = QLineEdit(self)
        self.password_input.resize(250, 24)
        self.password_input.move(90,82)
        self.password_input.setEchoMode(
            QLineEdit.EchoMode.Password) #Oculta la contraseña y es una variable estatica
        
        self.check_view_password = QCheckBox(self) #Crea un checkbox
        self.check_view_password.setText('Mostrar contraseña')
        self.check_view_password.move(90, 110)
        self.check_view_password.toggled.connect(self.mostrar_contrasena)

        login_button = QPushButton(self)
        login_button.setText('Login')
        login_button.resize(320,34)
        login_button.move(20, 140)
        login_button.clicked.connect(self.login)

        register_button = QPushButton(self)
        register_button.setText('Registrate')
        register_button.resize(320,34)
        register_button.move(20, 180)
        register_button.clicked.connect(self.registrar_usuario)

    def mostrar_contrasena(self,clicked):
        if clicked:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Normal)

        else:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

    def login(self):
        users = []
        users_path = 'usuarios.txt'

        try: 
            with open(users_path, 'r') as f:
                for line in f:
                    users.append(line.strip("\n"))
            login_informacion = f'{self.user_input.text()},{self.password_input.text()}'


            if login_informacion in users:
                QMessageBox.information(self, 'Inicio Sesion', 'Bienvenido',
                QMessageBox.StandardButton.Ok,
                QMessageBox.StandardButton.Ok)
                self.is_logged = True
                self.close()
                self.open_main_window()

            else:
                QMessageBox.critical(self, 'Error', 'Usuario o contraseña incorrectos',
                QMessageBox.StandardButton.Close,
                QMessageBox.StandardButton.Close)

        except FileNotFoundError as e:
            QMessageBox.critical(self, 'Error', 'No hay usuarios registrados',
            QMessageBox.StandardButton.Close,
            QMessageBox.StandardButton.Close)
        
        except Exception as e:
            QMessageBox.critical(self, 'Error', 'Ocurrió un error',
            QMessageBox.StandardButton.Close,
            QMessageBox.StandardButton.Close)


    def registrar_usuario(self):
        self.new_user_form =  registrarusuarioview()
        self.new_user_form.show()
    
    def open_main_window(self):
        self.main_window = mainwindow()
        self.main_window.show()

        



if __name__ == '__main__':
    app = QApplication(sys.argv) #se encarga de tomar las interacciones del usuario y enviarlas al sistema operativo
    login = Login()
    sys.exit(app.exec()) #Ejecuta la aplicación
