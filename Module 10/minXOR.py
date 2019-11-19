'''
Given a list of unsigned integers, find the pair of integers in the array which
have the minimum XOR value. Return the minimum XOR value.

Examples : 
Input 
0 2 5 7 
Output 
2 (0 XOR 2) 
Input 
0 4 7 9 
Output 
3 (4 XOR 7)
Constraints: 
2 <= N <= 100 000 
0 <= A[i] <= 1 000 000 000
'''
def min_xor_value(num):
	num.sort() #sort the list to make things easier

	minXor = 99999 #minXor number is high so that it can find the next small number easier
	value = 0
	for i in range(0,len(num)-1):
		for j in range(i+1,len(num)-1):
			value = num[i]^num[j]
			minXor = min(minXor,value)
	return minXor 
  
#Test Case from Example
print(min_xor_value([0,2,5,7]))
