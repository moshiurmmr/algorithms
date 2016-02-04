# This is a Heap Sort algorithm implementation

# to make the code equivalent to the algorithm, the array 'A' starts from inindex 1. Hence,  put a None at the A[0] position and the array size in n+1 rather than n

def Parent(i):
  return i/2
def LeftChild(i):
  return 2*i
def RightChild(i):
  return 2*i+1

# make the array 'A' a heap, 'n' is the total number of elements in 'A' and 'i' is the particular position to implement the heap
def Heapify(A,i,n):
  l = LeftChild(i)
  r = RightChild(i)
  if l <= n and A[l] > A[i]:
	largest = l
  else:
 	largest = i
  if r <= n and A[r] > A [largest]:
	largest = r
  if largest != i:
	A[i], A[largest] = A[largest], A[i]
	Heapify(A, largest, n)

def HeapLength(A):
  return len(A) - 1

def BuildHeap(A):
  # build a heap A from the unsorted array A
  n = HeapLength(A)
  for i in range(n/2, 0 , -1):
	Heapify(A, i, n)

def HeapSort(A):
  # use Heapify to build a ascending order sorted array of A
  BuildHeap(A)
  HeapSize = HeapLength(A)
  for i in range(HeapSize, 1, -1):
	# put largest element (to element of the heap) at the end of the array A
	A[1], A[i] = A[i], A[1]
	# shrink the heapsize by removing the largest element from the heap
	HeapSize = HeapSize - 1
	# make a heap of the rest (excluding the one already put at the beginning of the sorted array A) of the array
	Heapify(A, 1, HeapSize)
