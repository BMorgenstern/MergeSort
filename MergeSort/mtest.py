from mergesort import *
import sys

def main(args):
	Merged = []
	#hardcoded array given as an example
	list1 = [123, 34, 189, 56,  150, 12, 9, 240]
	if len(args) < 2:
		Merged = MergeSort(list1)
	else:
		'''
		Number of splits can be given from the terminal, 
		2 is assumed when the input is invalid of no input is given
		'''
		try:
			splits = int(args[1])
		except ValueError:
			print(args[1]+' is not a number; assuming 2...')
			splits = 2
		debug = len(args) > 2
		'''
		print debug info if there any terminal arguments beyond the number of splits
		'''
		Merged = MergeSort(list1, splits, debug)
	print(Merged)


if __name__ == '__main__':
	main(sys.argv)