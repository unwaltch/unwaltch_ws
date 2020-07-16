#!/usr/bin/env python

from datetime import datetime
import os
import stat
import subprocess as sp
import rospy
import rosbag
from std_msgs.msg import *

def Internet_On():
	command="ping -c 1 google.com"
	check = sp.call(command.split(),stdout=None) is 0;
	if check is True:
		print("Internet is connected !")
		return True
	else:
		print("Internet is not connected !")
		return False

def SSD_On():
	try:
		mode = os.stat("/dev/sda2").st_mode		
		stat.S_ISBLK(mode)
		print("SSD is okay !")
		return True
	except:
		print("SSD is not connected !")
		return False

def Record_To_Bag(bag):
	while not rospy.is_shutdown():
		bag.write([],[],raw=False)
	bag.close()

if __name__ == "__main__":
	
	dir_Name = datetime.now().strftime("%d.%B.%Y")
	try:
		os.mkdir(dir_Name)
		os.chdir(dir_Name)
	except:
		os.chdir(dir_Name)
		print("The folder already exists !")
		print("Current Folder: " + os.getcwd())
	
	if Internet_On()==True and SSD_On()==True:
		print("Bag has been created !")
		bag = rosbag.Bag(str(datetime.now().strftime("%H-%M")),'w')
	
	

	'''Record_To_Bag(bag)'''
	






