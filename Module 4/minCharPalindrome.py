'''
You are given a string. The only operation allowed is to insert characters in the beginning of the string.
Return the number of characters that are needed to be inserted to make the string a palindrome string.
'''
def minimumCharacters(s):
	length = len(s)
	match = 1
	for x in range(1,length):
		start = 0
		end = x
		pal = 1
		while(start < end):
			if(s[start] != s[end]):
				pal = 0
				break
			start += 1
			end -= 1
		if(pal):
			match += 1
	return length - match
  
  print(minimumCharacters("ABC")) #returns 2
  print(minimumCharacters("AACECAAAA")) #returns 2
