"""
Bubble sort swaps elements next to each other, doing more passes until 0 swaps occur. 

Best used when the array is sorted lol. I mean to identify whether the array is sorted or not.

Best avoided when the array is reversed. In general, this sort isn't used that often irl.

Stability: stable

Time Complexity
Comparisons Best: O(n)
Swaps Best: O(1)
Comparisons Average: O(n^2)
Swaps Average: O(n^2)
Comparisons Worst: O(n^2)
Swaps Worst: O(n^2)

Space Complexity
Total: O(n)

"""

def bubble_sort(array):
  '''
  Uses bubble sort to sort an array.

  Args:
  array (int) : array to be sorted

  Returns:
  array (int) : sorted array
  '''
  array_length = int(len(array))
  num_of_swaps = 1
  
  # If num_of_swaps == 0, then that means the whole array is sorted since no numbers were swapped with each other
  while num_of_swaps != 0: 
    num_of_swaps = 0
    for i in range(array_length - 1):
      j = i + 1
      if array[j] < array[i]:
        array[j], array[i] = array[i], array[j]
        num_of_swaps += 1
      
  return array
