from PyQt5 import QtWidgets,uic,QtCore,QtGui
from PyQt5.QtWidgets import QMainWindow
from collections import deque 

lis=[]
stack=[]
pos=[]
ans=[]
trkr=0;
    
def back():
    ui.lineEdit.setReadOnly(False)
    a=ui.lineEdit.text()
    if(a[-1]=="."):ui.Button_dot.setEnabled(True)
    if(a[-1]=="+"):ui.Button_dot.setEnabled(False)
    if(a[-1]=="*"):ui.Button_dot.setEnabled(False)
    if(a[-1]=="/"):ui.Button_dot.setEnabled(False)
    if(a[-1]=="%"):ui.Button_dot.setEnabled(False)
    a=a[0:-1]
    ui.lineEdit.setText(a)
    ui.lineEdit.setReadOnly(True)

def oagain():
    global lis
    global stack
    global pos
    global ans
    global trkr
    print(trkr)
    trkr=0
    print(trkr)
    ui.lineEdit.setReadOnly(False)
    b=ui.lineEdit.text()
    b=""
    lis=lis[0:0]
    stack=stack[0:0]
    pos=pos[0:0]
    ans=ans[0:0]
    ui.lineEdit.setText(b)
    ui.lineEdit.setReadOnly(True)
    ui.Button_plus.setEnabled(False)
    ui.Button_mod.setEnabled(False)
    ui.Button_mul.setEnabled(False)
    ui.Button_divide.setEnabled(False)
    ui.Button_7.setEnabled(True)
    ui.Button_8.setEnabled(True)
    ui.Button_9.setEnabled(True)
    ui.Button_4.setEnabled(True)
    ui.Button_5.setEnabled(True)
    ui.Button_6.setEnabled(True)
    ui.Button_1.setEnabled(True)
    ui.Button_2.setEnabled(True)
    ui.Button_3.setEnabled(True)
    ui.Button_0.setEnabled(True)
    ui.Button_dot.setEnabled(False)

def seven():
    ui.lineEdit.setReadOnly(False)
    ui.lineEdit.insert("7" )
    ui.lineEdit.setReadOnly(True)
    ui.Button_plus.setEnabled(True)
    ui.Button_mod.setEnabled(True)
    ui.Button_mul.setEnabled(True)
    ui.Button_divide.setEnabled(True)
def eight():
    ui.lineEdit.setReadOnly(True)
    ui.Button_plus.setEnabled(True)
    ui.Button_mod.setEnabled(True)
    ui.Button_mul.setEnabled(True)
    ui.Button_divide.setEnabled(True)
    ui.lineEdit.setReadOnly(False)
    ui.lineEdit.insert("8" )
    ui.lineEdit.setReadOnly(True)
def nine():
    ui.lineEdit.setReadOnly(True)
    ui.Button_plus.setEnabled(True)
    ui.Button_mod.setEnabled(True)
    ui.Button_mul.setEnabled(True)
    ui.Button_divide.setEnabled(True)
    ui.lineEdit.setReadOnly(False)
    ui.lineEdit.insert("9" )
    ui.lineEdit.setReadOnly(True)

def four():
    ui.lineEdit.setReadOnly(True)
    ui.Button_plus.setEnabled(True)
    ui.Button_mod.setEnabled(True)
    ui.Button_mul.setEnabled(True)
    ui.Button_divide.setEnabled(True)
    ui.lineEdit.setReadOnly(False)
    ui.lineEdit.insert("4" )
    ui.lineEdit.setReadOnly(True)
def five():
    ui.lineEdit.setReadOnly(True)
    ui.Button_plus.setEnabled(True)
    ui.Button_mod.setEnabled(True)
    ui.Button_mul.setEnabled(True)
    ui.Button_divide.setEnabled(True)
    ui.lineEdit.setReadOnly(False)
    ui.lineEdit.insert("5" )
    ui.lineEdit.setReadOnly(True)
def six():
    ui.lineEdit.setReadOnly(True)
    ui.Button_plus.setEnabled(True)
    ui.Button_mod.setEnabled(True)
    ui.Button_mul.setEnabled(True)
    ui.Button_divide.setEnabled(True)
    ui.lineEdit.setReadOnly(False)
    ui.lineEdit.insert("6" )
    ui.lineEdit.setReadOnly(True)

def one():
    ui.lineEdit.setReadOnly(True)
    ui.Button_plus.setEnabled(True)
    ui.Button_mod.setEnabled(True)
    ui.Button_mul.setEnabled(True)
    ui.Button_divide.setEnabled(True)
    ui.lineEdit.setReadOnly(False)
    ui.lineEdit.insert("1" )
    ui.lineEdit.setReadOnly(True)
def two():
    ui.lineEdit.setReadOnly(True)
    ui.Button_plus.setEnabled(True)
    ui.Button_mod.setEnabled(True)
    ui.Button_mul.setEnabled(True)
    ui.Button_divide.setEnabled(True)
    ui.lineEdit.setReadOnly(False)
    ui.lineEdit.insert("2" )
    ui.lineEdit.setReadOnly(True)
    
