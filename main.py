from PyQt6.QtWidgets import (QApplication, QLabel,QWidget, 
QLineEdit, QPushButton, QMessageBox, QCheckBox, QDialog)
from PyQt6.QtGui import QFont, QPixmap #Esta mmda es pa imagenes

class mainwindow():
    
    def __init__(self):
        super().__init__()
        self.inicializar_ui()
    
    def inicializar_ui(self):
        self.setGeometry(100,100,350,250)
        self.setWindowTitle('Ventana principal')
        self.generar_contenido()

    def generar_contenido(self):
        image_path = 'logo.png'

        try: 
            with open(image_path):
                image_label = QLabel(self)
                image_label.setPixmap(QPixmap(image_path))
        
        except FileNotFoundError as e:
            QMessageBox.critical(self, 'Error', 'No se encontro la imagen',
            QMessageBox.StandardButton.close,
            QMessageBox.StandardButton.close)

        except Exception as e:
            QMessageBox.critical(self, 'Error', 'Ocurrio un error inesperado',
            QMessageBox.StandardButton.close,
            QMessageBox.StandardButton.close)