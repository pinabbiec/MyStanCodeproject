"""
File: boggle.py
Name: Abbie Chen
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	TODO: find all the possible combination of words in the boggle
	"""
	start = time.time()
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')
	row_list = []
	for i in range(4):
		row = input(f'{i+1} row of letters: ')
		if len(row) != 7:
			print('Illegal input')
			break
		else:
			# make sure the input is correct
			if row[0].isalpha() or row[2].isalpha() or row[4].isalpha() or row[6].isalpha():
				row_l = []
				row_l = [row[0].lower(), row[2].lower(), row[4].lower(), row[6].lower()]
				row_list.append(row_l)
			else:
				print('Illegal input')
	# print(row_list)
	ans_num = boggle(row_list)
	print(f'There are {ans_num} words in total.')


def boggle(row_list):
	d = read_dictionary()
	ans_lst = []
	for x in range(len(row_list)):
		for y in range(len(row_list[0])):
			# choose a starting point
			s = row_list[x][y]
			path = [(x, y)]
			boggle_helper(row_list, d, s, path, ans_lst, (x, y))
	return boggle_helper(row_list, d, s, path, ans_lst, (x, y))


def boggle_helper(row_list, d, s, path, ans_lst, cur_pos):
	# print(s)
	if len(s) >= 4:
		if s in d:
			if s not in ans_lst:
				ans_lst.append(s)
				print(f'Found: {s}')
	cur_x, cur_y = cur_pos
	for i in range(-1, 2, 1):
		for j in range(-1, 2, 1):
			next_x = cur_x + i
			next_y = cur_y + j
			# choose
			if 0 <= next_x < len(row_list):
				if 0 <= next_y < len(row_list):
					if (next_x, next_y) not in path:
						s += row_list[next_x][next_y]
						cur_pos = (next_x, next_y)
						path.append((next_x, next_y))
						# explore
						if has_prefix(s, d):
							boggle_helper(row_list, d, s, path, ans_lst, cur_pos)
						# un-choose
						s = s[:-1]
						path.pop()
	return len(ans_lst)


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	d = []
	with open(FILE, 'r') as f:
		for line in f:
			word = line.split('\n')
			d.append(word[0])
	return d


def has_prefix(sub_s, d):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:param sub_s: (dict) Dictionary for check
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in d:
		if word.startswith(sub_s):
			return True
	return False



if __name__ == '__main__':
	main()
