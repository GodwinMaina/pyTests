# QUESTION 4

# Write a program that takes an integer as input and returns an integer with
# reversed digit ordering.
# Examples:
# For input 500, the program should return 5.
# For input -56, the program should return -65.
# For input -90, the program should return -9.
# For input 91, the program should return 19.

def reverse_integer():
  number=input("ENTER A NUMBER: ")

# -ve
  if number[0]=='-':
    output= '-'+ str(int(number[:0:-1]))
    print(output)
  
# +ve
  else:
    output=int(number[::-1])
    print(output)

reverse_integer()