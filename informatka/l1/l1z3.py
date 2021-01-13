Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> r=5
>>> pi=3.1415
>>> v=4/3*pi*r^3
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    v=4/3*pi*r^3
TypeError: unsupported operand type(s) for ^: 'float' and 'int'
>>> v=4/3*pi*r^3
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    v=4/3*pi*r^3
TypeError: unsupported operand type(s) for ^: 'float' and 'int'
>>> 
>>> v=4/3*pi*r*r*r
>>> print(v)
523.5833333333333
>>> 