### Python morsels repo for my challanges
## First problem: Circle.py
This week I want you to make a class that represents a circle.

The circle should have a radius, a diameter, and an area. It should also have a nice string representation.

For example:

>>> c = Circle(5)
>>> c
Circle(5)
>>> c.radius
5
>>> c.diameter
10
>>> c.area
78.53981633974483
Additionally the radius should default to 1 if no radius is specified when you create your circle:

>>> c = Circle()
>>> c.radius
1
>>> c.diameter
2
There are three bonuses for this exercise.

Bonus 1

For the first bonus, make sure when the radius of your class changes that the diameter and area both change as well: ✔️

>>> c = Circle(2)
>>> c.radius = 1
>>> c.diameter
2
>>> c.area
3.141592653589793
>>> c
Circle(1)
If you get stuck on this bonus, make sure to check the hints.

Bonus 2

For the second bonus, make sure you can set the diameter attribute in your class and the radius will update accordingly. Also make sure also that you cannot set the area (setting area should raise an AttributeError): ✔️

>>> c = Circle(1)
>>> c.diameter = 4
>>> c.radius
2.0
>>> c.area = 45.678
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "circle.py", line 16, in radius
AttributeError: can't set attribute
Bonus 3

For the third bonus, make sure your radius cannot be set to a negative number. You should raise a ValueError exception with the error message "Radius cannot be negative". ✔️

>>> c = Circle(5)
>>> c.radius = 3
>>> c.radius = -2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "circle.py", line 27, in radius
    raise ValueError("Radius cannot be negative")
ValueError: Radius cannot be negative
>>> c = Circle (-10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "circle.py", line 27, in radius
    raise ValueError("Radius cannot be negative")
ValueError: Radius cannot be negative
This means that diameter cannot be negative either (and setting diameter to a negative number should also raise a ValueError).

## Second problem
I'd like you to write a function that accepts two lists-of-lists of numbers and returns one list-of-lists with each of the corresponding numbers in the two given lists-of-lists added together.

It should work something like this:

>>> matrix1 = [[1, -2], [-3, 4]]
>>> matrix2 = [[2, -1], [0, -1]]
>>> add(matrix1, matrix2)
[[3, -3], [-3, 3]]
>>> matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
>>> matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
>>> add(matrix1, matrix2)
[[2, -1, 3], [-3, 3, -3], [5, -6, 7]]
Try to solve this exercise without using any third-party libraries (without using pandas for example).

Before attempting any bonuses, I'd like you to put some effort into figuring out the clearest and most idiomatic way to solve this problem. If you're using indexes to loop, take a look at the first hint.

There are two bonuses this week.

Bonus 1

For the first bonus, modify your add function to accept and "add" any number of lists-of-lists. ✔️

>>> matrix1 = [[1, 9], [7, 3]]
>>> matrix2 = [[5, -4], [3, 3]]
>>> matrix3 = [[2, 3], [-3, 1]]
>>> add(matrix1, matrix2, matrix3)
[[8, 8], [7, 7]]
Bonus 2

For the second bonus, make sure your add function raises a ValueError if the given lists-of-lists aren't all the same shape. ✔️

>>> add([[1, 9], [7, 3]], [[1, 2], [3]])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "add.py", line 10, in add
    raise ValueError("Given matrices are not the same size.")
ValueError: Given matrices are not the same size.