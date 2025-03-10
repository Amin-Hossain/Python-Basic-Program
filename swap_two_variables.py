#input two variables
a = input("Enter the value of the first variale :")
b = input ("Enter the value of the second variable :")
#display the original value
print (f"original value : a ={a}, b = {b}")
#swap the values using a temporary variable
temp = a
a = b
b = temp
#display the swapped values
print (f"Swapped values : a = {a}, b = {b}")
