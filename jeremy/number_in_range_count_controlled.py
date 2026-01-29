while True:
    num = float(input("Enter a number "))

    is_true = False
    for n in range(5,16):
        print(n)
        if n == num:
            is_true = True

    if is_true == True:
        print(f"{num} is inside the range of 5-15")
    elif is_true == False:
        print(f"{num} is outside the range of 5-15")