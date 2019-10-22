def excel_column_to_number(n):
  letter = 0
  for current_letter in n.upper():
    letter = 26 * letter + (ord(current_letter) - 65 + 1)
  return letter
#Test Cases

print(excel_column_to_number("A")) #returns 1
print(excel_column_to_number("AZ")) #returns 52
