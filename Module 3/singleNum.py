def single_number(integers):
  integers.sort() #sorts all of the numbers in array
  i = 0
  while i < len(integers) - 1: 
    if integers[i] == integers[i+1]: #if first instance of number is equal to the next one it is not a single num
      i += 2
    else:
      return integers[i]
  return integers[-1] #returns last number in array if while loop finishes without it hitting the else
  
  #Test Cases
  print(single_number([4,1,2,1,2])) #returns 4
  print(single_number([3,2,2,5,6,1,3,1,5]) #returns 5
