##################
### Question 1 ###
##################


def find_element(arr, x):
    for element in arr:
        if element == x:
            return True
    return False


animal_list = ["Lion", "Elephant", "Tiger", "Giraffe",
               "Zebra", "Panda", "Kangaroo", "Penguin"]

print("Question 1:", find_element(animal_list, "Penguin"))

##################
### Question 2 ###
##################


def bubble_sort(items):
    """ Implementation of bubble sort."""
    for i in range(len(items)):
        for j in range(len(items)-1-i):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
    return items


print("Question 2:", bubble_sort([64, 34, 25, 12, 22, 11, 90]))

##################
### Question 3 ###
##################


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount


account = BankAccount(100)
account.deposit(50)
print("Question 3:", account.balance)

##################
### Question 4 ###
##################


def r(s):
    if len(s) == 0:
        return s
    return r(s[1:]) + s[0]


p = "programming"
print("Question 4:", r(p))

##################
### Question 5 ###
##################

numbers = [-2, 5, -9, 8, -1, 10]
result = filter(lambda x: x >= 0, numbers)
print("Question 5:", list(result))

##################
### Question 6 ###
##################


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2 * 3.14159 * self.radius


print("Question 6:", Circle(3).circumference())

##################
### Question 7 ###
##################


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height


rect = Rectangle(3, 4)
print("Question 7:", "Area:", rect.area(), "Perimeter:", rect.perimeter())

##################
### Question 8 ###
##################

numbers = [1, 2, 3, 4, 5]
result = map(lambda x: x**2, numbers)
print("Question 8:", list(result))

##################
### Question 9 ###
##################


class ExampleClass:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value
    
print("Question 9: Spacing in the __init__ arguments")

###################
### Question 10 ###
###################


class Shape:
    def __init__(self, name):
        self.name = name


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Square(Shape):
    def __init__(self, side):
        super().__init__("Square")
        self.side = side

    def area(self):
        return self.side * self.side


circle = Circle(3)
square = Square(4)
total_area = circle.area() + square.area()
print("Question 10: Total Area:", total_area)
