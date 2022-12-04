# This file is meant to access and manage access to previous statistics

import cryptography.fernet as fernet
import os
import os.path
import json
import modules.styles as styles

PATH_STATISTICS = "./statistics/"
HIGH_SCORES = "high_scores.json"
SCORE_KEY = "score.key"


def letter_grade_score(grade):
	if 's' in grade.lower():
		return 5
	if 'a' in grade.lower():
		return 4
	if 'b' in grade.lower():
		return 3
	if 'c' in grade.lower():
		return 2
	if 'd' in grade.lower():
		return 1
	else:
		return 0


def init_stats():
	# Check to see if this is a new launch
	if not os.path.exists(PATH_STATISTICS):
		# Set-up path, create json and key files
		os.mkdir(PATH_STATISTICS)
		key = fernet.Fernet.generate_key()
		with open(PATH_STATISTICS + '/score.key', 'wb') as f:
			f.write(key)

		empty_data = dict()
		for subject in [styles.SUBJECT_HIRAGANA, styles.SUBJECT_HIRAGANA, styles.SUBJECT_HIRAGANA]:
			empty_data[subject] = dict()
			for difficulty in range(1, 5):
				empty_data[subject]["difficulty_" + str(difficulty)] = dict()
				empty_data[subject]["difficulty_" + str(difficulty)]["avg_time"] = None
				empty_data[subject]["difficulty_" + str(difficulty)]["total_questions"] = None
				empty_data[subject]["difficulty_" + str(difficulty)]["correct_answers"] = None
				empty_data[subject]["difficulty_" + str(difficulty)]["letter_grade"] = None

		empty_data_string = json.dumps(empty_data)
		print(empty_data_string)
		encryption = fernet.Fernet(key)
		encrypted_string = encryption.encrypt(empty_data_string.encode())

		# Write encrypted data
		with open(PATH_STATISTICS + HIGH_SCORES, 'wb') as f:
			f.write(encrypted_string)


def get_score_data():
	with open(PATH_STATISTICS + HIGH_SCORES, 'r') as scores_file, open(PATH_STATISTICS + SCORE_KEY, 'r') as key_file:
		key = key_file.read()
		score_data = scores_file.read()
		decryption = fernet.Fernet(key)

		score_data = json.loads(decryption.decrypt(score_data).decode())
		return score_data


def put_score_data(score_data):
	with open(PATH_STATISTICS + HIGH_SCORES, 'w+') as scores_file, open(PATH_STATISTICS + SCORE_KEY, 'r') as key_file:
		key = key_file.read()
		encoded_data = json.dumps(score_data).encode()
		encryption = fernet.Fernet(key)

		encrypted_data = json.loads(encryption.encrypt(encoded_data))
		scores_file.write(encrypted_data)


def validate_score(subject, difficulty, total_questions, correct_questions, avg_time, letter_grade):
	# There is currently a minimum of 50 questions
	if total_questions < 50:
		return

	if difficulty not in range(1, 5) or subject not in [styles.SUBJECT_HIRAGANA, styles.SUBJECT_KATAKANA, styles.SUBJECT_KANJI]:
		return

	current_scores = get_score_data()

	# if current_scores[subject]["difficulty_"][  + difficulty][letter_grade]:



