# ROS-based-Waiter-Robot
ROS + GUI. Control a bot in Gazebo using ROS on a GUI.
<br>
___

Demo video: https://www.youtube.com/watch?v=hUgpeqMP1vE
___

<br>
Bot link: <br>
RigBetel Labs LLP: https://github.com/rigbetellabs <br>
RBLbot: https://github.com/rigbetellabs/rblbot_description <br>

___

In this project, I have demonstrated ROS with the Graphical User Interface (GUI) to control the bot easily. I have all the required features, it can go to all the 5 tables and the chef's kitchen, i.e. Home. I also have a stop button, to stop the bot at any time. The user can also change the linear and angular speed of the bot, but increasing linear speed gives a small error within the limit of 0.1 meters. The most difficult problem was to stop the bot, in the middle of its path to a table. This concurrency between Gazebo's output and the user's GUI input got easier with ROS when I recognized the correct way.

