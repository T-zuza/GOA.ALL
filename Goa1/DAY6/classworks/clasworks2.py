age = 16
if age < 18: print("Apply Discount")
print("Proceed to Payment")

age = 75
if age < 18: 
  print("Junior discount")
elif age >= 75: 
  print("Senior discount")
else:
  print("No discount")
print("Proceed to payment")

age=75
if age < 18:
    print("Junior discount")
elif age >= 75:
    print("Senior discount")
else:
    print("No discount")

    age = 16
is_student = True

if age < 18:
  #execute if age is less than 18
  if is_student:
    #execute if under 18 and also a student
    print("20% discount")
  else:
    #execute if under 18 and not a student
    print("10% discount")
else:
  #execute this code customer 18 or over
  print("Regular price")

  for x in range(2):
     print("Repeat")
print("Stop")

count = 1
while count > 10:
  print(count)

  cart = ['lamp', 'candles', 'chair', 'carpet']
  print(cart[:3])