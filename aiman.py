

import math

# Inputs from user
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))


sum_result = a + b + c
difference = a - b - c
product = a * b * c
average = sum_result / 3


print("Sum:", sum_result)
print("Difference:", difference)
print("Product:", product)
print("Average:", average)


base = float(input("Enter base of triangle: "))
height = float(input("Enter height of triangle: "))
triangle_area = 0.5 * base * height
print("Area of triangle:", triangle_area)


side = float(input("Enter side of square: "))
square_area = side * side
print("Area of square:", square_area)


radius = float(input("Enter radius of circle: "))
circle_area = math.pi * radius ** 2
print("Area of circle:", circle_area)


length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
rectangle_area = length * width
print("Area of rectangle:", rectangle_area)


x = input("Enter first value: ")
y = input("Enter second value: ")


x, y = y, x


print("After swapping:")
print("First value:", x)
print("Second value:", y)