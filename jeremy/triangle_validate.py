while True:
    side1 = float(input("Enter a side "))
    side2 = float(input("Enter another side "))
    side3 = float(input("Enter another another side "))
    
    if side1 + side2 > side3 or side2 + side3 > side1 or side3 + side1 > side2:
        print("is triangle :D")
    else:
        print("is NOT triangle >:C")