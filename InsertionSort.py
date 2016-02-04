"""
 This is a insertion sort algorithm
"""
def InsertionSort(arr):
  for indx in range(1, len(arr)):
	nxtElmnt = arr[indx]
	prvElmntIndx = indx - 1
	while (prvElmntIndx >= 0) and (arr[prvElmntIndx] > nxtElmnt):
	  arr[prvElmntIndx + 1] = arr[prvElmntIndx]
	  prvElmntIndx = prvElmntIndx - 1
   	arr[prvElmntIndx + 1] = nxtElmnt 
	

	
