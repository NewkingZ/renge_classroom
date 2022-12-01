# This file will contain GUI structure and content for the initial launch page
# AKA the classroom

import tkinter as tk
import modules.styles as styles
from PIL import ImageTk, Image
import modules.test_screen as test_screen


def do_nothing():
	print("Nyanpasu!")


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
		# Structure will consist of 3 frames:
		# Left Frame: Teacher Renge
		# Right Frame: Option Selection
		# Bottom Frame: Control settings

		# Configure the GUI layout weight
		self.window.rowconfigure(10, weight=1)
		self.window.columnconfigure([10, 20], weight=2)

		# Now for the Frame creation and placement:
		self.frame_renge = tk.Frame(self.window, padx=5, pady=5, name="renge")
		self.frame_settings = tk.Frame(self.window, padx=5, pady=5, name="settings")
		self.frame_control = tk.Frame(self.window, padx=5, pady=5, name="control")

		self.frame_renge.grid(row=10, column=10, sticky="news", padx=20, pady=20)
		self.frame_settings.grid(row=10, column=20, sticky="news", padx=20, pady=20)
		self.frame_control.grid(row=20, column=10, columnspan=11, sticky="news", padx=20, pady=20)

		# Set-up the Renge Frame:
		self.frame_renge.grid_propagate(False)
		self.frame_renge.columnconfigure(10, weight=2)
		self.frame_renge.rowconfigure(10, weight=5)
		self.frame_renge.rowconfigure([20, 30], weight=1)

		# Set-up the picture and introduction
		welcome_pic = tk.PhotoImage(file=styles.get_image_path(styles.PIC_RENGE_PATH, "renge_welcome.png")).subsample(3)
		self.renge_welcome = tk.Label(self.frame_renge, image=welcome_pic)
		self.renge_welcome.image = welcome_pic
		self.renge_welcome.grid(row=10, column=10, sticky="news")

		tk.Label(self.frame_renge, text="Nyanpasu!", font=styles.TITLE_FONT).grid(row=20, column=10, sticky="news")
		tk.Label(self.frame_renge, text="Ready to practice some Japanese?", font=styles.SUBTITLE_FONT).\
			grid(row=30, column=10, sticky="news")

		# Set-up the control frame along with its buttons
		self.frame_control.columnconfigure([10, 90], weight=1)

		self.confirm_button = tk.Button(self.frame_control, text="Let's Go!", width=20,
										command=self.launch_testing_screen)
		self.confirm_button.grid(row=10, column=90, sticky="se", padx=10, pady=10)

		self.report_card_button = tk.Button(self.frame_control, text="Report Card", width=20, command=do_nothing)
		self.report_card_button.grid(row=10, column=10, sticky="sw", padx=10, pady=10)

		# Set-up the settings frame
		self.frame_settings.grid_propagate(False)
		self.frame_renge.columnconfigure(10, weight=1)
		self.frame_renge.rowconfigure([10, 20, 30, 40], weight=1)

		# Make a sub frame for each setting available
		self.settings_subject = tk.Frame(self.frame_settings)
		self.settings_count = tk.Frame(self.frame_settings)
		self.settings_difficulty = tk.Frame(self.frame_settings)

		self.settings_subject.grid(row=10, column=10, sticky="news", pady=10)
		self.settings_count.grid(row=20, column=10, sticky="news", pady=10)
		self.settings_difficulty.grid(row=30, column=10, sticky="news", pady=10)

		# Set up the subject frame
		self.settings_subject.rowconfigure(90, weight=1)
		self.settings_subject.columnconfigure(10, weight=1)

		tk.Label(self.settings_subject, text="Select subject:", font=styles.SUBTITLE_FONT)\
			.grid(row=10, column=10, sticky="w")
		self.subject_var = tk.IntVar(value=1)
		tk.Radiobutton(self.settings_subject, text="Hiragana", variable=self.subject_var, value=1)\
			.grid(row=20, column=10, sticky='w')
		tk.Radiobutton(self.settings_subject, text="Katakana", variable=self.subject_var, value=2)\
			.grid(row=30, column=10, sticky='w')
		tk.Radiobutton(self.settings_subject, text="Kanji", variable=self.subject_var, value=3)\
			.grid(row=40, column=10, sticky='w')

		# Set up the question count frame
		self.settings_count.rowconfigure(90, weight=1)
		self.settings_count.columnconfigure(10, weight=1)

		tk.Label(self.settings_count, text="Select number of test questions:", font=styles.SUBTITLE_FONT)\
			.grid(row=10, column=10, sticky="w")
		self.count_var = tk.IntVar(value="10")
		tk.Radiobutton(self.settings_count, text="10", variable=self.count_var, value=10)\
			.grid(row=20, column=10, sticky='w')
		tk.Radiobutton(self.settings_count, text="25", variable=self.count_var, value=25)\
			.grid(row=30, column=10, sticky='w')
		tk.Radiobutton(self.settings_count, text="50", variable=self.count_var, value=50)\
			.grid(row=40, column=10, sticky='w')
		tk.Radiobutton(self.settings_count, text="100", variable=self.count_var, value=100)\
			.grid(row=50, column=10, sticky='w')

		tk.Label(self.settings_difficulty, text="Select question difficulty:", font=styles.SUBTITLE_FONT)\
			.grid(row=10, column=10, sticky="w")
		self.difficulty_var = tk.IntVar(value=3)
		tk.Radiobutton(self.settings_difficulty, text="Beginner", variable=self.difficulty_var, value=1)\
			.grid(row=20, column=10, sticky='w')
		tk.Radiobutton(self.settings_difficulty, text="Easy", variable=self.difficulty_var, value=2)\
			.grid(row=30, column=10, sticky='w')
		tk.Radiobutton(self.settings_difficulty, text="Regular", variable=self.difficulty_var, value=3)\
			.grid(row=40, column=10, sticky='w')
		tk.Radiobutton(self.settings_difficulty, text="Hard", variable=self.difficulty_var, value=4)\
			.grid(row=50, column=10, sticky='w')
		tk.Radiobutton(self.settings_difficulty, text="私を破壊する", variable=self.difficulty_var, value=5)\
			.grid(row=60, column=10, sticky='w')

		# Disable some settings while tool is in development
		# Disable Subject for now (Hard set on Hiragana)
		for child in self.settings_subject.winfo_children():
			if child.winfo_class() == 'Frame':
				for grand_child in child.winfo_children():
					grand_child.config(state=tk.NORMAL)
			elif child.winfo_class() == 'TSeparator':
				pass
			else:
				child.config(state=tk.DISABLED)

		# Disable Difficulty for now (Hard set on regular
		for child in self.settings_difficulty.winfo_children():
			if child.winfo_class() == 'Frame':
				for grand_child in child.winfo_children():
					grand_child.config(state=tk.NORMAL)
			elif child.winfo_class() == 'TSeparator':
				pass
			else:
				child.config(state=tk.DISABLED)

		self.report_card_button.config(state=tk.DISABLED)

	def launch_testing_screen(self):
		test = test_screen.TestScreen(self.subject_var.get(), self.count_var.get(), self.difficulty_var.get(),
									  do_nothing)
		test.grab_set()
