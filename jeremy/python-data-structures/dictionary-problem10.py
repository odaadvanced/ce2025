gradebook = {
    "john": {
        "math": 70,
        "science": 2,
        "history": 90
        },
    "johnson": {
        "math": 10,
        "science": 50,
        "history": 30
        }
    }

for person in gradebook:
    total = 0
    for section in gradebook[person]:
        total = total + gradebook[person][section]
    average = total / len(gradebook[person])
    print(f"{person}'s average grade is {average}")