import sys
from PyQt5.QtWidgets import QApplication, QDialog
from LineEditClass import *
from marksClass import Marks
from studentClass import *
from resultClass import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.dispMessage)

        self.show()
        
    def dispMessage(self):
        resultsObj = Results(self.ui.lineEdit.text(), self.ui.lineEditCode.text()\
            , int(self.ui.lineEditHistory.text()), int(self.ui.lineEditGeography.text()))
        self.ui.lineEditTotal.setText(str(resultsObj.getTotal()))
        self.ui.lineEditPercentage.setText(str(resultsObj.getPercentage()))
        self.ui.labelText.setText("HI "+resultsObj.printName()+" Code: "+resultsObj.printCode()+" Geo:"+str(resultsObj.getGeographyMarks())\
            +" History: "+str(resultsObj.getHistoryMarks()))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())