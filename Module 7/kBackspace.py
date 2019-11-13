'''
K Backspaces
The backspace key is broken. Every time the backspace key is pressed, instead of deleting the last 
(non-backspace) character, a '<' is entered. 

Given a string typed with the broken backspace key, write a program that outputs the 
intended string i.e what the keyboard output should be when the backspace key works properly.

Input
One line containing the string that was written in the text editor. 
Only contains lowercase letters from the English alphabet as well as the character '<'.
'<' will not be the first character.
'''

def k_backspace(inputString):
  stack = []
  for character in inputString:
    if character == "<":
      stack.pop()
    else:
      stack.append(character)
  return "".join(stack)
	

# Test Case
testInput = 'a<bc<'
actualOutput = k_backspace(testInput)
print(actualOutput) #returns 'b'
