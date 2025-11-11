from MainWindow import Ui_MainWindow
from PyQt6.QtWidgets import QMessageBox
from myultilities import quadratic


class MainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAnhSlot()

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAnhSlot(self):
        self.pushButtonSolution.clicked.connect(self.process_solution)
        self.pushButtonClear.clicked.connect(self.process_clear)
        self.pushButtonClose.clicked.connect(self.process_close)

    def process_solution(self):
        a = float(self.lineEditA.text())
        b = float(self.lineEditB.text())
        c = float(self.lineEditC.text())
        result = quadratic(a, b, c)
        self.lineEditResult.setText(result)

    def process_clear(self):
        self.lineEditA.setText("")
        self.lineEditB.setText("")
        self.lineEditC.setText("")
        self.lineEditResult.setText("")
        self.lineEditA.setFocus()

    def process_close(self):
        dlg = QMessageBox(self.MainWindow)
        dlg.setWindowTitle("Exit Confirmation")
        dlg.setText("Are you sure you want to Exit?")
        dlg.setStandardButtons(
            QMessageBox.StandardButton.Yes
            | QMessageBox.StandardButton.No
        )
        dlg.setIcon(QMessageBox.Icon.Question)
        button = dlg.exec()
        # check the user confirmation
        button = QMessageBox.StandardButton(button)
        if button == QMessageBox.StandardButton.Yes:
            self.MainWindow.close()
        else:
            pass  # do nothing