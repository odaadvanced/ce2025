numbers = [4,7,2,7,9,4,1,2]
new_list = []

for n in numbers:
    for new_n in new_list:
        if n == new_n:
            break
    else:
        new_list.append(n)

print(new_list)