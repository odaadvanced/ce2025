num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
diff = num1 - num2
is_int = diff.is_integer()
print(F'The difference between {num1} and {num2} is an integer? {is_int}!')