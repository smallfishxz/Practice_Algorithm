#### Solution 1
# Code referrence: http://www.geekviewpoint.com/python/sorting/heapsort
def heapsort( aList ):
  # convert aList to heap
  length = len( aList ) - 1
  leastParent = length // 2
  for i in range ( leastParent, -1, -1 ):
    moveDown( aList, i, length )
 
  # flatten heap into sorted array
  for i in range ( length, 0, -1 ):
    if aList[0] > aList[i]:
      aList[0], aList[i] = aList[i], aList[0]
      moveDown( aList, 0, i - 1 )
  return aList
 
 
def moveDown( aList, first, last ):
  largest = 2 * first + 1
  while largest <= last:
    # right child exists and is larger than left child
    if ( largest < last ) and ( aList[largest] < aList[largest + 1] ):
      largest += 1
 
    # right child is larger than parent
    if aList[largest] > aList[first]:
      aList[largest], aList[first] = aList[first], aList[largest]
      # move down to largest child
      first = largest;
      largest = 2 * first + 1
    else:
      return # force exit
 
### Solution2 
# code reference: http://www.geeksforgeeks.org/heap-sort/
# Python program for implementation of heap Sort
 
# To heapify subtree rooted at index i.
# n is size of heap
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
 
    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l
 
    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    # Change root, if needed
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]  # swap
 
        # Heapify the root.
        heapify(arr, n, largest)
    print(arr)
 
# The main function to sort an array of given size
def heapsort1(arr):
    n = len(arr)
 
    # Build a maxheap.
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)
 
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # swap
        heapify(arr, i, 0)
    return arr

print(heapsort1([9,5,6,3,2]))
