'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem.
'''

def string_cleaning_fun(d_string):
  lowercase_string = d_string.lower()
  empty_string = ""
  for element in lowercase_string:
    if element.isalpha():
      empty_string = empty_string + element
  return empty_string
def isPalindrome(input_str):
  empty_string = string_cleaning_fun(input_str)
  if empty_string == empty_string[::-1]:
    return 1
  return 0

print(isPalindrome("Racecar")) #returns 1
print(isPalindrome("dog")) #returns 0
print(isPalindrome("A man, a plan, a canal, Panama.")) #returns 1
