"""
Selection sort is a sorting algorithm that sorts an unsorted array. Goes through every index finding the smallest one then swapping at the end.

Best used when the array is completely unsorted and small.

Best avoided when the array is partially sorted and large.

Stability: Not stable

Time Complexity
Comparisons Best: O(n^2)
Swaps Best: O(1)
Comparisons Average: O(n^2)
Swaps Average: O(n)
Comparisons Worst: O(n^2)
Swaps Worst: O(n)

Space Complexity
Total: O(1)

flowchart: selection_sort_flowchart.jpg
"""

def selection_sort(array):
    """
    Apply selection sort on a given integer array

    Args:
        array (int array): The array of numbers that require sorting

    Returns:
        int array: the sorted array 
    
    """
   
    array_length = int(len(array))

    for i in range(0, array_length - 1):
        min_index = i # Sets the minimum as the first index
        for j in range(i + 1, array_length):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    
    return array
