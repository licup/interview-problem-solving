'''
Given two strings s and t , write a function to determine if t is an anagram of s.
'''
def valid_anagram(s,t):
  if len(s) != len(t):
    return False
  s = sorted(s)
  t = sorted(t)
  return s == t 

print(valid_anagram("anagram","naragam")) #returns False
print(valid_anagram("anagram","naaragam")) #returns False
print(valid_anagram("trip","ptir")) #returns True
