def MergeSort(src_array):
	if len(src_array) < 2:
		return src_array
	midpoint = int(len(src_array)/2)
	lsub = MergeSort(src_array[:midpoint])
	rsub = MergeSort(src_array[midpoint:])
	return Merge(lsub, rsub)

def Merge(llist, rlist):
	retlist = []
	
	while(len(llist) > 0 and len(rlist) > 0):
		if llist[0] < rlist[0]:
			retlist.append(llist[0])
			del llist[0]

		else:
			retlist.append(rlist[0])
			del rlist[0]
				
	return retlist+llist+rlist