# remove string spaces
def no_space(x):
    new_str=""
    for i in x:
        if i!= "":
            new_str += i
    return new_str   
print(no_space("nika keshelava is the CEO of GOA"))