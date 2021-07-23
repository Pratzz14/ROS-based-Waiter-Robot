#!/usr/bin/env python

from PyQt5 import QtCore, QtGui, QtWidgets
import threading
import rospy
from geometry_msgs.msg import Point, Twist
from nav_msgs.msg import Odometry
import math
from tf.transformations import euler_from_quaternion


# Defining Global Variables

# For selected button and linear, angular speed changing
selected_button = ""
linear_speed = 1.0
angular_speed = -1.0

# x,y,theta of the bot
x=0.0
y=0.0
theta=0.0

# linear = 0.0
# angular = 0.0

# To apply twist for the bot
# Making it global because used in many functions
move_cmd = Twist()

# The x,y co-ords of all 5 tables and home
goal1 = Point()
goal1.x = -0.35
goal1.y = 0.0

goal2 = Point()
goal2.x = -0.66
goal2.y = -0.64

goal3 = Point()
goal3.x = 0.33
goal3.y = -0.64

goal4 = Point()
goal4.x = 0.66
goal4.y = 0.015

goal5 = Point()
goal5.x = 0.33
goal5.y = 0.66

goalhome = Point()
goalhome.x = -0.66
goalhome.y = 0.64

# Implementing distance between two points
def get_dist(p1x,p1y,p2x,p2y):
    distance = math.sqrt( ((p1x-p2x)**2)+((p1y-p2y)**2) )
    return distance

# Getting the Odomentry into about the bot
def botOdom(msg):
    global x, y, theta

    x=msg.pose.pose.position.x
    y=msg.pose.pose.position.y

    # Position of bots are defined by a quaternion 4-D stuff 
    # Using euler_from_quaternion() to get euler value, but using only the theta value(yaw)
    ori = msg.pose.pose.orientation
    (roll, pitch, theta) = euler_from_quaternion([ori.x, ori.y, ori.z, ori.w])

# Takes the goal and move the bot towards the goal
# Stop the bot when reached to tables : err < 0.1
def go_to(goal_name):
    global selected_button
    rate = rospy.Rate(10)

    if goal_name == "stopBot":
        bot_stop()

    else:

        inc_x = goal_name.x - x
        inc_y = goal_name.y - y

        # Inverse tan - to calculate the angle
        angle_to_go = math.atan2(inc_y,inc_x)
            
        distance = get_dist(goal_name.x,goal_name.y,x,y)

        # If bot reached the goal : err allowed is 0.1
        # Stop the bot and print appopriate message
        #Else rotate the bot towards the goal and dash ahead
        if distance < 0.1:
            move_cmd.linear.x = 0.0
            move_cmd.angular.z = 0.0
            pub.publish(move_cmd)
            
            #If the bot reached home
            #Else to one of the 5 tables.
            if goal_name ==goalhome:
                text = "Ready for Next Order"
                print(text)
                selected_button = ""
            else:
                selected_button = "home"
                rospy.sleep(2)
                text = "Order Delievered"
                print(text)
                
        else:
            if abs(angle_to_go - theta) > 0.2:
                move_cmd.linear.x = 0.0
                # move_cmd.angular.z = -1.0
                move_cmd.angular.z = angular_speed
            else:
                # move_cmd.linear.x = 1.0
                move_cmd.linear.x = linear_speed
                move_cmd.angular.z = 0.0

        pub.publish(move_cmd)

        rate.sleep()

# Stopping the bot by making linear,angular speed 0
def bot_stop():
    move_cmd.linear.x = 0.0
    move_cmd.angular.z = 0.0
    pub.publish(move_cmd)

# This gives go_to(goal_name) the goal value, acc. to the button pressed.
def move_bot():
    while not rospy.is_shutdown():
        if selected_button!="":

            if selected_button =="t1":
                go_to(goal1)

            elif selected_button =="t2":
                go_to(goal2)

            elif selected_button =="t3":
                go_to(goal3)

            elif selected_button =="t4":
                go_to(goal4)

            elif selected_button =="t5":
                go_to(goal5)

            elif selected_button =="stop":
                bot_stop()

            elif selected_button =="home":
                go_to(goalhome)

    thread_1.join()

