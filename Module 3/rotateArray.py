def rotate_array(input_array, k):
  k = k % len(input_array)
  input_array[:] = input_array[-k:] + input_array[:-k] #array places the last element([-k:]) into the front of the array([:-k] = array without last element)

#Test Cases
print(rotate_array([1,2,3,4,5,6,7], 3) # [ 5, 6, 7, 1, 2, 3, 4 ]
print(rotate_array([-1,-100,3,99], 2) # [ 3, 99, -1, -100 ]
