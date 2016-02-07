"""
This is a binary search algorithm. The list is divided into half and checked
if the middle item is the item being searched. If not and if the middle item
is smaller than the searched item, the list is sliced to a smaller list whose
first item is the next item to the middle item and the search continues to the
sliced list. If the middle item is larger than the searched item, the sliced
list is built whose last element is the item just before the middle item. 
"""

def binarySearch(alist, item):
  firstInd = 0
  lastInd = len(alist)-1
  isFound = False
  
  while (firstInd <= lastInd and not isFound):
	midInd = (firstInd + lastInd)//2
	if alist[midInd] == item:
	  isFound =  True

	else:
	  if alist[midInd] < item:
	    firstInd = midInd + 1
	  else:
	    lastInd = midInd - 1 

  return isFound

# Test binarySearch
"""
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))
"""
