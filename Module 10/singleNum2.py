'''
Given an array of integers, every element appears thrice except for one which occurs once.
Find that element which does not appear thrice.
Note: Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?

Example:
>> arr = [1, 2, 3, 1, 2, 3, 1, 2, 3, 4]
>> single_number(arr) # returns 4
'''

def single_number(nums):
	nums.sort()
	x = 0
	while x < len(nums) - 1:
		if nums[x] == nums[x+1] and nums[x] == nums[x+2]:
			x += 3
		else:
			return nums[x]
	return nums[-1]
ar = [1, 2, 3, 1, 2, 3, 1, 2, 3, 4]
print(single_number(ar))

#Test Case from Example

print(single_number([1, 2, 3, 1, 2, 3, 1, 2, 3, 4])) #returns 4
