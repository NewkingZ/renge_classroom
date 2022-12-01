# This page contains hiragana specific handling
# This includes the required keyboards, generating questions, etc...

import tkinter as tk
import simplejson as json
import modules.styles as styles


class HiraganaKeyboard(tk.Frame):
	def __init__(self, root, on_press):
		super().__init__(root)
		self.on_press = on_press

		self.propagate(False)
		self.rowconfigure([0, 90], weight=1)
		self.columnconfigure([0, 90], weight=1)

		with open("./assets/character_keys/hiragana.json", "r", encoding='utf8') as f:
			hiragana = json.load(f)

		# Now the hard part: Translate all the Hiragana characters to buttons

		for i in range(0, 6):
			for j in range(0, 21):
				tk.Button(self, text=hiragana[0]["kana"], font=styles.KEYBOARD_FONT, command=None).\
					grid(row=i + 1, column=j + 1, padx=5, pady=5)

