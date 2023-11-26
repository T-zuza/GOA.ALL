import random
print(random.randint(1,50))

my_students = ["taso","tiko","rezi","leo","nati","vaxo","ika"]
arr_of_cars = ["bmw","mercedes","prius","porche","bughati","opel","homnda"]

for i in range(len(my_students)):

    print(random.choice(my_students)  ,  "you won a car:"  ,   random.choice(arr_of_cars))
  
my_students = ["taso","tiko","rezi","leo","nati","vaxo","ika"]
arr_of_cars = ["bmw","mercedes","prius","porche","bughati","opel","homnda"]
for i in range(len(my_students)):
        winner=(random.choice(my_students))
        lucky_car=(random.choice(arr_of_cars))
        print(winner  ,  "you won a car:"  ,   lucky_car)
        my_students.remove(winner)
        arr_of_cars.remove(lucky_car)



