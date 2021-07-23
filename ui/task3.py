# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'task3.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):

    def append_text(self,userInput):

        #text = self.le.text()
        self.textBrowser.append(userInput)
        #self.le.clear()

    def clear_text(self):

        self.textBrowser.clear()


    def setupUi(self, Form):

        def t1_pressed():
            self.clear_text()
            text = "<center><h1>Going to T-1</h1></center>"
            self.append_text(text)
            pass

        def t2_pressed():
            self.clear_text()
            text = "<center><h1>Going to T-2</h1></center>"
            self.append_text(text)
            pass


        def t3_pressed():
            self.clear_text()
            text = "<center><h1>Going to T-3</h1></center>"
            self.append_text(text)
            pass


        def t4_pressed():
            self.clear_text()
            text = "<center><h1>Going to T-4</h1></center>"
            self.append_text(text)
            pass


        def t5_pressed():
            self.clear_text()
            text = "<center><h1>Going to T-5</h1></center>"
            self.append_text(text)
            pass


        def stop_pressed():
            self.clear_text()
            text = "<center><h1>Emergency STOP</h1></center>"
            self.append_text(text)
            pass

        def home_pressed():
            self.clear_text()
            text = "<center><h1>Going HOME</h1></center>"
            self.append_text(text)
            pass

        def value_changed():
            linear = self.horizontalSlider.value()
            print(linear)
            pass

        def value_changed_2():
            angular = self.horizontalSlider_2.value()
            print(angular)

            pass



        Form.setObjectName("Form")
        Form.resize(453, 431)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(90, 20, 256, 51))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setAcceptRichText(True)
        self.textBrowser.setOpenExternalLinks(True)
        self.t1 = QtWidgets.QPushButton(Form)
        self.t1.setGeometry(QtCore.QRect(30, 100, 61, 61))
        self.t1.setMinimumSize(QtCore.QSize(60, 60))
        self.t1.setMaximumSize(QtCore.QSize(100, 100))
        self.t1.setObjectName("t1")
        self.t1.setIcon(QtGui.QIcon('../images/1.png'))
        self.t1.setIconSize(QtCore.QSize(60,60))
        self.t2 = QtWidgets.QPushButton(Form)
        self.t2.setGeometry(QtCore.QRect(110, 160, 61, 61))
        self.t2.setObjectName("t2")
        self.t2.setIcon(QtGui.QIcon('../images/2.png'))
        self.t2.setIconSize(QtCore.QSize(60,60))
        self.t3 = QtWidgets.QPushButton(Form)
        self.t3.setGeometry(QtCore.QRect(200, 100, 61, 61))
        self.t3.setMinimumSize(QtCore.QSize(61, 61))
        self.t3.setObjectName("t3")
        self.t3.setIcon(QtGui.QIcon('../images/3.png'))
        self.t3.setIconSize(QtCore.QSize(60,60))
        self.t4 = QtWidgets.QPushButton(Form)
        self.t4.setGeometry(QtCore.QRect(280, 160, 61, 61))
        self.t4.setObjectName("t4")
        self.t4.setIcon(QtGui.QIcon('../images/4.png'))
        self.t4.setIconSize(QtCore.QSize(60,60))
        self.t5 = QtWidgets.QPushButton(Form)
        self.t5.setGeometry(QtCore.QRect(360, 100, 61, 61))
        self.t5.setObjectName("t5")
        self.t5.setIcon(QtGui.QIcon('../images/5.png'))
        self.t5.setIconSize(QtCore.QSize(60,60))
        self.stop = QtWidgets.QPushButton(Form)
        self.stop.setGeometry(QtCore.QRect(70, 250, 111, 51))

        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.stop.setFont(font)
        self.stop.setObjectName("stop")
        self.stop.setIcon(QtGui.QIcon('../images/stop.png'))
        self.stop.setIconSize(QtCore.QSize(50,50))

        self.home = QtWidgets.QPushButton(Form)
        self.home.setGeometry(QtCore.QRect(248, 250, 121, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.home.setFont(font)
        self.home.setObjectName("home")
        self.home.setIcon(QtGui.QIcon('../images/home.png'))
        self.home.setIconSize(QtCore.QSize(50,50))

        self.horizontalSlider = QtWidgets.QSlider(Form)
        self.horizontalSlider.setGeometry(QtCore.QRect(139, 340, 291, 20))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setMinimum(-5)
        self.horizontalSlider.setMaximum(5)
        self.horizontalSlider.setSliderPosition(0)

        self.horizontalSlider_2 = QtWidgets.QSlider(Form)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(140, 370, 291, 20))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalSlider_2.setMinimum(-5)
        self.horizontalSlider_2.setMaximum(5)
        self.horizontalSlider_2.setSliderPosition(0)

        self.linear = QtWidgets.QLabel(Form)
        self.linear.setGeometry(QtCore.QRect(30, 330, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.linear.setFont(font)
        self.linear.setObjectName("linear")

        self.angular = QtWidgets.QLabel(Form)
        self.angular.setGeometry(QtCore.QRect(30, 370, 81, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.angular.setFont(font)
        self.angular.setObjectName("angular")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        #self.t1.released.connect(t1_released)
        self.t1.pressed.connect(t1_pressed)

        #self.t2.released.connect(t1_released)
        self.t2.pressed.connect(t2_pressed)

        #self.t3.released.connect(t1_released)
        self.t3.pressed.connect(t3_pressed)

        #self.t4.released.connect(t1_released)
        self.t4.pressed.connect(t4_pressed)

        #self.t5.released.connect(t1_released)
        self.t5.pressed.connect(t5_pressed)

        #self.stop.released.connect(t1_released)
        self.stop.pressed.connect(stop_pressed)

        #self.home.released.connect(t1_released)
        self.home.pressed.connect(home_pressed)

        self.horizontalSlider.valueChanged.connect(value_changed)
        self.horizontalSlider_2.valueChanged.connect(value_changed_2)



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        # self.t1.setText(_translate("Form", "T1"))
        # self.t2.setText(_translate("Form", "T2"))
        # self.t3.setText(_translate("Form", "T3"))
        # self.t4.setText(_translate("Form", "T4"))
        # self.t5.setText(_translate("Form", "T5"))
        self.stop.setText(_translate("Form", "STOP"))
        self.home.setText(_translate("Form", "HOME"))
        self.linear.setText(_translate("Form", "LINEAR"))
        self.angular.setText(_translate("Form", "ANGULAR"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

