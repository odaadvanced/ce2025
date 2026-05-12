student_data = {
    "john": {
        "birth": (7, 3, 2015),
        "scores": [87, 51, 56],
        },
    "also john": {
        "birth": (1, 30, 2016),
        "scores": [32, 57, 71],
        }
    }

averages = {}

class_total = 0
for person in student_data:
    total = 0
    for score in student_data[person]["scores"]:
        total = total + score
    average = score / len(student_data[person]["scores"])
    class_total = class_total + average
    averages[person] = average
    print(f"{person}'s average score is {average}")

class_average = class_total / len(student_data)
print(f"the class average is {class_average}")

highest_average = 0
for average in averages:
    if averages[average] > highest_average:
        highest_average = averages[average]

print(f"the highest average in the class is {highest_average}")