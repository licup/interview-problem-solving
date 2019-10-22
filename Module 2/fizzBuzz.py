def fizzbuzz(n):
  for current_number in range(1,n+1): # runs a for loop through the each number in the input
    if current_number % 3 == 0 and current_number % 5 == 0:
      print("fizzbuzz")
    elif current_number%3 == 0:
      print("fizz")
    elif current_number%5 == 0:
      print("buzz")
    else:
      print(current_number)

#input
test_case = int(input("Please enter an input number:"))
fizzbuzz(test_case)
