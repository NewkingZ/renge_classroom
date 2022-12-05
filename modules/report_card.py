# This screen shows the current high scores achieved by the user

import os
import tkinter as tk
import modules.statistics as statistics
import modules.styles as styles

DIFFICULTY_NAMES = ["Beginner", "Easy", "Regular", "Hard", "Extreme"]


class ReportCard(tk.Toplevel):
	def __init__(self):
		tk.Toplevel.__init__(self)

		# Configure the window first:
		self.minsize(1000, 600)
		self.title("My test results!")
		self.resizable(False, False)
		self.rowconfigure(10, weight=1)
		self.rowconfigure([20, 30], weight=3)
		self.columnconfigure([10, 20, 30], weight=1)

		# Top frame: Title and instructions line
		# Frames in the middle for each subject
		# Frame in the bottom right for a renge pic
		self.frame_title = tk.Frame(self)
		self.frame_hiragana = tk.Frame(self)
		self.frame_katakana = tk.Frame(self)
		self.frame_kanji = tk.Frame(self)
		self.frame_renge = tk.Frame(self)

		# Place the frames in the screen
		self.frame_title.grid(row=10, column=10, columnspan=31, sticky="news", padx=5, pady=5)
		self.frame_hiragana.grid(row=20, column=10, sticky="news", padx=25, pady=5)
		self.frame_katakana.grid(row=20, column=20, sticky="news", padx=25, pady=5)
		self.frame_kanji.grid(row=20, column=30, sticky="news", padx=25, pady=5)
		self.frame_renge.grid(row=30, column=30, sticky="news", padx=5, pady=5)

		# Set-up title frame
		self.frame_title.columnconfigure(10, weight=1)
		self.grid_propagate(False)
		tk.Label(self.frame_title, text="Report Card", font=styles.FONT_TITLE).grid(row=10, column=10, sticky='ew')
		tk.Label(self.frame_title, text="A test must have a minimum of 50 questions to be saved on the report card",
				 font=styles.FONT_SUBTITLE).grid(row=20, column=10, sticky='ew')

		self.scores = statistics.get_score_data()

		# Set-up Hiragana frame
		self.frame_hiragana.grid_propagate(False)
		self.frame_hiragana.rowconfigure(90, weight=1)
		self.frame_hiragana.columnconfigure([10, 20, 30, 40], weight=1)

		# Create and place elements is said frame
		tk.Label(self.frame_hiragana, text="Hiragana", font=styles.FONT_SUBTITLE).grid(row=10, column=10, columnspan=31,
																					   sticky='new', padx=5, pady=5)
		tk.Label(self.frame_hiragana, text="Difficulty").grid(row=20, column=10, sticky='new', padx=5, pady=5)
		tk.Label(self.frame_hiragana, text="Avg time").grid(row=20, column=20, sticky='new', padx=5, pady=5)
		tk.Label(self.frame_hiragana, text="Score").grid(row=20, column=30, sticky='new', padx=5, pady=5)
		tk.Label(self.frame_hiragana, text="Grade").grid(row=20, column=40, sticky='new', padx=5, pady=5)

		for difficulty in self.scores[styles.SUBJECT_HIRAGANA]:
			index = int(difficulty[-1])
			tk.Label(self.frame_hiragana, text=DIFFICULTY_NAMES[index - 1]).grid(row=20 + index * 10, column=10,
																			 sticky='new', padx=5, pady=5)
			tk.Label(self.frame_hiragana, text=str(self.scores[styles.SUBJECT_HIRAGANA][difficulty]["avg_time"])).\
				grid(row=20 + index * 10, column=20, sticky='new', padx=5, pady=5)
			tk.Label(self.frame_hiragana, text=str(self.scores[styles.SUBJECT_HIRAGANA][difficulty]["correct_answers"])
					+ "/" + str(self.scores[styles.SUBJECT_HIRAGANA][difficulty]["total_questions"])).\
				grid(row=20 + index * 10, column=30, sticky='new', padx=5, pady=5)
			tk.Label(self.frame_hiragana, text=str(self.scores[styles.SUBJECT_HIRAGANA][difficulty]["letter_grade"])).\
				grid(row=20 + index * 10, column=40, sticky='new', padx=5, pady=5)

		# Set-up Katakana frame
		self.frame_katakana.grid_propagate(False)
		self.frame_katakana.rowconfigure(90, weight=1)
		self.frame_katakana.columnconfigure([10, 20, 30, 40], weight=1)

		# Create and place elements is said frame
		tk.Label(self.frame_katakana, text="Katakana", font=styles.FONT_SUBTITLE).grid(row=10, column=10, columnspan=31,
																					   sticky='new', padx=5, pady=5)
		tk.Label(self.frame_katakana, text="Difficulty").grid(row=20, column=10, sticky='new', padx=5, pady=5)
		tk.Label(self.frame_katakana, text="Avg time").grid(row=20, column=20, sticky='new', padx=5, pady=5)
		tk.Label(self.frame_katakana, text="Score").grid(row=20, column=30, sticky='new', padx=5, pady=5)
		tk.Label(self.frame_katakana, text="Grade").grid(row=20, column=40, sticky='new', padx=5, pady=5)

		for difficulty in self.scores[styles.SUBJECT_KATAKANA]:
			index = int(difficulty[-1])
			tk.Label(self.frame_katakana, text=DIFFICULTY_NAMES[index - 1]).grid(row=20 + index * 10, column=10,
																			 sticky='new', padx=5, pady=5)
			tk.Label(self.frame_katakana, text=str(self.scores[styles.SUBJECT_KATAKANA][difficulty]["avg_time"])).\
				grid(row=20 + index * 10, column=20, sticky='new', padx=5, pady=5)
			tk.Label(self.frame_katakana, text=str(self.scores[styles.SUBJECT_KATAKANA][difficulty]["correct_answers"])
					+ "/" + str(self.scores[styles.SUBJECT_KATAKANA][difficulty]["total_questions"])).\
				grid(row=20 + index * 10, column=30, sticky='new', padx=5, pady=5)
			tk.Label(self.frame_katakana, text=str(self.scores[styles.SUBJECT_KATAKANA][difficulty]["letter_grade"])).\
				grid(row=20 + index * 10, column=40, sticky='new', padx=5, pady=5)

		# Set-up Kanji frame
		self.frame_kanji.grid_propagate(False)
		self.frame_kanji.rowconfigure(90, weight=1)
		self.frame_kanji.columnconfigure([10, 20, 30, 40], weight=1)

		# Create and place elements is said frame
		tk.Label(self.frame_kanji, text="Katakana", font=styles.FONT_SUBTITLE).grid(row=10, column=10, columnspan=31,
																					   sticky='new', padx=5, pady=5)
		tk.Label(self.frame_kanji, text="Difficulty").grid(row=20, column=10, sticky='new', padx=5, pady=5)
		tk.Label(self.frame_kanji, text="Avg time").grid(row=20, column=20, sticky='new', padx=5, pady=5)
		tk.Label(self.frame_kanji, text="Score").grid(row=20, column=30, sticky='new', padx=5, pady=5)
		tk.Label(self.frame_kanji, text="Grade").grid(row=20, column=40, sticky='new', padx=5, pady=5)

		for difficulty in self.scores[styles.SUBJECT_KANJI]:
			index = int(difficulty[-1])
			tk.Label(self.frame_kanji, text=DIFFICULTY_NAMES[index - 1]).grid(row=20 + index * 10, column=10,
																			 sticky='new', padx=5, pady=5)
			tk.Label(self.frame_kanji, text=str(self.scores[styles.SUBJECT_KANJI][difficulty]["avg_time"])).\
				grid(row=20 + index * 10, column=20, sticky='new', padx=5, pady=5)
			tk.Label(self.frame_kanji, text=str(self.scores[styles.SUBJECT_KANJI][difficulty]["correct_answers"])
					+ "/" + str(self.scores[styles.SUBJECT_KANJI][difficulty]["total_questions"])).\
				grid(row=20 + index * 10, column=30, sticky='new', padx=5, pady=5)
			tk.Label(self.frame_kanji, text=str(self.scores[styles.SUBJECT_KANJI][difficulty]["letter_grade"])).\
				grid(row=20 + index * 10, column=40, sticky='new', padx=5, pady=5)





