def divide(num1, num2):
    try:
        print(num1 / num2)
    except TypeError:
        print("Both must be numbs")
    except ZeroDivisionError:
        print("num2 must not be zero")
#wow