'''
Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses
( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:
It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.

Given a parentheses string, return the minimum number of parentheses we must add to make 
the resulting string valid.

Input
S.length <= 1000
S only consists of '(' and ')' characters.
'''
def minAddToMakeValid(S):
  counter = 0
  stack = []
  for i, element in enumerate(S):
    if element == '(':
      stack.append(element)
    else:
      if stack == []:
        counter +=1
      else:
        stack.pop()
  return len(stack) + counter
    
sampleInput = '())'
print(minAddToMakeValid(sampleInput)) #returns 1
