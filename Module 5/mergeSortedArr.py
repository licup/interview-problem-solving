'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
'''

def merge_sorted_list(nums1, nums2):
  nums1_index = 0
  nums2_index = 0
  
  while nums2_index < len(nums2):
    if nums2[nums2_index] <= nums1[nums1_index] or nums1[nums1_index] == 0:
      nums1.insert(nums1_index,nums2[nums2_index])
      nums1.pop()
      nums2_index+=1
    else:
      nums1_index+=1
  return nums1
  
print(merge_sorted_list([1,2,3,0,0,0],[2,5,6])) #returns [1,2,2,3,5,6]
