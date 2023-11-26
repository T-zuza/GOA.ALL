#Grasshopper - Summation
def summation(num):
    my_sum = 0
    for i in range(num + 1):
        my_sum += i
    return my_sum

#A Needle in the Haystack
def find_needle(haystack):
    my_arr = haystack.index("needle")
    return "found the needle at position " + str(my_arr)

#Returning Strings
def greet(name):
    return "Hello, " + name + " how are you doing today?" 

#quare(n) Sum
def square_sum(numbers):
    return sum(x ** 2 for x in numbers)