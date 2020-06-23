Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 0b4
SyntaxError: invalid digit '4' in binary literal
>>> '0b4'
'0b4'
>>> # Number system conversion
>>> bin(9)
'0b1001'
>>> oct(7)
'0o7'
>>> oct(10)
'0o12'
>>> hex(96)
'0x60'
>>> '0b1001'
'0b1001'
>>> 0b1001
9
>>> 0o7
7
>>> 0x60
96
>>> x = 10
>>> id(x)
140717106698176
>>> id(x)
140717106698176
>>> y = x
>>> id(y)
140717106698176
>>> values = [2,3,4,5,6,67,7]
>>> id(values)
2247429596800
>>> values[0] = 5
>>> id(values)
2247429596800
>>> values = [4,3,2,3,5,6,67,7]
>>> id(values)
2247429595456
>>> values = [4,3,2,5,6,67,7]
>>> id(values)
2247429596608
>>> vals = values
>>> id(vals)
2247429596608
>>> print(vals)
[4, 3, 2, 5, 6, 67, 7]
>>> vals[2] = 100
>>> id(vals)
2247429596608
>>> print(vals)
[4, 3, 100, 5, 6, 67, 7]
>>> print(values)
[4, 3, 100, 5, 6, 67, 7]
>>> # Shallow copy
>>> # Deep Copy
>>> new = values.copy()
>>> id(new)
2247429596800
>>> new[2] = 2
>>> print(new)
[4, 3, 2, 5, 6, 67, 7]
>>> print(values)
[4, 3, 100, 5, 6, 67, 7]
>>> id(values)
2247429596608
>>> 
