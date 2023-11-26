def square_sum(number):
    my_sum = 0
    for num in number:
        my_sum +=(num **2)
    return my_sum
print(square_sum([3,5,7]))