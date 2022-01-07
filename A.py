def bubblesort(array):
  for n in range(len(array)-1, 0, -1):
    for i in range(n):
      if array[i] > array[i + 1]:
        array[i], array[i + 1] = array[i + 1], array[i]
array = [39,12,18,85,72,10,2,18]
  
print("Unsorted list is,") 
print( array)
bubblesort(array)
print("Sorted Array is, ")
print(array)