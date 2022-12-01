# File contains different definitions for GUI characteristics to maintain a consistent feel across the interface
import os
import sys


def get_image_path(regular_path, file_name):
	try:
		base_path = sys._MEIPASS + "/pictures/"
	except Exception:
		base_path = regular_path

	return os.path.join(base_path, file_name)


PIC_RENGE_PATH = './assets/renge_pics/'


TITLE_FONT = ("calibri", 20)
SUBTITLE_FONT = ("calibri", 15)
KEYBOARD_FONT = ("calibri", 15)
