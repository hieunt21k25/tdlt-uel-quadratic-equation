from PyQt6.QtWidgets import QApplication, QMainWindow

from learn_gui.quadratic_equation.QuadraticEquation_MainWindowEx import QuadraticEquation_MainWindowEx

app=QApplication([])
my_gui=QuadraticEquation_MainWindowEx()
my_gui.setupUi(QMainWindow())
my_gui.showWindow()
app.exec()