def thre():
    ui.lineEdit.setReadOnly(True)
    ui.Button_plus.setEnabled(True)
    ui.Button_mod.setEnabled(True)
    ui.Button_mul.setEnabled(True)
    ui.Button_divide.setEnabled(True)
    ui.lineEdit.setReadOnly(False)
    ui.lineEdit.insert("3" )
    ui.lineEdit.setReadOnly(True)
def dec():
    ui.lineEdit.setReadOnly(False)
    ui.lineEdit.insert("." )
    ui.lineEdit.setReadOnly(True)
    ui.Button_dot.setEnabled(False)
def zero():
    
    ui.Button_plus.setEnabled(True)
    ui.Button_mod.setEnabled(True)
    ui.Button_mul.setEnabled(True)
    ui.Button_divide.setEnabled(True)
    ui.lineEdit.setReadOnly(False)
    ui.lineEdit.insert("0" )
    ui.lineEdit.setReadOnly(True)
def plus():
    global lis
    global trkr
    ui.Button_dot.setEnabled(True)
    ui.Button_7.setEnabled(True)
    ui.Button_8.setEnabled(True)
    ui.Button_9.setEnabled(True)
    ui.Button_4.setEnabled(True)
    ui.Button_5.setEnabled(True)
    ui.Button_6.setEnabled(True)
    ui.Button_1.setEnabled(True)
    ui.Button_2.setEnabled(True)
    ui.Button_3.setEnabled(True)
    ui.Button_0.setEnabled(True)
    ui.lineEdit.setReadOnly(True)
    ui.lineEdit.setReadOnly(False)
    #print("in plus")
    a=ui.lineEdit.text()
    print (trkr)
    print(a)
    a=ui.lineEdit.text()
    lis.append(float(a[trkr:len(a)]))
    #print(lis)
    ui.lineEdit.insert("+" )
    lis.append("+")
    a=ui.lineEdit.text()
    #print(a)
    trkr=len(a)
    #print(trkr)
    #print("End of plus")
    ui.lineEdit.setReadOnly(True)
def mod():
    global lis
    global trkr
    ui.Button_dot.setEnabled(True)
    ui.Button_7.setEnabled(True)
    ui.Button_8.setEnabled(True)
    ui.Button_9.setEnabled(True)
    ui.Button_4.setEnabled(True)
    ui.Button_5.setEnabled(True)
    ui.Button_6.setEnabled(True)
    ui.Button_1.setEnabled(True)
    ui.Button_2.setEnabled(True)
    ui.Button_3.setEnabled(True)
    ui.Button_0.setEnabled(True)
    ui.lineEdit.setReadOnly(True)
    ui.lineEdit.setReadOnly(False)
    #print("in mul")
    a=ui.lineEdit.text()
    #print (trkr)
    #print(a)
    a=ui.lineEdit.text()
    lis.append(float(a[trkr:len(a)]))
    #print(lis)
    ui.lineEdit.insert("%" )
    lis.append("%")
    #print(lis)
    #print(a)
    a=ui.lineEdit.text()
    trkr=len(a)
    #print(trkr)
    ui.lineEdit.setReadOnly(True)
def mul():
    global lis
    global trkr
    ui.Button_dot.setEnabled(True)
    ui.Button_7.setEnabled(True)
    ui.Button_8.setEnabled(True)
    ui.Button_9.setEnabled(True)
    ui.Button_4.setEnabled(True)
    ui.Button_5.setEnabled(True)
    ui.Button_6.setEnabled(True)
    ui.Button_1.setEnabled(True)
    ui.Button_2.setEnabled(True)
    ui.Button_3.setEnabled(True)
    ui.Button_0.setEnabled(True)
    ui.lineEdit.setReadOnly(False)
    #print("in mul")
    a=ui.lineEdit.text()
    #print (trkr)
    #print(a)
    a=ui.lineEdit.text()
    lis.append(float(a[trkr:len(a)]))
    #print(lis)
    ui.lineEdit.insert("*" )
    lis.append("*")
    #print(lis)
    #print(a)
    a=ui.lineEdit.text()
    trkr=len(a)
    #print(trkr)
    ui.lineEdit.setReadOnly(True)
    ui.lineEdit.setReadOnly(True)

def divide():
    global lis
    global trkr
    ui.Button_dot.setEnabled(True)
    ui.Button_7.setEnabled(True)
    ui.Button_8.setEnabled(True)
    ui.Button_9.setEnabled(True)
    ui.Button_4.setEnabled(True)
    ui.Button_5.setEnabled(True)
    ui.Button_6.setEnabled(True)
    ui.Button_1.setEnabled(True)
    ui.Button_2.setEnabled(True)
    ui.Button_3.setEnabled(True)
    ui.Button_0.setEnabled(True)
    ui.lineEdit.setReadOnly(False)
    #print("in mul")
    a=ui.lineEdit.text()
    #print (trkr)
    #print(a)
    a=ui.lineEdit.text()
    lis.append(float(a[trkr:len(a)]))
    #print(lis)
    ui.lineEdit.insert("/")
    lis.append("/")
    #print(lis)
    #print(a)
    a=ui.lineEdit.text()
    trkr=len(a)
    #print(trkr)
    ui.lineEdit.setReadOnly(True)
