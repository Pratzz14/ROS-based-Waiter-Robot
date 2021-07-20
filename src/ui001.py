#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import rospy
from geometry_msgs.msg import Twist

move_cmd = Twist()

class Ui_Form(object):
    def setupUi(self, Form):

        def forwardButton_pressed():

            global move_cmd

            move_cmd.linear.x = 1.0
            pub.publish(move_cmd)

        def forwardButton_released():

            global move_cmd

            move_cmd.linear.x = 0.0
            pub.publish(move_cmd)



        Form.setObjectName("Form")
        Form.resize(294, 263)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 291, 261))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.forwardButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.forwardButton.setObjectName("forwardButton")
        self.gridLayout.addWidget(self.forwardButton, 0, 0, 1, 1)
        self.stopButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.stopButton.setFont(font)
        self.stopButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.stopButton.setObjectName("stopButton")
        self.gridLayout.addWidget(self.stopButton, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.forwardButton.pressed.connect(forwardButton_pressed)
        self.forwardButton.released.connect(forwardButton_released)

        

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.forwardButton.setText(_translate("Form", "Forward"))
        self.stopButton.setText(_translate("Form", "Stop"))

        
    


if __name__ == "__main__":
    import sys

    rospy.init_node('UI_001')

    pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

