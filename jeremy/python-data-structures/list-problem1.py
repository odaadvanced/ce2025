num_list = [3621, 7362, 36217, 2, 4, 12379, 32163217, 74, 13, 746]

even_list = []
total = 0

for n in num_list:
    if n % 2 == 0:
        even_list.append(n)
    total = n + total

average = total / len(num_list)

print(f"max is {max(num_list)} and min is {min(num_list)}")
print(f"even numbers in num_list are {even_list}")
print(f"average of num_list is {average}")