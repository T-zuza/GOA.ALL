#This code does not execute properly. Try to figure out why.
def multiply(a, b):
    a * b

    # Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
    def even_or_odd(number):
       if number %2==0:
        return "Even"
       else:
        return "Odd"

#We need a function that can transform a number (integer) into a string.
#What ways of achieving this do you know?
def number_to_string(num):
     return str(num)

#Very simple, given an integer or a floating-point number, find its opposite.
def opposite(number):
  # your solution here
    opposite=-number
    return  opposite

#Complete the solution so that it reverses the string passed into it.
def solution(string):
    my_str=""
    i = len(string)

    while i > 0:
        my_str += string[i-1]
        i -= 1

    return my_str

#In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?
def make_negative( number ):
    if number >= 0:
        return number *-1
    return number

#Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    return "No"

#You get an array of numbers, return the sum of all of the positives ones.
#Example [1,-4,7,12] => 1 + 7 + 12 = 20
#Note: if there is nothing to sum, the sum is default to 0.
def positive_sum(arr):
    sum = 0
    for Element in arr:
        if Element > 0:
            sum += Element
    return sum

#Write a function that accepts an integer n and a string s as parameters, and returns a string of s repeated exactly n times.
#Examples (input -> #output)
def repeat_str(repeat, string):
    return repeat * string

#It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. You're given one parameter, the original string. You don't have to worry with strings with less than two characters.
def remove_char(s):
    return s  [ 1 : -1]

#Given an array of integers your solution should find the smallest integer.
def find_smallest_int(arr):
    # Code here
    return min(arr)

#The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to and including the year 200, etc.
#Given a year, return the century it is in.
def century(year):
    if year % 100  == 0:
        return year // 100
    return year // 100 + 1

#Clock shows h hours, m minutes and s seconds after midnight.
#Your task is to write a function which returns the time since midnight in milliseconds.
def past(h, m, s):
    return (h  *3600 + m * 60 + s) * 1000

#Write a function that accepts an integer n and a string s as parameters, and returns a string of s repeated exactly n times.
def repeat_str(repeat, string):
    return repeat * string

#Your classmates asked you to copy some paperwork for them. You know that there are 'n' classmates and the paperwork has 'm' pages.
#Your task is to calculate how many blank pages do you need. If n < 0 or m < 0 return 0.
def paperwork(n, m):
    if n > 0 and m > 0:
        return m * n
    return 0

#Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each. If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love.
#Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.
def lovefunc( flower1, flower2 ):
    if (flower1 + flower2) % 2 == 0:
        return False
    return True

#Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
#The output should be two capital letters with a dot separating them.
def abbrev_name(name):
    my_list = name.split()
    list_name = my_list[0]
    list_surname = my_list[1]
    
    return (list_name[0] + "." + list_surname[0]).upper()

