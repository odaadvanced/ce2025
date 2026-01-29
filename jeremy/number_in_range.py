while True:
    num = float(input("Enter a number "))

    is_true = False
    for n in range(10,21):
        if n == num:
            is_true = True

    if is_true == True:
        print(f"{num} is inside the range of 10-20")
    elif is_true == False:
        print(f"{num} is outside the range of 10-20")
