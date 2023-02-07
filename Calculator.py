# ***** CALCULATOR *****

from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtWidgets import QLineEdit,QPushButton
from PyQt5.QtGui import QFont
import sys

app=QApplication(sys.argv)
app.setStyle('Plastique')

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setFixedSize(420,630)
        self.Main()
    def Font(self,obj,x,y,z,t):
        obj.setFont(QFont('Times',15))
        obj.setFixedSize(z,t)
        obj.move(x,y)
    def Main(self):
        self.input1=QLineEdit(self)
        self.Font(self.input1,10,250,400,50)
        self.input1.setPlaceholderText('0')
        self.input1.setStyleSheet('''
            color: black;
            border-bottom-width: 1px;
            border-style: solid;
            border-color: rgb(206, 214, 224);''')
        
        self.one=QPushButton('1',self)
        self.Font(self.one,10,300,80,80)
        self.one.clicked.connect(self.One)

        self.two=QPushButton('2',self)
        self.Font(self.two,90,300,80,80)
        self.two.clicked.connect(self.Two)

        self.three=QPushButton('3',self)
        self.Font(self.three,170,300,80,80)
        self.three.clicked.connect(self.Three)

        self.four=QPushButton('4',self)
        self.Font(self.four,10,380,80,80)
        self.four.clicked.connect(self.Four)

        self.five=QPushButton('5',self)
        self.Font(self.five,90,380,80,80)
        self.five.clicked.connect(self.Five)

        self.six=QPushButton('6',self)
        self.Font(self.six,170,380,80,80)
        self.six.clicked.connect(self.Six)

        self.seven=QPushButton('7',self)
        self.Font(self.seven,10,460,80,80)
        self.seven.clicked.connect(self.Seven)

        self.eight=QPushButton('8',self)
        self.Font(self.eight,90,460,80,80)
        self.eight.clicked.connect(self.Eight)

        self.nine=QPushButton('9',self)
        self.Font(self.nine,170,460,80,80)
        self.nine.clicked.connect(self.Nine)

        self.zero=QPushButton('0',self)
        self.Font(self.zero,90,540,80,80)
        self.zero.clicked.connect(self.Zero)

        self.back=QPushButton('⌫',self)
        self.Font(self.back,170,540,80,80)
        self.back.clicked.connect(self.Back)
        self.back.setStyleSheet("""
            color: white;
            background-color: #F2921D;
        """)

        self.clear=QPushButton('C',self)
        self.Font(self.clear,10,540,80,80)
        self.clear.clicked.connect(self.Clear)
        self.clear.setStyleSheet("""
            color: white;
            background-color: #F2921D;
        """)

        self.equal=QPushButton('=',self)
        self.Font(self.equal,250,540,160,80)
        self.equal.clicked.connect(self.Equal)
        self.equal.setStyleSheet("""
            color: white;
            background-color: #F2921D;
        """)

        self.plus=QPushButton('+',self)
        self.Font(self.plus,250,300,80,80)
        self.plus.clicked.connect(self.Plus)
        self.plus.setStyleSheet("""
            color: white;
            background-color: #F2921D;
        """)

        self.minus=QPushButton('-',self)
        self.Font(self.minus,330,300,80,80)
        self.minus.clicked.connect(self.Minus)
        self.minus.setStyleSheet("""
            color: white;
            background-color: #F2921D;
        """)

        self.divide=QPushButton('/',self)
        self.Font(self.divide,250,380,80,80)
        self.divide.clicked.connect(self.Divide)
        self.divide.setStyleSheet("""
            color: white;
            background-color: #F2921D;
        """)

        self.multiple=QPushButton('*',self)
        self.Font(self.multiple,330,380,80,80)
        self.multiple.clicked.connect(self.Multiple)
        self.multiple.setStyleSheet("""
            color: white;
            background-color: #F2921D;
        """)

        self.lbreak=QPushButton('(',self)
        self.Font(self.lbreak,250,460,80,80)
        self.lbreak.clicked.connect(self.Lbreak)
        self.lbreak.setStyleSheet("""
            color: white;
            background-color: #F2921D;
        """)

        self.rbreak=QPushButton(')',self)
        self.Font(self.rbreak,330,460,80,80)
        self.rbreak.clicked.connect(self.Rbreak)
        self.rbreak.setStyleSheet("""
            color: white;
            background-color: #F2921D;
        """)

    def One(self,):
        self.input1.setText(self.input1.text()+self.one.text())
    def Two(self):
        self.input1.setText(self.input1.text()+self.two.text())
    def Three(self):
        self.input1.setText(self.input1.text()+self.three.text())
    def Four(self):
        self.input1.setText(self.input1.text()+self.four.text())
    def Five(self):
        self.input1.setText(self.input1.text()+self.five.text())
    def Six(self):
        self.input1.setText(self.input1.text()+self.six.text())
    def Seven(self):
        self.input1.setText(self.input1.text()+self.seven.text())
    def Eight(self):
        self.input1.setText(self.input1.text()+self.eight.text())
    def Nine(self):
        self.input1.setText(self.input1.text()+self.nine.text())
    def Zero(self):
        if len(self.input1.text())!=0:
            if self.input1.text()[0] in '123456789':
                self.input1.setText(self.input1.text()+self.zero.text())
    def Back(self):
        try:
            ls=[]
            temp=''
            for i in self.input1.text():
                ls.append(i)
            ls.pop()
            for i in ls:
                temp+=i
            self.input1.setText(temp)
        except:
            self.input1.setText('')
    def Plus(self):
        if len(self.input1.text())!=0:
            if self.plus.text()!=self.input1.text()[-1] and self.input1.text()[-1]!='-'  and self.input1.text()[-1]!='*' and self.input1.text()!='/' and self.input1.text()[-1]!='(':
                self.input1.setText(self.input1.text()+self.plus.text())
    def Minus(self):
        if len(self.input1.text())!=0:
            if self.minus.text()!=self.input1.text()[-1] and self.input1.text()[-1]!='+' and self.input1.text()[-1]!='*' and self.input1.text()!='/' and self.input1.text()[-1]!='(':
                self.input1.setText(self.input1.text()+self.minus.text())
    def Multiple(self):
        if len(self.input1.text())!=0:
            if self.multiple.text()!=self.input1.text()[-1] and self.input1.text()[-1]!='+' and self.input1.text()[-1]!='-' and self.input1.text()[-1]!='/' and self.input1.text()[-1]!='(':
                self.input1.setText(self.input1.text()+self.multiple.text())
    def Divide(self):
        if len(self.input1.text())!=0:
            if self.divide.text()!=self.input1.text()[-1] and self.input1.text()[-1]!='+' and self.input1.text()[-1]!='-' and self.input1.text()[-1]!='*' and self.input1.text()[-1]!='(':
                self.input1.setText(self.input1.text()+self.divide.text())
    def Rbreak(self):
        if len(self.input1.text())!=0:
            if self.rbreak.text()!=self.input1.text()[-1] and self.input1.text()[-1]!='+' and self.input1.text()[-1]!='-' and self.input1.text()[-1]!='*' and self.input1.text()[-1]!='/' and self.input1.text()[-1]!='(' and self.lbreak.text() in self.input1.text():
                self.input1.setText(self.input1.text()+self.rbreak.text())
    def Lbreak(self):
        if len(self.input1.text())!=0:
            if self.lbreak.text()!=self.input1.text()[-1] and self.input1.text()[-1] not in '0123456789':
                self.input1.setText(self.input1.text()+self.lbreak.text())
    def Equal(self):
        if len(self.input1.text())!=0:
            if self.input1.text()[-1] not in '+-*/':
                self.input1.setText(str(eval(self.input1.text())))
    def Clear(self):
        self.input1.setText('')

window=Window()
window.setStyleSheet('background-color: #BFBFBF;')
window.show()

sys.exit(app.exec_())