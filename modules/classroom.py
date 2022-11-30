# This file will contain GUI structure and content for the initial launch page
# AKA the classroom

import sys
import os
import tkinter as tk
import modules.styles as styles
from PIL import ImageTk, Image


def get_image_path(regular_path, file_name):
	try:
		base_path = sys._MEIPASS + "/pictures/"
	except Exception:
		base_path = regular_path

	return os.path.join(base_path, file_name)


class Classroom:
	"""
	Main GUI where selection of topic and settings is made
	"""
	def __init__(self, window: tk.Tk, version):
		self.window = window
		self.window.title("Renge's Classroom (" + version + ")")
		# self.window.geometry("%dx%d+200+100" % (self.window.winfo_screenwidth(), self.window.winfo_screenheight()))
		self.window.minsize(1000, 800)
		self.window.resizable(False, False)

		# Start setting up the GUI content
		# Structure will consist of 5 frames:
		# Top left: Renge pic + intro
		# Top Right: Subject selection: Katakana, Hiragana, Kanji
		# Bottom Left: Select number of questions to be asked
		# Bottom Right: Difficulty level selection
		# Complete bottom: Control buttons

		# Configure the GUI layout weight
		self.window.rowconfigure([0, 10], weight=2)
		self.window.rowconfigure(20, weight=1)
		self.window.columnconfigure([0, 10], weight=2)

		# Now for the Frame creation and placement:
		self.frame_renge = tk.Frame(self.window, padx=5, pady=5, name="renge")
		self.frame_subject = tk.Frame(self.window, padx=5, pady=5, name="subject")
		self.frame_count = tk.Frame(self.window, padx=5, pady=5, name="count")
		self.frame_difficulty = tk.Frame(self.window, padx=5, pady=5, name="difficulty")
		self.frame_control = tk.Frame(self.window, padx=5, pady=5, name="control")

		self.frame_renge.grid(row=0, column=0, sticky="news", padx=20, pady=20)
		self.frame_subject.grid(row=0, column=10, sticky="news", padx=20, pady=20)
		self.frame_count.grid(row=10, column=0, sticky="news", padx=20, pady=20)
		self.frame_difficulty.grid(row=10, column=10, sticky="news", padx=20, pady=20)
		self.frame_control.grid(row=20, column=0, columnspan=11, sticky="news", padx=20, pady=20)

		# self.frame_renge.config(bg="blue")
		# self.frame_subject.config(bg="red")
		# self.frame_count.config(bg="yellow")
		# self.frame_difficulty.config(bg="green")
		# self.frame_control.config(bg="orange")

		# Set-up the Renge Frame:
		self.frame_renge.grid_propagate(False)
		self.frame_renge.rowconfigure(10, weight=2)
		self.frame_renge.columnconfigure([10, 20], weight=2)

		# Set-up the picture and introduction
		welcome_pic = tk.PhotoImage(file=get_image_path(styles.PIC_RENGE_PATH, "renge_welcome.png"))
		self.renge_welcome = tk.Label(self.frame_renge, image=welcome_pic)
		self.renge_welcome.image = welcome_pic
		self.renge_welcome.grid(row=10, column=10, sticky="ns")

		tk.Label(self.frame_renge, text="Nyanpasu!", font=styles.TITLE_FONT).grid(row=10, column=20, sticky="news")

		# Set-up the Subject
		self.frame_subject.grid_propagate(False)














