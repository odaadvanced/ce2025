fer1 = input(" enter a tempurture in degrees F: ")

cel1 = (float(fer1) - 32) * 5/9
answer1 = round(cel1, 2)
print (fer1, " degrees F is ", answer1, " degrees C ")

cel2 = input ("enter a tempurture in degrees C: ")

fer2 = float (cel2) * 9/5 + 32
answer2 = round(fer2, 2)
print (cel2, " degrees C is ", answer2, "degrees F")