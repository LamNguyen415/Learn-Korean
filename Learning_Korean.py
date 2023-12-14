import csv
from PyQt5 import QtWidgets, uic
import sys
import random
import copy

class Ui(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.mainWindow = uic.loadUi('mainWindow.ui',self)
        filename = 'Book1.csv'
        self.data = self.loadData(filename)
        self.datalist = list(range(len(self.data)))
        self.startBtn.clicked.connect(self.open_dialog)
        self.choice = None
        self.Qrest = None
        self.rdAnswer = None
        self.correctAnswer = []
        self.wrongAnswer = []

    def loadData(self,filename):
        data = []
        with open(filename,'r',encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            your_list = list(reader)
            for i in range(len(your_list)):
                data.append([your_list[i][0],your_list[i][1]])
        return data
    def open_dialog(self):
        self.dialog = dialog()
        self.Qrest = copy.deepcopy(self.datalist)
        self.changeQuestion()
        
        self.dialog.pushButtonA.clicked.connect(self.open_messageA)
        self.dialog.pushButtonB.clicked.connect(self.open_messageB)
        self.dialog.pushButtonC.clicked.connect(self.open_messageC)
        self.dialog.pushButtonD.clicked.connect(self.open_messageD)

        self.dialog.exec_()
    def open_messageA(self):
        self.message = message()
        self.message.labelS.setText('Wrong!')
        self.message.labelQ.setText(self.question)
        self.message.labelA.setText(self.answer)
        if self.rdoption =='A':
            self.message.labelS.setText('Correct!')
            self.correctAnswer.append(self.data[self.choice])
            self.Qrest.remove(self.choice)
        self.message.pushButton.clicked.connect(self.OKButton)
        self.message.exec_()
    def open_messageB(self):
        self.message = message()
        self.message.labelS.setText('Wrong!')
        self.message.labelQ.setText(self.question)
        self.message.labelA.setText(self.answer)
        if self.rdoption =='B':
            self.message.labelS.setText('Correct!')
            self.correctAnswer.append(self.data[self.choice])
            self.Qrest.remove(self.choice)
        self.message.pushButton.clicked.connect(self.OKButton)
        self.message.exec_()
    def open_messageC(self):
        self.message = message()
        self.message.labelS.setText('Wrong!')
        self.message.labelQ.setText(self.question)
        self.message.labelA.setText(self.answer)
        if self.rdoption =='C':
            self.message.labelS.setText('Correct!')
            self.correctAnswer.append(self.data[self.choice])
            self.Qrest.remove(self.choice)
        self.message.pushButton.clicked.connect(self.OKButton)
        self.message.exec_()
    def open_messageD(self):
        self.message = message()
        self.message.labelS.setText('Wrong!')
        self.message.labelQ.setText(self.question)
        self.message.labelA.setText(self.answer)
        if self.rdoption =='D':
            self.message.labelS.setText('Correct!')
            self.correctAnswer.append(self.data[self.choice])
            self.Qrest.remove(self.choice)
        self.message.pushButton.clicked.connect(self.OKButton)

        self.message.exec_()
    def changeQuestion(self):
        self.choice = random.choice(self.Qrest)
        self.question = self.data[self.choice][0]
        self.answer = self.data[self.choice][1]
        
        self.failchoice = random.choices(self.Qrest,k=3)
        failAnswer1 = self.data[self.failchoice[0]][1]
        failAnswer2 = self.data[self.failchoice[1]][1]
        failAnswer3 = self.data[self.failchoice[2]][1]
        option = ['A','B','C','D']
        self.rdoption = random.choice(option)
        if self.rdoption == 'A':
            Astr = 'A. ' + self.answer
            Bstr = 'B. ' + failAnswer1
            Cstr = 'C. ' + failAnswer2
            Dstr = 'D. ' + failAnswer3
        elif self.rdoption == 'B':
            Bstr = 'B. ' + self.answer
            Astr = 'A. ' + failAnswer1
            Cstr = 'C. ' + failAnswer2
            Dstr = 'D. ' + failAnswer3
        elif self.rdoption == 'C':
            Cstr = 'C. ' + self.answer
            Bstr = 'B. ' + failAnswer1
            Astr = 'A. ' + failAnswer2
            Dstr = 'D. ' + failAnswer3
        elif self.rdoption == 'D':
            Dstr = 'D. ' + self.answer
            Bstr = 'B. ' + failAnswer1
            Cstr = 'C. ' + failAnswer2
            Astr = 'A. ' + failAnswer3
        Qstr = 'Q: ' + self.question
        Countstr = str(len(self.Qrest))+'/'+str(len(self.datalist))
        self.dialog.pushButtonA.setText(Astr)
        self.dialog.pushButtonB.setText(Bstr)
        self.dialog.pushButtonC.setText(Cstr)
        self.dialog.pushButtonD.setText(Dstr)
        self.dialog.labelQ.setText(Qstr)
        self.dialog.labelCount.setText(Countstr)
        self.dialog.labelCorrect.setText('correct: '+str(len(self.correctAnswer)))
        self.dialog.labelWrong.setText('')
    def OKButton(self):
        self.changeQuestion()
        self.message.close()
class dialog(QtWidgets.QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.dialog = uic.loadUi('UiLearning.ui',self)

class message(QtWidgets.QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.message = uic.loadUi('message.ui',self)

app = QtWidgets.QApplication(sys.argv)
window = Ui()
window.show()
sys.exit(app.exec_())



