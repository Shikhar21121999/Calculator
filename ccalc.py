from PyQt5 import QtWidgets,uic,QtCore,QtGui
from PyQt5.QtWidgets import QMainWindow
from collections import deque 

lis=[]
stack=[]
pos=[]
ans=[]
trkr=0;
    
def back():
    global lis
    global stack
    global pos
    global ans
    global trkr
    lis=lis[0:0]
    stack=stack[0:0]
    pos=pos[0:0]
    ans=ans[0:0]
    ui.lineEdit.setReadOnly(False)
    a=ui.lineEdit.text()
    if(a[-1]=="."):ui.Button_dot.setEnabled(True)
    if(a[-1]=="+"):ui.Button_dot.setEnabled(False)
    if(a[-1]=="*"):ui.Button_dot.setEnabled(False)
    if(a[-1]=="/"):ui.Button_dot.setEnabled(False)
    if(a[-1]=="%"):ui.Button_dot.setEnabled(False)
    a=a[0:-1]
    if(len(a)==0):
        ui.Button_back.setEnabled(False)
        ui.Button_dot.setEnabled(True)
        lis=lis[0:0]
        stack=stack[0:0]
        pos=pos[0:0]
        ans=ans[0:0]
    ui.lineEdit.setText(a)
    ui.lineEdit.setReadOnly(True)


def oagain():
    ui.Button_back.setEnabled(False)
    ui.Button_dot.setEnabled(True)
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
    ui.Button_back.setEnabled(True)
    ui.lineEdit.setReadOnly(False)
    ui.lineEdit.insert("7" )
    ui.lineEdit.setReadOnly(True)
    ui.Button_plus.setEnabled(True)
    ui.Button_minus.setEnabled(True)
    ui.Button_mod.setEnabled(True)
    ui.Button_mul.setEnabled(True)
    ui.Button_divide.setEnabled(True)
def eight():
    ui.Button_back.setEnabled(True)
    ui.lineEdit.setReadOnly(True)
    ui.Button_plus.setEnabled(True)
    ui.Button_minus.setEnabled(True)
    ui.Button_mod.setEnabled(True)
    ui.Button_mul.setEnabled(True)
    ui.Button_divide.setEnabled(True)
    ui.lineEdit.setReadOnly(False)
    ui.lineEdit.insert("8" )
    ui.lineEdit.setReadOnly(True)
def nine():
    ui.Button_back.setEnabled(True)
    ui.lineEdit.setReadOnly(True)
    ui.Button_plus.setEnabled(True)
    ui.Button_minus.setEnabled(True)
    ui.Button_mod.setEnabled(True)
    ui.Button_mul.setEnabled(True)
    ui.Button_divide.setEnabled(True)
    ui.lineEdit.setReadOnly(False)
    ui.lineEdit.insert("9" )
    ui.lineEdit.setReadOnly(True)

def four():
    ui.Button_back.setEnabled(True)
    ui.lineEdit.setReadOnly(True)
    ui.Button_plus.setEnabled(True)
    ui.Button_minus.setEnabled(True)
    ui.Button_mod.setEnabled(True)
    ui.Button_mul.setEnabled(True)
    ui.Button_divide.setEnabled(True)
    ui.lineEdit.setReadOnly(False)
    ui.lineEdit.insert("4" )
    ui.lineEdit.setReadOnly(True)
def five():
    ui.Button_back.setEnabled(True)
    ui.lineEdit.setReadOnly(True)
    ui.Button_plus.setEnabled(True)
    ui.Button_minus.setEnabled(True)
    ui.Button_mod.setEnabled(True)
    ui.Button_mul.setEnabled(True)
    ui.Button_divide.setEnabled(True)
    ui.lineEdit.setReadOnly(False)
    ui.lineEdit.insert("5" )
    ui.lineEdit.setReadOnly(True)
def six():
    ui.Button_back.setEnabled(True)
    ui.lineEdit.setReadOnly(True)
    ui.Button_plus.setEnabled(True)
    ui.Button_minus.setEnabled(True)
    ui.Button_mod.setEnabled(True)
    ui.Button_mul.setEnabled(True)
    ui.Button_divide.setEnabled(True)
    ui.lineEdit.setReadOnly(False)
    ui.lineEdit.insert("6" )
    ui.lineEdit.setReadOnly(True)

