#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64

move_cmd = Twist()

class Ui_Form(object):
    def setupUi(self, Form):

        def button_released():
            global move_cmd
            move_cmd.linear.x = 0.0
            move_cmd.angular.z = 0.0
            pub.publish(move_cmd)

        def fl_button_pressed():
            global move_cmd
            move_cmd.linear.x = 1.0
            move_cmd.angular.z = 5.0
            pub.publish(move_cmd)

        def f_button_pressed():
            global move_cmd
            move_cmd.linear.x = 1.0
            move_cmd.angular.z = 0.0
            pub.publish(move_cmd)

        def fr_button_pressed():
            global move_cmd
            move_cmd.linear.x = 1.0
            move_cmd.angular.z = -5.0
            pub.publish(move_cmd)

        def l_button_pressed():
            global move_cmd
            move_cmd.linear.x = 0.0
            move_cmd.angular.z = 5.0
            pub.publish(move_cmd)

        def stop_button_pressed():
            global move_cmd
            move_cmd.linear.x = 0.0
            move_cmd.angular.z = 0.0
            pub.publish(move_cmd)

        def r_button_pressed():
            global move_cmd
            move_cmd.linear.x = 0.0
            move_cmd.angular.z = -5.0
            pub.publish(move_cmd)

        def bl_button_pressed():
            global move_cmd
            move_cmd.linear.x = -1.0
            move_cmd.angular.z = -5.0
            pub.publish(move_cmd)

        def b_button_pressed():
            global move_cmd
            move_cmd.linear.x = -1.0
            move_cmd.angular.z = 0.0
            pub.publish(move_cmd)

        def br_button_pressed():
            global move_cmd
            move_cmd.linear.x = -1.0
            move_cmd.angular.z = 5.0
            pub.publish(move_cmd)

        def value_changed():
            angle = self.horizontalSlider.value()
            rad = (angle*3.14)/180
            print(rad)
            slidepub.publish(rad)

        Form.setObjectName("Form")
        Form.resize(382, 407)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 381, 341))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.button_f = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_f.setMinimumSize(QtCore.QSize(0, 70))
        self.button_f.setMaximumSize(QtCore.QSize(70, 16777215))
        self.button_f.setObjectName("button_f")
        self.gridLayout.addWidget(self.button_f, 0, 1, 1, 1)
        self.button_fr = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_fr.setMinimumSize(QtCore.QSize(0, 70))
        self.button_fr.setMaximumSize(QtCore.QSize(70, 16777215))
        self.button_fr.setObjectName("button_fr")
        self.gridLayout.addWidget(self.button_fr, 0, 2, 1, 1)
        self.button_fl = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_fl.setMinimumSize(QtCore.QSize(0, 70))
        self.button_fl.setMaximumSize(QtCore.QSize(70, 16777215))
        self.button_fl.setObjectName("button_fl")
        self.gridLayout.addWidget(self.button_fl, 0, 0, 1, 1)
        self.button_br = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_br.setMinimumSize(QtCore.QSize(0, 70))
        self.button_br.setMaximumSize(QtCore.QSize(70, 16777215))
        self.button_br.setObjectName("button_br")
        self.gridLayout.addWidget(self.button_br, 2, 2, 1, 1)
        self.button_bl = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_bl.setMinimumSize(QtCore.QSize(0, 70))
        self.button_bl.setMaximumSize(QtCore.QSize(70, 16777215))
        self.button_bl.setObjectName("button_bl")
        self.gridLayout.addWidget(self.button_bl, 2, 0, 1, 1)
        self.button_b = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_b.setMinimumSize(QtCore.QSize(0, 70))
        self.button_b.setMaximumSize(QtCore.QSize(70, 16777215))
        self.button_b.setObjectName("button_b")
        self.gridLayout.addWidget(self.button_b, 2, 1, 1, 1)
        self.button_r = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_r.setMinimumSize(QtCore.QSize(0, 70))
        self.button_r.setMaximumSize(QtCore.QSize(70, 16777215))
        self.button_r.setObjectName("button_r")
        self.gridLayout.addWidget(self.button_r, 1, 2, 1, 1)
        self.button_l = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_l.setMinimumSize(QtCore.QSize(0, 70))
        self.button_l.setMaximumSize(QtCore.QSize(70, 16777215))
        self.button_l.setObjectName("button_l")
        self.gridLayout.addWidget(self.button_l, 1, 0, 1, 1)
        self.button_stop = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_stop.setMinimumSize(QtCore.QSize(0, 70))
        self.button_stop.setMaximumSize(QtCore.QSize(70, 16777215))
        self.button_stop.setObjectName("button_stop")
        self.gridLayout.addWidget(self.button_stop, 1, 1, 1, 1)
        self.horizontalSlider = QtWidgets.QSlider(Form)
        self.horizontalSlider.setGeometry(QtCore.QRect(70, 370, 227, 15))
        self.horizontalSlider.setMinimum(-25)
        self.horizontalSlider.setMaximum(85)
        self.horizontalSlider.setSliderPosition(0)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 370, 41, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(320, 370, 41, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


        self.button_fl.released.connect(button_released)
        self.button_f.released.connect(button_released)
        self.button_fr.released.connect(button_released)
        self.button_r.released.connect(button_released)
        self.button_stop.released.connect(button_released)
        self.button_l.released.connect(button_released)
        self.button_bl.released.connect(button_released)
        self.button_b.released.connect(button_released)
        self.button_br.released.connect(button_released)

        self.button_fl.pressed.connect(fl_button_pressed)
        self.button_f.pressed.connect(f_button_pressed)
        self.button_fr.pressed.connect(fr_button_pressed)
        self.button_r.pressed.connect(r_button_pressed)
        self.button_stop.pressed.connect(stop_button_pressed)
        self.button_l.pressed.connect(l_button_pressed)
        self.button_bl.pressed.connect(bl_button_pressed)
        self.button_b.pressed.connect(b_button_pressed)
        self.button_br.pressed.connect(br_button_pressed)

        self.horizontalSlider.valueChanged.connect(value_changed)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.button_f.setText(_translate("Form", "F"))
        self.button_fr.setText(_translate("Form", "FR"))
        self.button_fl.setText(_translate("Form", "FL"))
        self.button_br.setText(_translate("Form", "BR"))
        self.button_bl.setText(_translate("Form", "BL"))
        self.button_b.setText(_translate("Form", "B"))
        self.button_r.setText(_translate("Form", "R"))
        self.button_l.setText(_translate("Form", "L"))
        self.button_stop.setText(_translate("Form", "STOP"))
        self.label.setText(_translate("Form", "Close"))
        self.label_2.setText(_translate("Form", "Open"))


if __name__ == "__main__":
    import sys

    rospy.init_node('UI_002')
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
    slidepub = rospy.Publisher('/irckt/motor_finger_right_position_controller/command', Float64, queue_size=1)

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

