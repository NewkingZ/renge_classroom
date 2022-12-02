# This page contains hiragana specific handling
# This includes the required keyboards, generating questions, etc...

import tkinter as tk
import simplejson as json
import modules.styles as styles


class HiraganaSetup(tk.Frame):
	def __init__(self, root, difficulty, on_press):
		super().__init__(root)

		self.difficulty = difficulty
		self.on_press = on_press

		# Set-up Hiragana question space
		self.grid_propagate(False)
		self.rowconfigure(10, weight=1)
		self.rowconfigure(20, weight=2)
		self.columnconfigure(10, weight=1)

		# Create relevant frames
		self.frame_question = tk.Frame(self)
		self.frame_keyboard = tk.Frame(self)

		# Place them in the Hiragana frame
		self.frame_question.grid(row=10, column=10, sticky='news')
		self.frame_keyboard.grid(row=20, column=10, sticky='news')

		# Configure the question frame
		self.frame_question.grid_propagate(False)
		self.frame_question.rowconfigure([0, 90], weight=1)
		self.frame_question.columnconfigure([0, 90], weight=1)

		tk.Label(self.frame_question, text="Select the symbol associated with:", font=styles.FONT_TITLE).\
			grid(row=10, column=10)
		self.question_var = tk.StringVar(value="-")
		tk.Label(self.frame_question, textvariable=self.question_var, font=styles.FONT_QUESTION).grid(row=20, column=10)

		# Configure Keyboard
		self.frame_keyboard.grid_propagate(False)
		self.frame_keyboard.rowconfigure([0, 90], weight=1)
		self.frame_keyboard.columnconfigure([0, 90], weight=1)

		with open("./assets/character_keys/hiragana.json", "r", encoding='utf-8') as f:
			hiragana = json.load(f)

		# Now the hard part: Translate all the Hiragana characters to buttons

		key_index = 0
		for j in range(0, 22):
			for i in range(0, 6):
				if j == 11:
					padv=50
				else:
					padv=5

				# Basic hiragana only spans 5:
				if j < 11 and i == 5:
					continue

				# Remove ye yi indices
				if j == 7 and (i == 1 or i == 3):
					continue

				# Remove Wi, Wu, and We indices
				if j == 9 and (1 <= i <= 3):
					continue

				# only n in n column
				if j == 10 and i != 0:
					continue

				# Remove yo sound for first 5 additional sounds
				if 11 <= j <= 15 and i == 5:
					continue

				if key_index > len(hiragana):
					continue

				if difficulty < 4 and j >= 11:
					state = tk.DISABLED
				else:
					state = tk.NORMAL

				tk.Button(self.frame_keyboard, text=hiragana[key_index]["kana"], font=styles.FONT_KEYBOARD,
						  command=lambda: self.on_press(False), state=state).grid(row=i + 1, column=j + 1, padx=[padv, 5], pady=5)

				key_index += 1

		tk.Button(self.frame_keyboard, text=hiragana[key_index]["kana"], font=styles.FONT_KEYBOARD,
				  command=lambda: self.on_press(True)).grid(row=6, column=1, columnspan=2, padx=5, pady=5, sticky="ew")

