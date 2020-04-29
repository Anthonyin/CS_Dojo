# a mapping
# input or an argument
def function(x):
    return 2 * x


a = function(2)
print(a)


def function1(x, y):
    return x + y


e = function1(2, 7)
print(e)


def function2(x):
    print(x)
    print("still in this function")
    return 2 * x


f = function2(2)
print(f)


def convert(km):
    return 0.62137 * km


km = float(input("Enter your number in km: "))
number = convert(km)
print("{} km convert in miles is {}".format(km, number))
