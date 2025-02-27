import sys
from PySide6.QtWidgets import QApplication
from Notacontroller import NotaController

def main():
    app = QApplication(sys.argv)
    controller = NotaController()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
