from mergesort import *
import sys

def getIntArray():
	retlist = []
	while True:
		num = input("Enter an integer value to add to the array, or hit Enter to stop inputting values ")
		if num == "":
			return retlist
		try:
			retlist.append(int(num,10))
		except ValueError:
			print(num+" is not a number")

def main(args):
	Merged = []
	
	#hardcoded array given as an example
	#list1 = [123, 34, 189, 56,  150, 12, 9, 240]
	
	list1 = getIntArray()
	print("Before sorting: ")
	print(list1)
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
	print("After sorting : ")
	print(Merged)


if __name__ == '__main__':
	main(sys.argv)