def one():
    ui.Button_back.setEnabled(True)
    ui.lineEdit.setReadOnly(True)
    ui.Button_minus.setEnabled(True)
    ui.Button_plus.setEnabled(True)
    ui.Button_mod.setEnabled(True)
    ui.Button_mul.setEnabled(True)
    ui.Button_divide.setEnabled(True)
    ui.lineEdit.setReadOnly(False)
    ui.lineEdit.insert("1" )
    ui.lineEdit.setReadOnly(True)
def two():
    ui.Button_back.setEnabled(True)
    ui.lineEdit.setReadOnly(True)
    ui.Button_plus.setEnabled(True)
    ui.Button_mod.setEnabled(True)
    ui.Button_minus.setEnabled(True)
    ui.Button_mul.setEnabled(True)
    ui.Button_divide.setEnabled(True)
    ui.lineEdit.setReadOnly(False)
    ui.lineEdit.insert("2" )
    ui.lineEdit.setReadOnly(True)
    
def thre():
    ui.Button_back.setEnabled(True)
    ui.lineEdit.setReadOnly(True)
    ui.Button_plus.setEnabled(True)
    ui.Button_mod.setEnabled(True)
    ui.Button_mul.setEnabled(True)
    ui.Button_minus.setEnabled(True)
    ui.Button_divide.setEnabled(True)
    ui.lineEdit.setReadOnly(False)
    ui.lineEdit.insert("3" )
    ui.lineEdit.setReadOnly(True)
def dec():
    ui.Button_back.setEnabled(True)
    ui.lineEdit.setReadOnly(False)
    ui.lineEdit.insert("." )
    ui.lineEdit.setReadOnly(True)
    ui.Button_dot.setEnabled(False)
def zero():
    ui.Button_back.setEnabled(True)
    ui.Button_plus.setEnabled(True)
    ui.Button_mod.setEnabled(True)
    ui.Button_mul.setEnabled(True)
    ui.Button_divide.setEnabled(True)
    ui.Button_minus.setEnabled(True)
    ui.lineEdit.setReadOnly(False)
    ui.lineEdit.insert("0" )
    ui.lineEdit.setReadOnly(True)
def plus():
    ui.Button_back.setEnabled(True)
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
    ui.lineEdit.insert("+" )
    ui.lineEdit.setReadOnly(True)
def mod():
    ui.Button_back.setEnabled(True)
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
    ui.lineEdit.insert("%" )
    ui.lineEdit.setReadOnly(True)
def mul():
    ui.Button_back.setEnabled(True)
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
    ui.lineEdit.insert("*" )
    ui.lineEdit.setReadOnly(True)
    ui.lineEdit.setReadOnly(True)

def divide():
    ui.Button_back.setEnabled(True)
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
    ui.lineEdit.insert("/")
    ui.lineEdit.setReadOnly(True)

def sub ():
    ui.Button_back.setEnabled(True)
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
    ui.lineEdit.insert("-")
    ui.lineEdit.setReadOnly(True)

def strtolis(a):
    print("in str to lis")
    global lis
    btrkr=0 #peeche waala
    ftrkr=0 #aage waala
    l=len(a)
    while(btrkr<l and ftrkr<l):
        if(a[ftrkr]=="+"):
            print(lis)
            lis.append(float(a[btrkr:ftrkr]))
            print(lis)
            lis.append("+")
            btrkr=ftrkr+1
            ftrkr=btrkr
        elif(a[ftrkr]=="*"):
            print(lis)
            lis.append(float(a[btrkr:ftrkr]))
            print(lis)
            lis.append("*")
            btrkr=ftrkr+1
            ftrkr=btrkr
        elif(a[ftrkr]=="/"):
            print(lis)
            lis.append(float(a[btrkr:ftrkr]))
            print(lis)
            lis.append("/")
            btrkr=ftrkr+1
            ftrkr=btrkr
        elif(a[ftrkr]=="%"):
            print(lis)
            lis.appendfloat((a[btrkr:ftrkr]))
            print(lis)
            lis.append("%")
            btrkr=ftrkr+1
            ftrkr=btrkr
        elif(a[ftrkr]=="/"):
            print(lis)
            lis.append(float(a[btrkr:ftrkr]))
            print(lis)
            lis.append("/")
            btrkr=ftrkr+1
            ftrkr=btrkr
        elif(a[ftrkr]=="-"):
            print(lis)
            lis.append(float(a[btrkr:ftrkr]))
            print(lis)
            lis.append("-")
            btrkr=ftrkr+1
            ftrkr=btrkr
        elif(ftrkr==l-1):
            print(lis)
            lis.append(float(a[btrkr:l]))
            print(lis)
            btrkr=ftrkr+1
            ftrkr=btrkr
        else:
            ftrkr+=1
            continue
    print("str to lis done")
