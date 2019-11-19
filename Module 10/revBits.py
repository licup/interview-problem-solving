'''
Given an integer n, reverse its first 32 bits, and return the reversed-bit integer.
0 <= n <= 2^32 - 1
Example:
5 (00000000000000000000000000000101) ==> 2684354560 (10100000000000000000000000000000)
'''
def reverse_bits(num):
	initBit = bin(num) #changing the input into a binary number
	reverseBit = initBit[::-1]#reversing initBit
	binNum = reverseBit[0:-2] #removes the extra b0 at the end of the binary string
	while len(binNum) != 32: #adds 0s to the left until there are 32 bits
		binNum += '0'
	return int(binNum, 2)
print(reverse_bits(5))
