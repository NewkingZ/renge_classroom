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
		self.frame_renge.rowconfigure([10, 20], weight=2)
		self.frame_renge.columnconfigure([10, 20], weight=2)

		# Set-up the picture and introduction
		welcome_pic = tk.PhotoImage(file=get_image_path(styles.PIC_RENGE_PATH, "renge_welcome.png"))
		self.renge_welcome = tk.Label(self.frame_renge, image=welcome_pic)
		self.renge_welcome.image = welcome_pic
		self.renge_welcome.grid(row=10, column=10, rowspan=11, sticky="ns")

		tk.Label(self.frame_renge, text="Nyanpasu!", font=styles.TITLE_FONT).grid(row=10, column=20, sticky="news")
		tk.Label(self.frame_renge, text="Time to learn some\nJapanese Mutha Fucka").\
			grid(row=20, column=20, sticky="new")

		# Set-up the Subject Frame
		self.frame_subject.grid_propagate(False)
		self.frame_subject.rowconfigure([10, 90], weight=2)
		self.frame_subject.rowconfigure([20, 30, 40], weight=1)
		self.frame_subject.columnconfigure([10, 20, 30], weight=2)

		# Set-up the title and options
		tk.Label(self.frame_subject, text="Select subject to test!", font=styles.SUBTITLE_FONT).\
			grid(row=10, column=10, columnspan=11, sticky="news")

		self.subject_var = tk.IntVar()
		self.subject_options_hiragana = tk.Radiobutton(self.frame_subject, text="Hiragana", variable=self.subject_var,
													   value=1)
		self.subject_options_hiragana.grid(row=20, column=20, sticky="nws")
		self.subject_options_katakana = tk.Radiobutton(self.frame_subject, text="Katakana", variable=self.subject_var,
													   value=2)
		self.subject_options_katakana.grid(row=30, column=20, sticky="nws")
		self.subject_options_kanji = tk.Radiobutton(self.frame_subject, text="Kanji", variable=self.subject_var,
													   value=3)
		self.subject_options_kanji.grid(row=40, column=20, sticky="nws")

		# Set-up the count frame
		self.frame_count.grid_propagate(False)
		self.frame_count.rowconfigure([10, 90], weight=2)
		self.frame_count.rowconfigure([20, 30, 40, 50], weight=1)
		self.frame_count.columnconfigure([10, 20, 30], weight=2)

		# Create and add number of questions options
		tk.Label(self.frame_count, text="Select number of questions", font=styles.SUBTITLE_FONT).\
			grid(row=10, column=10, columnspan=11, sticky="news")

		self.count_var = tk.IntVar()
		self.count_options_10 = tk.Radiobutton(self.frame_count, text="10", variable=self.count_var,
													   value=1)
		self.count_options_10.grid(row=20, column=20, sticky="nws")

		self.count_options_25 = tk.Radiobutton(self.frame_count, text="25", variable=self.count_var,
													   value=2)
		self.count_options_25.grid(row=30, column=20, sticky="nws")

		self.count_options_50 = tk.Radiobutton(self.frame_count, text="50", variable=self.count_var,
													   value=3)
		self.count_options_50.grid(row=40, column=20, sticky="nws")

		self.count_options_100 = tk.Radiobutton(self.frame_count, text="100", variable=self.count_var,
													   value=4)
		self.count_options_100.grid(row=50, column=20, sticky="nws")



