def enter():
    global lis
    global a
    ui.lineEdit.setReadOnly(False)
    a=ui.lineEdit.text()
    print(a)
    strtolis(a)
    print(lis)
    infi_to_post()
    
    ui.lineEdit.setReadOnly(True)
    

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
    global lis
    global stack
    global pos
    global ans
    global trkr
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
                den=ans.pop()
                num=ans.pop()
                ans.append(num%den)
            elif(i=="-"):
                den=ans.pop()
                num=ans.pop()
                ans.append(num-den)
        print(pos)
        print(ans)
    print(ans[0])
    ui.lineEdit.setText(str(ans[0]))
    lis=lis[0:0]
    stack=stack[0:0]
    pos=pos[0:0]
    ans=ans[0:0]        

app=QtWidgets.QApplication([])
ui=uic.loadUi("Calc.ui")
ui.setWindowIcon(QtGui.QIcon("download.png"))
ui.setWindowTitle("Our calculator")
stylesheet = """
QPushButton#Button_9{
    Background-color:#fb8d44;
    color:#000000;
}
QPushButton#Button_8{
    Background-color:#fb8d44;
    color:#000000;
}
QPushButton#Button_7{
    Background-color:#fb8d44;
    color:#000000;
}
QPushButton#Button_6{
    Background-color:#fb8d44;
    color:#000000;
}
QPushButton#Button_5{
    Background-color:#fb8d44;
    color:#000000;
}
QPushButton#Button_4{
    Background-color:#fb8d44;
    color:#000000;
}
QPushButton#Button_3{
    Background-color:#fb8d44;
    color:#000000;
}
QPushButton#Button_2{
    Background-color:#fb8d44;
    color:#000000;
}
QPushButton#Button_1{
    Background-color:#fb8d44;
    color:#000000;
}
QPushButton#Button_0{
    Background-color:#fb8d44;
    color:#000000;
}
QMainWindow{
    Background-color : #f9b146;
}
QPushButton#Button_plus{
    Background-color:#e8a357;
    color:#000000;
}
QPushButton#Button_mul{
    Background-color:#e8a357;
    color:#000000;
}
QPushButton#Button_mod{
    Background-color:#e8a357;
    color:#000000;
}
QPushButton#Button_divide{
    Background-color:#e8a357;
    color:#000000;
}
QPushButton#Button_minus{
    Background-color:#e8a357;
    color:#000000;
}
QPushButton#ButtonEnter{
    Background-color:#d08adf;
    color:#000000;
}
QPushButton#Button_back{
    Background-color:#d08adf;
    color:#000000;
}
QPushButton#Button_dot{
    Background-color:#d08adf;
    color:#000000;
}
QPushButton#pushButton_2{
    Background-color:#d08adf;
    color:#000000;
}
"""
app.setStyleSheet(stylesheet)
ui.Button_plus.setEnabled(False)
ui.Button_mod.setEnabled(False)
ui.Button_mul.setEnabled(False)
ui.Button_divide.setEnabled(False)
ui.Button_minus.setEnabled(False)
ui.Button_back.setEnabled(False)
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
ui.Button_divide.setShortcut("/")
ui.Button_minus.setShortcut("-")
ui.ButtonEnter.setShortcut("Return")
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
ui.Button_minus.clicked.connect(sub)
ui.Button_mod.clicked.connect(mod)
ui.Button_mul.clicked.connect(mul)
ui.ButtonEnter.clicked.connect(enter)
ui.Button_divide.clicked.connect(divide)
ui.Button_dot.clicked.connect(dec)
ui.pushButton_2.clicked.connect(oagain)
ui.show()
app.exec_()