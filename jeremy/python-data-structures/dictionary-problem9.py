gradebook = {
    "john": 27,
    "john2": 76,
    "john3": 97,
    "john4": 37,
    "not john": 0
    }

total = 0

for person in gradebook:
    total = total + gradebook[person]
    
average = total / len(gradebook)

print(average)