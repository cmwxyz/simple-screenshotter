import pyautogui
import os
import re
from pathlib import Path


my_screenshot = pyautogui.screenshot()

download_path = os.path.abspath(r'C:\Users\YOURUSERNAMEHERE\Desktop')

my_filename_pre = "screenshot-"
my_filename_num = 1
my_filename_suf = ".png"

my_filename = my_filename_pre + str(my_filename_num) + my_filename_suf
	

pattern = re.compile("^screenshot-(\d+)\.png$")


for filename in os.listdir(download_path):
	print("checking:" + filename)
	result = pattern.search(filename)	
	if result == None:
		print("result was none")
		continue
	print('regex match:' + filename)
	if int(result.group(1)) == my_filename_num:
		my_filename_num += 1
	my_filename = my_filename_pre + str(my_filename_num) + my_filename_suf

print('creating:' + my_filename)


my_screenshot.save(Path(download_path) / Path(my_filename))


