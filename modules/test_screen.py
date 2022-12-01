# This is the screen that's used for testing the user
import tkinter as tk
import modules.styles as styles

SUBJECT_HIRAGANA = 1
SUBJECT_KATAKANA = 2
SUBJECT_KANJI = 3

DIFFICULTY_BEGINNER = 1
DIFFICULTY_EASY = 1
DIFFICULTY_REGULAR = 1
DIFFICULTY_HARD = 1
DIFFICULTY_EXTREME = 1

RENGE_MOOD_PICS = [["renge_dying_inside.png", 1],
				   ["renge_disgusted.png", 1],
				   ["renge_regular.png", 1],
				   ["renge_intrigued.png", 1],
				   ["renge_cheerful.png", 1]]


def subject_from_int(subject):
	if subject == SUBJECT_HIRAGANA:
		return "Hiragana"
	elif subject == SUBJECT_KATAKANA:
		return "Katakana"
	elif subject == SUBJECT_KANJI:
		return "Kanji"
	else:
		return "Unknown"


class TestScreen(tk.Toplevel):
	def __init__(self, subject, question_count, difficulty, on_complete):
		tk.Toplevel.__init__(self)
		self.subject = subject
		self.total_questions = question_count
		self.difficulty = difficulty
		self.questions_completed = 0
		self.current_mood = 2
		self.on_complete = on_complete

		self.title("Testing " + str(self.total_questions) + " of " + subject_from_int(self.subject) + " at difficulty "
				   + str(self.difficulty))
		self.attributes("-fullscreen", True)

		# This screen will consist of 4 areas each stacked on top of each other
		# Top: Renge picture
		# Second highest: Questions asked
		# Third: Keyboard with characters
		# Fourth: control buttons

		# Configure the GUI layout weight
		self.rowconfigure([10, 20, 30], weight=1)
		self.columnconfigure(10, weight=2)

		# Now for the Frame creation and placement:
		self.frame_renge = tk.Frame(self, padx=5, pady=5, name="renge")
		self.frame_question = tk.Frame(self, padx=5, pady=5, name="question")
		self.frame_keyboard = tk.Frame(self, padx=5, pady=5, name="keyboard")
		self.frame_control = tk.Frame(self, padx=5, pady=5, name="control")

		self.frame_renge.grid(row=10, column=10, sticky="news", padx=20, pady=20)
		self.frame_question.grid(row=20, column=10, sticky="news", padx=20, pady=20)
		self.frame_keyboard.grid(row=30, column=10, sticky="news", padx=20, pady=20)
		self.frame_control.grid(row=40, column=10, sticky="news", padx=20, pady=20)

		# Configure the renge frame
		self.frame_renge.grid_propagate(False)
		self.frame_renge.columnconfigure(10, weight=1)
		self.frame_renge.rowconfigure(10, weight=1)

		# Set-up the picture and introduction
		welcome_pic = tk.PhotoImage(file=styles.get_image_path(styles.PIC_RENGE_PATH,
															   RENGE_MOOD_PICS[self.current_mood][0])).subsample(2)
		self.renge_welcome = tk.Label(self.frame_renge, image=welcome_pic)
		self.renge_welcome.image = welcome_pic
		self.renge_welcome.grid(row=10, column=10, sticky="news")

		# Configure the question frame

		# Configure the keyboard frame

		# Configure the control frame
		self.frame_control.columnconfigure([10, 90], weight=1)

		self.report_card_button = tk.Button(self.frame_control, text="Exit", width=20, height=3,
											command=lambda: self.destroy())
		self.report_card_button.grid(row=10, column=10, sticky="sw", padx=10, pady=10)

	def renge_change_mood(self, new_mood):
		if new_mood == self.current_mood:
			print("new mood is the same as the current mood")
			return
		print("Set new mood to " + new_mood)




