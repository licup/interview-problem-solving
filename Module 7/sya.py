'''
Reverse polish notation is a postfix notation for mathematical expressions. 
For example, the infix expression (1 + 2) / 3 would become 1 2 + 3 /. 
More detailed explanation here:  https://en.wikipedia.org/wiki/Reverse_Polish_notation

Task:
Given a mathematical expression in reverse polish notation, represented by an array of strings, 
find the answer to this expression. Operators consist only of +, -, *, /,
and all numbers are integer values. When performing a division on two numbers,
use python's integer division operator (//). Your output should be a single integer, 
which is the value of the expression when evaluated. Each expression is guaranteed to be valid.
'''
def evaluate_expression(expression):
  stack = []
  for element in expression:
    if element.isnumeric():
      stack.append(int(element))
    else:
      if element == '+':
        n = stack.pop()
        n1 = stack.pop()
        stack.append(n + n1)
      elif element == '-':
        n = stack.pop()
        n1 = stack.pop()
        stack.append(n1 - n)
      elif element == '/':
        n = stack.pop()
        n1 = stack.pop()
        stack.append(n1 // n)
      elif element == '*':
        n = stack.pop()
        n1 = stack.pop()
        stack.append(n1 * n)
  return stack.pop()

print(evaluate_expression(["3","4","+","5","-"])) #( 3 + 4 ) - 5 = 2
