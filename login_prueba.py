import sys
from PyQt6.QtWidgets import (QApplication, QLabel, QWidget, 
QLineEdit, QPushButton, QMessageBox, QCheckBox, QDialog)
from PyQt6.QtGui import QFont, QPixmap, QColor, QPalette
from PyQt6.QtCore import Qt
from registro import registrarusuarioview
from main import mainwindow

class Login(QWidget):

    def __init__(self):
        super().__init__()
        self.set_ui_style()
        self.inicializar_ui()

    def set_ui_style(self):
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(20, 20, 30))  # Fondo oscuro
        self.setPalette(palette)

    def inicializar_ui(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('NASA Secure Login')
        self.generar_formulario()
        self.show()

    def generar_formulario(self):
        self.is_logged = False

        title_label = QLabel('NASA Secure Access', self)
        title_label.setFont(QFont('Consolas', 14, QFont.Weight.Bold))
        title_label.setStyleSheet("color: cyan;")
        title_label.move(100, 20)

        user_label = QLabel('Usuario:', self)
        user_label.setFont(QFont('Consolas', 10))
        user_label.setStyleSheet("color: white;")
        user_label.move(20, 70)

        self.user_input = QLineEdit(self)
        self.user_input.resize(250, 24)
        self.user_input.move(120, 68)
        self.user_input.setStyleSheet("background-color: #222; color: white; border: 1px solid cyan;")

        password_label = QLabel('Password:', self)
        password_label.setFont(QFont('Consolas', 10))
        password_label.setStyleSheet("color: white;")
        password_label.move(20, 110)

        self.password_input = QLineEdit(self)
        self.password_input.resize(250, 24)
        self.password_input.move(120, 108)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setStyleSheet("background-color: #222; color: white; border: 1px solid cyan;")

        self.check_view_password = QCheckBox('Mostrar contraseña', self)
        self.check_view_password.move(120, 140)
        self.check_view_password.setStyleSheet("color: cyan;")
        self.check_view_password.toggled.connect(self.mostrar_contrasena)

        login_button = QPushButton('Login', self)
        login_button.resize(320, 34)
        login_button.move(40, 180)
        login_button.setStyleSheet("background-color: cyan; color: black; font-weight: bold;")
        login_button.clicked.connect(self.login)

        register_button = QPushButton('Registrate', self)
        register_button.resize(320, 34)
        register_button.move(40, 230)
        register_button.setStyleSheet("background-color: #444; color: white;")
        register_button.clicked.connect(self.registrar_usuario)

    def mostrar_contrasena(self, clicked):
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
        self.new_user_form = registrarusuarioview()
        self.new_user_form.show()
    
    def open_main_window(self):
        self.main_window = mainwindow()
        self.main_window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Login()
    sys.exit(app.exec())
