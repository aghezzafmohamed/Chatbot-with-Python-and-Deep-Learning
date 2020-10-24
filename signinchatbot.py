#! /usr/bin/env python3
# coding: utf-8

"""
Created on Tue Apr 01 09:01:02 2020

@author: AGHEZZAF Mohamed & HAJJAJI Nassim
"""

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from application import Application

class SignIn(object):
    def connexion(self):
            md = self.lineEdit_2.text()
            id = self.lineEdit.text()
            if id != "" and md != "":
                #connexion to data base
                if(id == "1411023210" and md == "chatbot"):
                    #connexion to data base
                    print("valide")
                    self.window = QtWidgets.QMainWindow()
                    self.ui = Application()
                    self.ui.setupUi(self.window)
                    Form.hide()
                    self.window.show()
                            
                else:
                    print("Les données sont incorréctes")
                    self.lineEdit.clear()
                    self.lineEdit_2.clear()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.setEnabled(True)
        Form.resize(419, 527)
        font = QtGui.QFont()
        font.setFamily("sans-serif")
        font.setPointSize(-1)
        Form.setFont(font)
        Form.setMouseTracking(False)
        Form.setTabletTracking(False)
        Form.setFocusPolicy(QtCore.Qt.NoFocus)
        Form.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        Form.setAcceptDrops(False)
        Form.setToolTip("")
        Form.setStatusTip("")
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("*{\n"
"font-size:20px;\n"
"font-family:sans-serif;\n"
"}\n"
"#label{\n"
"\n"
"    color: #fff;\n"
"    text-align: center;\n"
"    font-family:  Tahoma, sans-serif;\n"
"}\n"
"#label_4{\n"
"background:url(images/us.png);\n"
"height: 5px\n"
"}\n"
"#label_2{\n"
"background:#13386d;\n"
"height: 5px\n"
"}\n"
"QLabel{\n"
"color:white;\n"
"}\n"
"#frame_2{\n"
"background:url(images/us.png);\n"
"}\n"
"#frame1{\n"
"background:#16418e;\n"
"}\n"
"#pushButton{\n"
"background:rgba(0,0,0,0.6);\n"
"color:#fff;\n"
"border-radius:15px;\n"
"}\n"
"#pushButton_2{\n"
"  display:block;\n"
"  height: 300px;\n"
"  width: 300px;\n"
"  border-radius: 50%;\n"
"}\n"
"#pushButton:hover{\n"
"background:#13386d;\n"
"color:#fff;\n"
"border-radius:15px;\n"
"}\n"
"QLineEdit\n"
"{\n"
"border-radius:15px;\n"
"background:transparent;\n"
"border:none;\n"
"color:#fff;\n"
"border-bottom:1px solid #fff;\n"
"}\n"
)
        Form.setInputMethodHints(QtCore.Qt.ImhNone)
        self.frame1 = QtWidgets.QFrame(Form)
        self.frame1.setGeometry(QtCore.QRect(-60, 0, 491, 531))
        self.frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1.setObjectName("frame1")
        self.pushButton_2 = QtWidgets.QLabel(self.frame1)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 40, 151, 151))
        self.pushButton_2.setMouseTracking(True)
        self.pushButton_2.setTabletTracking(False)
        self.pushButton_2.setAcceptDrops(False)
        self.pushButton_2.setAccessibleDescription("")
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pushButton_2.setText("")    
        movie = QtGui.QMovie("images/chatbot.gif")
        self.pushButton_2.setMovie(movie)
        movie.start()
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.frame1)
        self.label_2.setGeometry(QtCore.QRect(60, 0, 451, 41))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.frame1)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(90, 460, 341, 41))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame1)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 370, 321, 41))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.frame1)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(100, 340, 141, 41))
        self.label_3.setMouseTracking(True)
        self.label_3.setTabletTracking(False)
        self.label_3.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_3.setAcceptDrops(False)
        self.label_3.setStatusTip("")
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setScaledContents(False)
        self.label_3.setWordWrap(False)
        self.label_3.setOpenExternalLinks(False)
        self.label_3.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.frame1)
        self.lineEdit.setGeometry(QtCore.QRect(100, 270, 321, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.frame1)
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QtCore.QRect(100, 240, 121, 31))
        font = QtGui.QFont()
        font.setFamily("sans-serif")
        font.setPointSize(-1)
        self.label_4.setFont(font)
        self.label_4.setMouseTracking(True)
        self.label_4.setTabletTracking(False)
        self.label_4.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_4.setAcceptDrops(False)
        self.label_4.setStatusTip("")
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setScaledContents(False)
        self.label_4.setWordWrap(False)
        self.label_4.setOpenExternalLinks(False)
        self.label_4.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame1)
        self.label_5.setEnabled(True)
        self.label_5.setGeometry(QtCore.QRect(220, -10, 171, 51))
        font = QtGui.QFont()
        font.setFamily("sans-serif")
        font.setPointSize(-1)
        self.label_5.setFont(font)
        self.label_5.setMouseTracking(True)
        self.label_5.setTabletTracking(False)
        self.label_5.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_5.setAcceptDrops(False)
        self.label_5.setStatusTip("")
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setScaledContents(False)
        self.label_5.setWordWrap(False)
        self.label_5.setOpenExternalLinks(False)
        self.label_5.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_5.setObjectName("label_5")
        self.label_2.raise_()
        self.pushButton_2.raise_()
        self.pushButton.raise_()
        self.lineEdit_2.raise_()
        self.label_3.raise_()
        self.lineEdit.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.pushButton.clicked.connect(self.connexion)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Authentification"))
        self.pushButton.setText(_translate("Form", "Connexion"))
        self.lineEdit_2.setText(_translate("Form", ""))
        self.label_3.setText(_translate("Form", "Mot de passe"))
        self.lineEdit.setText(_translate("Form", ""))
        self.label_4.setText(_translate("Form", "CNE/Massar"))
        self.label_5.setText(_translate("Form", "Connexion"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = SignIn()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
