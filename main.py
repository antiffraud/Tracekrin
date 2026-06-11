import sys
import os
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QFont
from main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    
    icon_path = "assets/logo.png"  
    if os.path.exists(icon_path):
        app.setWindowIcon(QIcon(icon_path))
    
    import platform
    if platform.system() == 'Darwin':  
        font = QFont("Helvetica Neue", 10)
        if not font.exactMatch():
            font = QFont("Arial", 10)
            if not font.exactMatch():
                font = QFont("System", 10) 
    elif platform.system() == 'Windows':
        font = QFont("Segoe UI", 10)
        if not font.exactMatch():
            font = QFont("Arial", 10)
    else:
        font = QFont("Ubuntu", 10)
        if not font.exactMatch():
            font = QFont("DejaVu Sans", 10)
            if not font.exactMatch():
                font = QFont("Arial", 10)
    
    app.setFont(font)
    
    try:
        main_window = MainWindow()
        main_window.show()
        sys.exit(app.exec())
    except Exception as e:
        print(f"Error starting application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()