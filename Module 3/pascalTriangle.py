'''
Pascal's Triangle

Given numRows, generate the first numRows of Pascal’s triangle.
Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.
'''
def pascal_triangle(numRows):
  triangle = []
  for i in range(numRows):
    triangle.append([])
    for j in range(i + 1):
      if j in (0,i):
        triangle[i].append(1)
      else:
        triangle[i].append(triangle[i-1][j-1] + triangle[i-1][j])
  return triangle

#Test Case
print(pascal_triangle(5)) 
'''should return 
[
     [1],
     [1,1],
     [1,2,1],
     [1,3,3,1],
     [1,4,6,4,1]
]
'''
