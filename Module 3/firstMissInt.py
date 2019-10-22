def first_missing_positive_integer(integers):
  found = []
  for integer in integers:
    if integer < 0:
      continue
    if integer + 1 > len(found):
      extend_size = integer - len(found) + 1
      found.extend([False] * extend_size)
    found[integer] = True
    
  missing_integer = 0
  for position in range(1,len(found)):
    if found[position] == False:
      missing_integer = position
      return missing_integer
  if missing_integer == 0 and len(found) == 0:
    return 1
  elif missing_integer == 0 and len(found) > 0:
    return len(found)
    
#Test Cases
print(first_missing_positive_integer([1,2,0])) #returns 3
print(first_missing_positive_integer([3,4,-1,1])) #returns 2
print(first_missing_positive_integer([-8, -7, -6])) #returns 1
