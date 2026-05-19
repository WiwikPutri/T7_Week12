# ==========================================
# NAMA  : WIWIK PUTRI
# NIM   : F1D02310096
# KELAS : C
# ==========================================

import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from dashboard import SupermarketDashboard

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wiwik Putri - F1D02310096")
        self.resize(1200, 750)
        
        self.dashboard = SupermarketDashboard()
        self.setCentralWidget(self.dashboard)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    app.setStyle('Fusion')
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec())