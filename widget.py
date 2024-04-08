import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QTimeEdit
from PyQt5.QtCore import QTime
import subprocess

class ShutdownApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Shutdown Timer')

        self.timeEdit = QTimeEdit()
        self.timeEdit.setDisplayFormat('HH:mm')
        self.timeEdit.setTime(QTime.currentTime())

        self.shutdownButton = QPushButton('Shutdown')
        self.shutdownButton.clicked.connect(self.shutdown)

        layout = QVBoxLayout()
        layout.addWidget(self.timeEdit)
        layout.addWidget(self.shutdownButton)

        self.setLayout(layout)

    def shutdown(self):
        shutdown_time = self.timeEdit.time().toString('HH:mm')
        hours, minutes = map(int, shutdown_time.split(':'))
        shutdown_seconds = hours * 3600 + minutes * 60

        subprocess.run(['shutdown', '/s', '/t', str(shutdown_seconds)])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ShutdownApp()
    window.show()
    sys.exit(app.exec_())
