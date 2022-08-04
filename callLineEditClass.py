import sys
from PyQt5.QtWidgets import QApplication, QDialog
from LineEditClass import *
from marksClass import Marks
from studentClass import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.dispMessage)

        self.show()
        
    def dispMessage(self):
        marksObj = Marks(self.ui.lineEdit.text(), self.ui.lineEditCode.text()\
            , self.ui.lineEditHistory.text(), self.ui.lineEditGeography.text())

        self.ui.label_2.setText("Hello " + marksObj.printName() + " " + marksObj.printCode()\
            + " History Marks: " + marksObj.getHistoryMarks() + " Geo Marks " +  marksObj.getGeographyMarks())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())