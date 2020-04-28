a = 2
b = 2
if a < b:
    print("a is less than b")
elif a == b:
    print("a is equal to b")
else:
    print("a is greater than b ")

name = input("Please enter your name: ").capitalize()
height = int(input("Please enter your height in cm: "))
weight = float(input("Please enter your weight in kg: "))

bmi = weight / (height ** 2) * 10000
print("Hi {}, Your BMI is: {}".format(name,bmi))

if bmi <= 18.5:
    print("Your are underweight. ")
elif bmi >= 30:
    print("Your are obseity")
elif bmi <= 24.9:
    print("Your are normal weight")
else:
    print("Your are overweight")