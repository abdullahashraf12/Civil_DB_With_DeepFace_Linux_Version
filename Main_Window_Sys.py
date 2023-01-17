from All import MainWindow
from PySide6.QtWidgets import QApplication

import sys

def main():
    
    app = QApplication([])
    x=MainWindow()
    sys.exit(app.exec())

main()