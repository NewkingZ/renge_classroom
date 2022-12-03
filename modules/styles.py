# File contains different definitions for GUI characteristics to maintain a consistent feel across the interface
import os
import sys


def get_image_path(regular_path, file_name):
	try:
		base_path = sys._MEIPASS + "/pictures/"
	except Exception:
		base_path = regular_path

	return os.path.join(base_path, file_name)


def get_char_set(regular_path, file_name):
	try:
		base_path = sys._MEIPASS + "/character_sets/"
	except Exception:
		base_path = regular_path

	return os.path.join(base_path, file_name)


PIC_RENGE_PATH = './assets/renge_pics/'


FONT_TITLE = ("calibri", 20)
FONT_SUBTITLE = ("calibri", 15)
FONT_KEYBOARD = ("calibri", 20)
FONT_QUESTION = ("calibri", 50)
FONT_FINAL_GRADE = ("calibri", 125)
