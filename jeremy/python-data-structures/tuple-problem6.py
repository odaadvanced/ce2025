two_numbers = (5,10)

def cool_function(two_num):
    x, y = two_num
    num_sum = x + y
    num_dif = x - y
    num_prod = x * y
    return num_sum, num_dif, num_prod

print(cool_function(two_numbers))