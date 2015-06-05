#! /usr/bin/python3

# This program calulates the area, circumference and diameter of a circle based on it's radius

radius = float(input('Enter the radius of your circle (cm) to work out its diameter, circumference and area: '))

circumference = 2 * 3.14 * radius
area = 3.14 * radius * radius
diameter = radius * 2

print('Diameter: ' + str(diameter) + 'cm')
print('Circumference: ' + str(circumference) + 'cm')
print('Area: ' + str(area) + 'cm2')
