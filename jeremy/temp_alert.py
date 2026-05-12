while True:
    temp = float(input("Give a temperature "))

    if temp < 32 or temp > 100:
        print("Warning")
    else:
        print("Normal")
