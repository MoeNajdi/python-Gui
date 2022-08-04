import sys
from PyQt5.QtWidgets import QApplication, QDialog
from LineEditClass import *
from studentClass import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.dispMessage)

        self.show()
        
    def dispMessage(self):
        studentObj = Student(self.ui.lineEdit.text())
        self.ui.label_2.setText("Hello " + studentObj.printName())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())