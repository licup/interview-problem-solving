def excel_column_to_number(n): #Takes in a string input and converts it to the the excel column number
  letter = 0
  for current_letter in n.upper():
    letter = 26 * letter + (ord(current_letter) - 65 + 1)
  return letter

#Test Cases
print(excel_column_to_number("A")) #returns 1
print(excel_column_to_number("AZ")) #returns 52
print(excel_column_to_number("BZ")) #returns 78
