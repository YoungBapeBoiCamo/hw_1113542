# Name: Ferran
# Student ID: 1113542
# Date of Submission: 2024/11/28

import heapq

def merge_k_sorted_arrays(k, arrays):
    # Initialize the min heap 
    min_heap = []
    # Result array to store merged sorted elements
    result = []
    
    # Insert the first element of each array along with array index and element index
    for i in range(k):
        if arrays[i]:  # Check if the array is not empty
            heapq.heappush(min_heap, (arrays[i][0], i, 0))  

    # Process the heap
    while min_heap:
        # Extract the smallest element
        val, arr_index, ele_index = heapq.heappop(min_heap)
        result.append(val)  # Add it to the result
        
        # If there is another element in the same array, insert it into the heap
        if ele_index + 1 < len(arrays[arr_index]):
            next_val = arrays[arr_index][ele_index + 1]
            heapq.heappush(min_heap, (next_val, arr_index, ele_index + 1))
    
    return result

# input
k = int(input("Enter the number of arrays (K): "))
arrays = []

for i in range(k):
    arr = list(map(int, input(f"Enter sorted array {i+1} ( SPACE SEPARATED ): ").split()))
    arrays.append(arr)

# Merge the arrays
merged_array = merge_k_sorted_arrays(k, arrays)

# Output the merged array
print("Merged Array:", merged_array)