# This tread carries out all the function of moving the bot towards the goal
# The goal values is from the global var selected_button
thread_1 = threading.Thread(target=move_bot)
thread_1.start()


#User-Interface of the BOT
class Ui_Form(object):

    def append_text(self,userInput):
        self.textBrowser.append(userInput)

    def clear_text(self):
        self.textBrowser.clear()

    def setupUi(self, Form):

        # To read which button is pressed. Change the textBrowser and var selected_button 
        def t1_pressed():
            global selected_button
            self.clear_text()
            text = "<center><h1>Going to T-1</h1></center>"
            self.append_text(text)
            selected_button = "t1"

        def t2_pressed():
            global selected_button
            self.clear_text()
            text = "<center><h1>Going to T-2</h1></center>"
            self.append_text(text)
            selected_button = "t2"


        def t3_pressed():
            global selected_button
            self.clear_text()
            text = "<center><h1>Going to T-3</h1></center>"
            self.append_text(text)
            selected_button = "t3"


        def t4_pressed():
            global selected_button
            self.clear_text()
            text = "<center><h1>Going to T-4</h1></center>"
            self.append_text(text)
            selected_button = "t4"


        def t5_pressed():
            global selected_button
            self.clear_text()
            text = "<center><h1>Going to T-5</h1></center>"
            self.append_text(text)
            selected_button = "t5"


        def stop_pressed():
            global selected_button
            self.clear_text()
            text = "<center><h1>Emergency STOP</h1></center>"
            self.append_text(text)
            selected_button = "stop"

        def home_pressed():
            global selected_button

            bot_stop()
            self.clear_text()
            text = "<center><h1>Going HOME</h1></center>"
            self.append_text(text)
            selected_button = "home"

        def value_changed():
            global linear_speed
            linear = self.horizontalSlider.value()
            linear_speed = linear
            self.clear_text()
            text = "<center><h1>Linear: "+str(linear)+"</h1></center>"
            self.append_text(text)

        def value_changed_2():
            global angular_speed
            angular = self.horizontalSlider_2.value()
            #print(angular)
            angular_speed = angular
            self.clear_text()
            text = "<center><h1>Angular: "+str(angular_speed)+"</h1></center>"
            self.append_text(text)


        Form.setObjectName("Form")
        Form.resize(453, 431)
        # textBrowser where some commands are displayed
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(90, 20, 256, 51))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setAcceptRichText(True)
        self.textBrowser.setOpenExternalLinks(True)

        #Table number icons 1-5
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

        # Stop and home button
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

        # Slider1 for linear velocity
        self.horizontalSlider = QtWidgets.QSlider(Form)
        self.horizontalSlider.setGeometry(QtCore.QRect(139, 340, 291, 20))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(5)
        self.horizontalSlider.setSliderPosition(1)

        #Slider2 for angular velocity
        self.horizontalSlider_2 = QtWidgets.QSlider(Form)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(140, 370, 291, 20))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalSlider_2.setMinimum(-5)
        self.horizontalSlider_2.setMaximum(5)
        self.horizontalSlider_2.setSliderPosition(-1)

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

        # Functions when buttons are pressed and Sliders are moved 

        self.t1.pressed.connect(t1_pressed)
        self.t2.pressed.connect(t2_pressed)
        self.t3.pressed.connect(t3_pressed)
        self.t4.pressed.connect(t4_pressed)
        self.t5.pressed.connect(t5_pressed)
        self.stop.pressed.connect(stop_pressed)
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

    rospy.init_node('RBLBot_Controller')

    pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
    sub = rospy.Subscriber('/odom', Odometry, botOdom)
    
    # For UI
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

