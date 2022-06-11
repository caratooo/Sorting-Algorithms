'''
Insertion sort at the heart

Example array: 62, 83, 18, 53, 07, 17, 95, 86, 47, 69, 25, 28

Insertion sorts use gap of 1. (So it sorts numbers within 1 indice radius)
However, with shell sort, we decide what gap to compare, and we work our gap size all the way down to one. 

Lets try gap sizes: 5, 3, 1*
*We always end at gap of 1

GAP 5:
*62*, ~83~, -18-, 53, (07), *17*, ~95~, -86-, 47, (69), *25*, ~28~

62 has a gap size of 5 with 17 and 25
Subarray ** : 62, 17, 25
Insertion sort on subarray
62, 17, 25 -> 17, 62, 25 -> 17, 25, 62 -> done

Repeat with all subarrays

End up with:
** : 17, 25, 62
~~ : 28, 83, 95
-- : 18, 86
   : 47, 53
() : 07, 69

First round array:
17, 28, 18, 47, 07, 25, 83, 86, 53, 69, 62, 95

GAP 3:
*17*, -28-, (18), *47*, -07-, (25), *83*, -86-, (53), *69*, -62-, (95)

Insertion sort subarrays againnnnnn

End up with:
** : 17, 47, 83, 69
-- : 07, 28, 62, 86
() : 18, 25, 53, 95

Second round array:
17, 07, 18, 47, 28, 25, 83, 62, 53, 69, 86, 95

GAP 1:

Insertion sortttttt

Sorted array:
07, 17, 18, 25, 28, 47, 53, 62, 69, 83, 86, 95

Choosing gap size:
5, 3, 1 is one way.
Use N/2^k
N : length of array

Best used when the amount of difference of numbers on the borders. Reg insertion sort would be worst case really often if you used that.

Best avoided if they're just regular numbers.

Stability: Not stable

Time Complexity
Best for worst gap sequence: O(nlog^2n)
Best for best gap sequence: O(nlogn)
Worst for worst gap sequence: O(n^2)
Worst for best gap sequence: O(log^2n)

Space Complexity
Total: O(n)

'''


def shell_sort(array):
  '''
  Sorts array using shell sorted

  Args:
  array (int) : array to be sorted

  Returns:
  array (int) : sorted array
  '''
  array_length = int(len(array))
  list_of_gap_sizes = []
  gap_size = array_length
  k = 1 # Used for the N/2**k gap size calculation

  while gap_size > 1:
      gap_size = int(array_length / 2**k)
      list_of_gap_sizes.append(gap_size)
      k += 1

  for x in list_of_gap_sizes:
      for i in range(0, x): # Creates first index of different subarrays
          for j in range(i, array_length, x): # Determines the other indices of the subarray
              for z in range(j, i, -x): # Insertion sort on subarray
                  if array[z] < array[z - x]:
                      array[z], array[z - x] = array[z - x], array[z]

  return array
