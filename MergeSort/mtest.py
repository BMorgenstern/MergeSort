from mergesort import *


def main():
	list1 = [123, 34, 189, 56,  150, 12, 9, 240]
	print("Before sorting:")
	for elem in list1:	
		print(elem)
	print("After sorting:")
	for elem in MergeSort(list1):
		print(elem)
		


if __name__ == '__main__':
	main()