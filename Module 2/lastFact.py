def last_factorial_digit(n):
  fact = 1
  for x in range(n, 1, -1): #fact is constantly multiplied by increments of n-1
    fact *= x
  num = str(fact) #turns the factorial number into 3
  return int(num[-1]) #returns the last number of the factorial number
  
#Test Cases
print(last_factorial_digit(3)) #returns 6
print(last_factorial_digi(9)) #returns 0
