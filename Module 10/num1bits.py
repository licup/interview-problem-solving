'''
Given an integer value in Python, return the count of "1" bits the number has, 
when converted as a 32-bit unsigned integer.
'''
def count_set_bits(num):
	counter = 0
	newNum = bin(num)
	for x, bit in enumerate(newNum):
		if bit == '1':
			counter += 1
	return counter

print(count_set_bits(500)) #returns 6
