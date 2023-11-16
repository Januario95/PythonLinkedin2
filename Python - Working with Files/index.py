import os
from timeit import timeit
from pathlib import Path


def count_files_with_scandir(path):
	total = 0
	for entry in os.scandir(path):
		if entry.is_file():
			total += 1
		else:
			total += count_files_with_scandir(entry)
	return total


def count_files_with_pathlib(path):
	total = 0
	for entry in Path(path).iterdir():
		if entry.is_file():
			total += 1
		else:
			total += count_files_with_pathlib(entry)
	return total

if __name__=='__main__':
	path = 'C:/Users/a248433/Documents/Learning/' #/Programming/My Projects'
	total = count_files_with_scandir(path)
	# print(timeit('count_files_with_scandir(".")',
	# 	'from __main__ import count_files_with_scandir'))

# total = count_files_with_scandir('.')
# print(total)
# print('')

# path = 'C:/Users/a248433/Documents/Learning/' #/Programming/My Projects'
# total = count_files_with_pathlib(path)
# print(total)
# total = count_files_with_pathlib('.')
# print(total)


















































