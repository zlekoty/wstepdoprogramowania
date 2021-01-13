Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> szer = 13 wys = 12.0 znak = ’.’
SyntaxError: invalid syntax
>>> szer = 13 wys = 12.0 znak = ’.’
SyntaxError: invalid syntax
>>> wys = 12.0
>>> znak = ’.’
SyntaxError: invalid character in identifier
>>> szer = 13
>>> znak = '.'
>>> szer/2
6.5
>>> szer/2.0
6.5
>>> wys/3
4.0
>>> znak*5
'.....'
>>> znak+5
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    znak+5
TypeError: can only concatenate str (not "int") to str
>>> s='12'
>>> s*5
'1212121212'
>>> s+5
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    s+5
TypeError: can only concatenate str (not "int") to str
>>> 