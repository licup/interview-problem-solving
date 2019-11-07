'''
Given a sorted array and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.
'''
def find_index(sorted_list, target):
  start = 0
  end = len(sorted_list)-1
  while start < end:
    mid = (start+end) //2
    if target <= sorted_list[mid]:
      end = mid
    else:
      start = mid + 1
  if sorted_list[start] < target:
    return start + 1
  else:
    return start
    
print(find_index([1,3,5,6], 5)) #returns 2
print(find_index([1,3,5,6], 2)) #returns 1
print(find_index([1,3,5,6], 0)) #returns 0
print(find_index([1,3,5,6], 7)) #returns 4