def enter():
    global lis
    global a
    print(lis)
    ui.lineEdit.setReadOnly(False)
    a=ui.lineEdit.text()
    print(a)
    lis.append(float(a[trkr:len(a)]))
    print(lis)
    infi_to_post()
    
    ui.lineEdit.setReadOnly(True)
    ui.Button_7.setEnabled(False)
    ui.Button_8.setEnabled(False)
    ui.Button_9.setEnabled(False)
    ui.Button_4.setEnabled(False)
    ui.Button_5.setEnabled(False)
    ui.Button_6.setEnabled(False)
    ui.Button_1.setEnabled(False)
    ui.Button_2.setEnabled(False)
    ui.Button_3.setEnabled(False)
    ui.Button_0.setEnabled(False)

def precedence(char):
    if char == '+' or char == '-':
        return 1
    elif char == '*':
        return 2
    elif char == '/':
        return 3
    else:
        return -1
def infi_to_post ():
    print("inside inp")
    global pos
    global stack
    print(pos)
    for i in lis:
        if (isinstance(i, float)):
            pos.append(i)
            print(pos)
        else:
                print(stack)
                if(len(stack)==0):
                    stack.append(i)
                    print(stack)
                else:
                    pp=stack.pop()
                    print(stack)
                    if(precedence(pp)>=precedence(i)):
                        while(precedence(pp)>=precedence(i)):
                            print("inside")
                            print(stack)
                            print(pos)
                            pos.append(pp)
                            if(len(stack)==0):break
                            else:
                                pp=stack.pop()
                                if(precedence(pp)<precedence(i)):
                                    stack.append(pp)
                            print(stack)
                            print(pos)
                        stack.append(i)
                    elif(precedence(pp)<precedence(i)):
                        stack.append(pp)
                        stack.append(i)
    print(pos)
    print(stack)
    while(len(stack)>0):
        pos.append(stack.pop())
    print(pos)
    posev()

def posev ():
    global pos
    global ans
    ans=ans[0:0]
    print("inside posev")
    for i in pos:
        print(pos)
        print(ans)
        if (isinstance(i, float)):
            ans.append(i)
        else:
            if(i=="+"):
                ans.append(ans.pop()+ans.pop())
            elif(i=="*"):
                ans.append(ans.pop()*ans.pop())
            elif(i=="/"):
                den=ans.pop()
                num=ans.pop()
                ans.append(num/den)
            elif(i=="%"):
                ans.append(ans.pop()%ans.pop())
            elif(i=="-"):
                ans.append(ans.pop()-ans.pop())
        print(pos)
        print(ans)
    print(ans[0])
    ui.lineEdit.setText(str(ans[0]))        

app=QtWidgets.QApplication([])
ui=uic.loadUi("Calc.ui")
ui.setWindowIcon(QtGui.QIcon("download.png"))
ui.setWindowTitle("Our calculator")
stylesheet = """
QPushButton#Button_9{
    Background-color : red;
    color:pink;

}
"""
app.setStyleSheet(stylesheet)
ui.Button_plus.setEnabled(False)
ui.Button_mod.setEnabled(False)
ui.Button_mul.setEnabled(False)
ui.Button_divide.setEnabled(False)
ui.Button_back.setShortcut("Backspace")
ui.Button_7.setShortcut("7")
ui.Button_8.setShortcut("8")
ui.Button_9.setShortcut("9")
ui.Button_6.setShortcut("6")
ui.Button_5.setShortcut("5")
ui.Button_4.setShortcut("4")
ui.Button_3.setShortcut("3")
ui.Button_2.setShortcut("2")
ui.Button_1.setShortcut("1")
ui.Button_0.setShortcut("0")
ui.Button_plus.setShortcut("+")
ui.Button_mod.setShortcut("Shift+5")
ui.Button_mul.setShortcut("*")
ui.ButtonEnter.setShortcut("Return")
ui.Button_divide.setShortcut("/")
ui.Button_dot.setShortcut(".")
ui.Button_back.clicked.connect(back)
ui.Button_7.clicked.connect(seven)
ui.Button_8.clicked.connect(eight)
ui.Button_9.clicked.connect(nine)
ui.Button_6.clicked.connect(six)
ui.Button_5.clicked.connect(five)
ui.Button_4.clicked.connect(four)
ui.Button_3.clicked.connect(thre)
ui.Button_2.clicked.connect(two)
ui.Button_1.clicked.connect(one)
ui.Button_0.clicked.connect(zero)
ui.Button_plus.clicked.connect(plus)
ui.Button_mod.clicked.connect(mod)
ui.Button_mul.clicked.connect(mul)
ui.ButtonEnter.clicked.connect(enter)
ui.Button_divide.clicked.connect(divide)
ui.Button_dot.clicked.connect(dec)
ui.pushButton_2.clicked.connect(oagain)
ui.show()
app.exec_()