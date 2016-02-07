"""
This is a simple implementation of sequential search algorithm.
Input to the function is a list and an item/number to search in the list.
The function will print a text if the item is found in the list or not.
""" 

def sequentialSearch(alist, item):
  isFound = False
  ind = 0
  
  while ind < len(alist) and not isFound:
	if alist[ind] == item:
	  isFound = True
	  print "Yes!", item, "is in the list."
	else:
	  ind = ind + 1

  #if not isFound:
	#print "No,", item, "is not in the list."
  return isFound

"""
  for ind in range(len(alist)+1):
	if alist[ind] == item:
	  isFound = True
	  print "Yes!", item, "is in the list."
	  return
	
  if not isFound:
	print "No,", item, "is not in the list."
"""
