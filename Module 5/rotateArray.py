'''
Suppose a sorted array A is rotated at some pivot unknown to you beforehand.
Find the minimum element.
The array will not contain duplicates.

Note: If you know the number of times the array is rotated, then this problem becomes trivial. 
      If the number of rotation is x, then minimum element is A[x].
''''
def find_pivot_index(input_list):
  # List is sorted, but then rotated.
  # Find the minimum element in less than linear time
  # return it's index
  start = 0
  end = len(input_list) - 1
  minimum_index = 0
  while start < end - 1:
    if end - start % 2 == 0:
      pivot = int((end - start / 2)) + start
    else:
      pivot = int((end -start + 1) / 2) + start
    if input_list[pivot] < input_list[minimum_index]:
    	end = pivot
    	minimum_index = pivot
    else:
      start = pivot
  return minimum_index

print(find_pivot_index([0, 1, 2, 4, 5, 6, 7]) #returns 4 5 6 7 0 1 2
