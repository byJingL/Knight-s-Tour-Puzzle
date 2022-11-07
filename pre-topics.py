# ----------------- Megic Method ------------------- #
class Sun:
    n = 0  # number of instances of this class

    def __new__(cls):
        if cls.n == 0: 
            cls.n += 1
            return object.__new__(cls)  # create new object of the class

sun1 = Sun()
print(sun1.n)
# n is 1, cant return new object. resrict the number of projrct, 
sun2 = Sun()
try:
    print(sun2.n)
except AttributeError:
    print("'NoneType' object has no attribute 'n'")

class Account:
    def __init__(self, number, funds, status="active"):
        self.number = number
        self.funds = funds
        self.status = status

    def __repr__(self):
        return f'Account {self.number} for {self.funds}'

    def __str__(self):
        return f'Account {self.number} for {self.funds} {self.status}'

new_account = Account(18, 28)
# Default will print 'str'
print(new_account)  # Account 18 for 28 active
# If want print 'repr'
print(repr(new_account))

# ----------------- Nested List Comprehension ------------------- #
countries = [["Beijing", "Shanghai", "Guangzhou"], 
          ["London", "York"],
          ["New York", "Boston"],
          ]
city_list1 = []
for country in countries:
    for city in country:
        city_list1.append(city)
# 1st for: outter loop, 2nd for: inner loop
city_list2 = [city for country in countries for city in country]
print(city_list1, '\n', city_list2)

# ----------------- Overriding after Inheritanc ------------------- #
class Animal:
    def __init__(self, species):
        self.species = species
        self.tail = 0
        print("Animal __init__")

class Dog(Animal):
    def __init__(self, name):
        super().__init__("dog")
        # Override the attributes
        self.eye_num = 1
        self.name = name
        print("Cat __init__")

dog = Dog("Lucky")    
print(dog.species, dog.name, dog.tail)

# ----------------- User-defined Exceptions ------------------- #
# Example 1
class ZeroDivisionError(Exception):
    pass

def divide(x, y):
    try:
        if y == 0:
            raise ZeroDivisionError
        else:
            print(x / y)
    except ZeroDivisionError:
        print("The denominator is 0! Try again, please!")

divide(8, 0)

# Example 2 Specifying exception classes use __str__
class NotInBoundsError(Exception):
    def __str__(self):
        return "Wrong!"

def check_num(num):
    try:
        if not 200 < num < 335:
            raise NotInBoundsError
    except NotInBoundsError as err:
        print(err)

check_num(34)

# Example 3 Specifying exception classes use __init__    
class LessThanFiveHundredError(Exception):
    def __init__(self, num):
        self.message = f"The integer {num} is below 500!"
        super().__init__(self.message)

def check_500(num):
    try:
        if num < 500:
            raise LessThanFiveHundredError(num)
        else:
            print(num)
    except LessThanFiveHundredError as err:
        print(err)

check_500(78)

# ----------------- Assert ------------------- #
try:
    word = input('Enter a word ')
    messaga = "'cat' is a wrong word!"
    assert word != 'cat', messaga
    print(f'Your word is {word}')
except AssertionError as err:
    print(err)

def test_mark(i):
    messaga = f'The student got a bad mark {i}!'
    assert i > 60, messaga
    return i

print(test_mark(64))
try:
    print(test_mark(54))
except AssertionError as err:
    print(err)

# ----------------- Test User Input ------------------- #
while True:
    try:
        your_int = int(input("Enter an integer number between 25 and 50 (inclusively): "))
        if 25 <= your_int <= 50:  # border values are now included
            print(your_int, "is the right number!")
            break
        else:
            print(your_int, "is the wrong number! Try again!")
    except ValueError:
        print("Your input is not an integer! Try again!")

# ----------------- Loop Control Statement ------------------- #
pets = ['dog', 'cat', 'parrot']
for pet in pets:
    if pet == 'dog':
        continue
    print(pet) # cat parrot

# ----------------- Write Recursion in Python ------------------- #
def recursive_factorial(n):
    # base case
    if n == 0:
        return 1
    # recursive case
    else:
        return n * recursive_factorial(n - 1)
print(recursive_factorial(3)) # 6

def func(x, y):
    # base case
    if x < y:
        return x
    # recursive case
    else:
        return func(x - y, y)
print(func(20, 5))  # 0

