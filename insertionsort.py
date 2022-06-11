"""
Insertion sort is a sorting algorithm that sorts an unsorted array. Constantly swaps elements until it's done.

Best used when the array is almost sorted and small.

Best avoided when the array is completely unsorted and large.

Stability: Stable

Time Complexity
Comparisons Best: O(n)
Swaps Best: O(1)
Comparisons Average: O(n^2)
Swaps Average: O(n^2)
Comparisons Worst: O(n^2)
Swaps Worst: O(n)

Space Complexity
Total: O(n)
"""

def insertion_sort(array):
  '''
  Does insertion sort on array. 

  Args:
  array (int array): The array of numbers that require sorting

  Returns:
  int array : sorted array
  '''

  array_length = int(len(array))
  
  for i in range(1, array_length):
    for j in range(i, 0, -1): # Checks if each index before it is less then the current
      if array[j] < array[j - 1]:
        array[j], array[j - 1] = array[j - 1], array[j]

  return array
