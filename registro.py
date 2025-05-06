import sys
from PyQt6.QtWidgets import (QApplication, QLabel, QLineEdit, QDialog, QPushButton, QMessageBox)
from PyQt6.QtGui import QFont

class registrarusuarioview(QDialog):
    def __init__(self):
        super().__init__()
        self.setModal(True) # Hace que la ventana sea modal y no pueda usar la clase padre 
        self.init_ui()

    def init_ui(self):
        self.setGeometry(100, 100, 350, 250)
        self.setWindowTitle('Registro de Usuario')

        # Label y campo de Usuario
        user_label = QLabel('Usuario:', self)
        user_label.setFont(QFont('Arial', 10))
        user_label.move(20, 40)

        self.user_input = QLineEdit(self)
        self.user_input.resize(250, 24)
        self.user_input.move(90, 38)

        # Label y campo de Password 1
        password_1_label = QLabel('Contraseña:', self)  # Cambiado para diferenciar
        password_1_label.setFont(QFont('Arial', 10))
        password_1_label.move(20, 80)

        self.password_1_input = QLineEdit(self)
        self.password_1_input.resize(250, 24)
        self.password_1_input.move(90, 78)
        self.password_1_input.setEchoMode(QLineEdit.EchoMode.Password)

        # Label y campo de Confirmar Password
        password_2_label = QLabel('Confirmar:', self)  # Cambiado para diferenciar
        password_2_label.setFont(QFont('Arial', 10))
        password_2_label.move(20, 120)

        self.password_2_input = QLineEdit(self)
        self.password_2_input.resize(250, 24)
        self.password_2_input.move(90, 118)
        self.password_2_input.setEchoMode(QLineEdit.EchoMode.Password)

        create_button = QPushButton(self)
        create_button.setText('Crear cuenta')
        create_button.resize(150, 32)
        create_button.move(20, 170)
        create_button.clicked.connect(self.crear_usuario)

        cancel_button = QPushButton(self)
        cancel_button.setText('Cancelar')
        cancel_button.resize(150, 32)
        cancel_button.move(170, 170)
        cancel_button.clicked.connect(self.cancelar_registro)

    def cancelar_registro(self):
        self.close()

    def crear_usuario(self):
        user_path = 'usuarios.txt'
        usuario = self.user_input.text()
        password_1 = self.password_1_input.text()
        password_2 = self.password_2_input.text()
        # Verificar que los campos no estén vacíos
        if password_1 == '' or password_2 == '' or usuario == '':
            QMessageBox.critical(self, 'Error', 'No puede haber campos vacíos',
            QMessageBox.StandardButton.Close, 
            QMessageBox.StandardButton.Close)

        elif password_1 != password_2:
            QMessageBox.critical(self, 'Error', 'Las contraseñas no coinciden',
            QMessageBox.StandardButton.Close, 
            QMessageBox.StandardButton.Close)
        # Verificar que las contraseñas coincidan

        else:
            try:
                with open(user_path, 'a+') as f:
                    f.write(f'{usuario},{password_1}\n')
                    QMessageBox.information(self, 'Éxito', 'Usuario creado con éxito',
                    QMessageBox.StandardButton.Ok, 
                    QMessageBox.StandardButton.Ok)
                    self.close()

            except FileNotFoundError as e:
                QMessageBox.critical(self, 'Error', 'No se encontró el archivo de usuarios',
                QMessageBox.StandardButton.Close, 
                QMessageBox.StandardButton.Close)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = registrarusuarioview()
    window.show()
    sys.exit(app.exec())


