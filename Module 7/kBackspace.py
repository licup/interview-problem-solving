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
