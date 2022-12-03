# This contains the class for the custom tk toplevel screen for test results

import tkinter as tk
import modules.styles as styles

# Picture path along with subsample modifier (TBI)
RENGE_MOOD_PICS = {'F': ["renge_dying_inside.png", 2],
				   'D': ["renge_disappointed.png", 1],
				   'C': ["renge_disgusted.png", 2],
				   'B': ["renge_regular.png", 2],
				   'A': ["renge_intrigued.png", 2],
				   'S': ["renge_cheerful.png", 1]}


def calculate_score(total_answers, correct_answers, average_time):
	# Get a multiplier based on the avg time
	if average_time < 1:
		multiplier = 2
	elif 1 <= average_time < 2.5:
		multiplier = 1.5
	elif 2.5 <= average_time < 5:
		multiplier = 1
	elif 5 <= average_time < 10:
		multiplier = 0.75
	elif 10 <= average_time < 30:
		multiplier = 0.5
	else:
		multiplier = 0.3

	score = correct_answers / total_answers * multiplier * 100

	if score == 200:
		return 'S'
	elif score > 90:
		return 'A'
	elif score > 60:
		return 'B'
	elif score > 40:
		return 'C'
	elif score > 20:
		return 'D'
	else:
		return 'F'


class TestResults(tk.Toplevel):
	def __init__(self, subject, difficulty, total_answers, correct_answers, average_time):
		tk.Toplevel.__init__(self)
		self.title("Test Score! [Subject: " + str(subject) + " level " + str(difficulty) + "]")

		self.score = calculate_score(total_answers, correct_answers, average_time)

		# Screen will have three frames:
		# Left: Renge reaction face to result
		# Right: Metrics results and letter grade

		self.minsize(800, 450)
		self.resizable(False, False)
		self.rowconfigure(10, weight=1)
		self.columnconfigure([10, 20], weight=1)

		self.frame_renge = tk.Frame(self)
		self.frame_metrics = tk.Frame(self)

		self.frame_renge.grid(row=10, column=20, sticky="news", padx=5, pady=5)
		self.frame_metrics.grid(row=10, column=10, sticky="news", padx=5, pady=5)

		# Configure Renge frame
		self.frame_renge.rowconfigure(10, weight=1)
		self.frame_renge.columnconfigure(10, weight=1)
		self.frame_renge.grid_propagate(False)

		renge_face = tk.PhotoImage(file=styles.get_image_path(styles.PIC_RENGE_PATH, RENGE_MOOD_PICS[self.score][0])).\
			subsample(RENGE_MOOD_PICS[self.score][1])
		self.renge_face = tk.Label(self.frame_renge, image=renge_face)
		self.renge_face.image = renge_face
		self.renge_face.grid(row=10, column=10, sticky="news", padx=10)

		# Configure Metrics frame
		self.frame_metrics.rowconfigure([0, 90], weight=1)
		self.frame_metrics.columnconfigure(10, weight=1)
		self.frame_metrics.grid_propagate(False)

		tk.Label(self.frame_metrics, text=subject + " level " + str(difficulty) + " test results!",
				 font=styles.FONT_TITLE).grid(row=10, column=10, sticky="nw", padx=5, pady=5)
		tk.Label(self.frame_metrics, text="Correct Answers: " + str(correct_answers) + "/" + str(total_answers),
				 font=styles.FONT_SUBTITLE).grid(row=11, column=10, sticky="nw", padx=5, pady=5)
		tk.Label(self.frame_metrics, text="Average Time per Question: " + str(average_time),
				 font=styles.FONT_SUBTITLE).grid(row=12, column=10, sticky="nw", padx=5, pady=5)

		tk.Label(self.frame_metrics, text="Final Grade: ",
				 font=styles.FONT_SUBTITLE).grid(row=13, column=10, sticky="nw", padx=10, pady=[10, 0])

		if self.score == 'S':
			grade_color = 'gold'
		elif self.score == 'A':
			grade_color = 'green'
		elif self.score == 'B':
			grade_color = 'blue'
		elif self.score == 'C':
			grade_color = 'slate blue'
		elif self.score == 'D':
			grade_color = 'orange'
		else:
			grade_color = 'red'

		tk.Label(self.frame_metrics, text=self.score, fg=grade_color,
				 font=styles.FONT_FINAL_GRADE).grid(row=14, column=10, sticky="new")


