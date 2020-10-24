#! /usr/bin/env python3
# coding: utf-8

# -*- coding: utf-8 -*-
"""
Created on Tue May 30 12:11:06 2020

@author: AGHEZZAF Mohamed & HAJJAJI Nassim
"""

from PyQt5 import QtCore, QtGui, QtWidgets

class About(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.setEnabled(True)
        Form.resize(321, 169)
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
"font-size:12px;\n"
"font-family:sans-serif;\n"
"}\n"
"#label_7{\n"
"font-size:20px;\n"
"color: #fff;\n"
"\n"
"text-align: center;\n"
"font-family:  Tahoma, sans-serif;\n"
"}\n"
"#label_4{\n"
"font-size:14px;\n"
"color: #fff;\n"
"\n"
"text-align: center;\n"
"font-family:  Tahoma, sans-serif;\n"
"}\n"
"#label_6{\n"
"font-size:14px;\n"
"color: #fff;\n"
"\n"
"text-align: center;\n"
"font-family:  Tahoma, sans-serif;\n"
"}\n"
"\n"
"QLabel{\n"
"color:white;\n"
"}\n"
"#frame_2{\n"
"background:url(images/us.png);\n"
"}\n"
"#frame1{\n"
"background:#16418e;\n"
"}\n"
)
        Form.setInputMethodHints(QtCore.Qt.ImhNone)
        self.frame1 = QtWidgets.QFrame(Form)
        self.frame1.setGeometry(QtCore.QRect(-60, 0, 491, 531))
        self.frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1.setObjectName("frame1")
        self.label_3 = QtWidgets.QLabel(self.frame1)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(180, 140, 61, 31))
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
        self.label_4 = QtWidgets.QLabel(self.frame1)
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QtCore.QRect(70, 40, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma,sans-serif")
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
        self.label_5.setGeometry(QtCore.QRect(130, 100, 171, 41))
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
        self.label_6 = QtWidgets.QLabel(self.frame1)
        self.label_6.setEnabled(True)
        self.label_6.setGeometry(QtCore.QRect(70, 70, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma,sans-serif")
        font.setPointSize(-1)
        self.label_6.setFont(font)
        self.label_6.setMouseTracking(True)
        self.label_6.setTabletTracking(False)
        self.label_6.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_6.setAcceptDrops(False)
        self.label_6.setStatusTip("")
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setAutoFillBackground(False)
        self.label_6.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_6.setTextFormat(QtCore.Qt.AutoText)
        self.label_6.setScaledContents(False)
        self.label_6.setWordWrap(False)
        self.label_6.setOpenExternalLinks(False)
        self.label_6.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame1)
        self.label_7.setEnabled(True)
        self.label_7.setGeometry(QtCore.QRect(185, 0, 71, 31))
        self.label_7.setMouseTracking(True)
        self.label_7.setTabletTracking(False)
        self.label_7.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_7.setAcceptDrops(False)
        self.label_7.setStatusTip("")
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setAutoFillBackground(False)
        self.label_7.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_7.setTextFormat(QtCore.Qt.AutoText)
        self.label_7.setScaledContents(False)
        self.label_7.setWordWrap(False)
        self.label_7.setOpenExternalLinks(False)
        self.label_7.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame1)
        self.label_8.setEnabled(True)
        self.label_8.setGeometry(QtCore.QRect(180, 120, 81, 41))
        self.label_8.setMouseTracking(True)
        self.label_8.setTabletTracking(False)
        self.label_8.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_8.setAcceptDrops(False)
        self.label_8.setStatusTip("")
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setAutoFillBackground(False)
        self.label_8.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_8.setTextFormat(QtCore.Qt.AutoText)
        self.label_8.setScaledContents(False)
        self.label_8.setWordWrap(False)
        self.label_8.setOpenExternalLinks(False)
        self.label_8.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_8.setObjectName("label_8")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "About"))
        self.label_3.setText(_translate("Form", "2019/2020"))
        self.label_4.setText(_translate("Form", "- Communication oral"))
        self.label_5.setText(_translate("Form", ""))
        self.label_6.setText(_translate("Form", "- Communication écrite"))
        self.label_7.setText(_translate("Form", "Chatbot"))
        self.label_8.setText(_translate("Form", "( Python )"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = About()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

