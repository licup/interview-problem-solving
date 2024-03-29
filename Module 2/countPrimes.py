# Determine if the input number is a prime number
def isPrime(n):
  for current_number in range(2,n):
    # if the input number is evenly divisible by the current number?
    if n % current_number == 0:
      return False
  return True

# Determine how many prime numbers are UNDER the input number
def countPrimes(n):
  prime = 0
  for i in range(2,n):
    if isPrime(i):
      prime+=1
  return prime

# Test Cases

print(countPrimes(10)) # should return 4
print(countPrimes(40)) # should return 8
