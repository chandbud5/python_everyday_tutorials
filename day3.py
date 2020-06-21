Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> lst = []
>>> lst.extend([6,7,8])
>>> s = {2,4,5,6,3,2,2}
>>> print(s)
{2, 3, 4, 5, 6}
>>> tup = (3l5,6,784)
SyntaxError: invalid syntax
>>> tup = (3,5,6,7,8)
>>> print(tup[3])
7
>>> # list
>>> # tuple
>>> # set
>>> lst.index(7)
1
>>> lst[2]
8
>>> lst.remove(6)
>>> print(lst)
[7, 8]
>>> # Dictionary
>>> names = {1:'Abc', 2:"def", 3:"ghi"}
>>> names[1]
'Abc'
>>> names.get(2)
'def'
>>> names.get(4, "Nathi value")
'Nathi value'
>>> names[4]
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    names[4]
KeyError: 4
>>> names.get(2, "nathi")
'def'
>>> names.fromkeys(2)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    names.fromkeys(2)
TypeError: 'int' object is not iterable
>>> # 3.7.
>>> names.keys()
dict_keys([1, 2, 3])
>>> names.items()
dict_items([(1, 'Abc'), (2, 'def'), (3, 'ghi')])
>>> # zip
>>> roll = [1,2,3,4]
>>> name = ["A", "B", "B", "D"]
>>> x = dict(zip(roll, name))
>>> print(x)
{1: 'A', 2: 'B', 3: 'B', 4: 'D'}
>>> y = dict(zip(name, roll))
>>> print(y)
{'A': 1, 'B': 3, 'D': 4}
>>> x[2] = "Chand"
>>> print(x)
{1: 'A', 2: 'Chand', 3: 'B', 4: 'D'}
>>> del x[2]
>>> print(x)
{1: 'A', 3: 'B', 4: 'D'}
>>> del lst[0:2]
>>> print(lst)
[]
>>> # Nested
>>> ide = {'C':'Turbo C', 'Java':['Netbeans', 'Eclipse'], 'python':{3.7:"Pycharm", 3.8:"VS code"}}
>>> print(ide)
{'C': 'Turbo C', 'Java': ['Netbeans', 'Eclipse'], 'python': {3.7: 'Pycharm', 3.8: 'VS code'}}
>>> print('C')
C
>>> print(ide('C'))
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    print(ide('C'))
TypeError: 'dict' object is not callable
>>> ide('C')
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    ide('C')
TypeError: 'dict' object is not callable
>>> ide("C")
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    ide("C")
TypeError: 'dict' object is not callable
>>> ide['C']
'Turbo C'
>>> ide['Java']
['Netbeans', 'Eclipse']
>>> ide['Java'][1]
'Eclipse'
>>> ide['python'][3.7]
'Pycharm'
>>> # ide - Integrated development environment
>>> ide['python']
{3.7: 'Pycharm', 3.8: 'VS code'}
>>> # OPerators
>>> # Arithmetic operator ->  +,-,*,/,//,**
>>> # %
>>> 3 // 2
1
>>> 2 ** 3
8
>>> 3/2
1.5
>>> # Relational, Logical
>>> # Logical - and, or, not
>>> 2 and 3
3
>>> i = 5
>>> # Relational < >, <=, >=
>>> i<=8
True
>>> i > 0
True
>>> i <2
False
>>> i == 3
False
>>> i == 5
True
>>> True and True
True
>>> 1 and 0
0
>>> # AND
>>> # 1 1 - 1
>>> # 1 0 - 0
>>> # 0 1 - 0
>>> # 0 0 - 0
>>> i = 7
>>> # OR
>>> # 1 1 - 1
>>> # 1 0 - 1
>>> # 0 1 - 1
>>> # 0 0 - 0
>>> i<5 and i<3
False
>>> i<5
False
>>> i<8 and i<6
False
>>> i>6 and i==8
False
>>> i<9 and i==7
True
>>> i>6 or i==8
True
>>> not i<6
True
>>> # NOT
>>> # 1 - 0
>>> # 0 - 1
>>> # Assignment - =
>>> a =5
>>> !a
SyntaxError: invalid syntax
>>> !True
SyntaxError: invalid syntax
>>> # Bitwise
>>> # &, |, ~, ^
>>> # pipe, tilt, cap
>>> # XOR
>>> # 1 1  0
>>> # 1 0  1
>>> # 0 1  1
>>> # 0 0  0
>>> 2 & 3
2
>>> # 2-010, 3-
>>> 5 or 9
5
>>> # above command is incorrect
>>> 5 | 9
13
>>> 7 | 9
15
>>> 6 ^ 9
15
>>> 4^2
6
>>> #7 & 8,	4 | 1, 	5^0
>>> 4 | 1
5
>>> 7&8
0
>>> 5^0
5
>>> # 4&12 , 7|0, 4^1
>>> 4&12
4
>>> 7|0
7
>>> 4^1
5
>>> ~5
-6
>>> # Arithmetic -->  +,-,*,/,//,**
>>> # Assignment -->  =
>>> # Relational -->  <, >, <=, >=, ==
>>> # Logical 	 -->  and, or, not
>>> # Unary 	 -->  -
>>> # BitWise 	 -->  &, |, ~, ^
>>> 
