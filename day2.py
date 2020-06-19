Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Name = input()
Chand
>>> Age = int(input())
19
>>> CGPA = float(input())
8.94
>>> print("My name is " + Name + " I'm " + Age + "yr old CGPA is "+ CGPA)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print("My name is " + Name + " I'm " + Age + "yr old CGPA is "+ CGPA)
TypeError: can only concatenate str (not "int") to str
>>> print("My name is " + Name + " I'm " + str(Age) + "yr old CGPA is "+ str(CGPA))
My name is Chand I'm 19yr old CGPA is 8.94
>>> # printf("MArks %d",m)
>>> print("My name is {} I'm {} yr old CGPA is {}".format(Name, Age, CGPA))
My name is Chand I'm 19 yr old CGPA is 8.94
>>> print("My name is {} I'm {} yr old CGPA is {}".format( Age,Name, CGPA))
My name is 19 I'm Chand yr old CGPA is 8.94
>>> lst = [2,3,56,09,63]
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> lst = [2,3,56,9,63]
>>> lst[2]
56
>>> lst[3] = 90
>>> print(lst)
[2, 3, 56, 90, 63]
>>> lst.append(45)
>>> print(lst)
[2, 3, 56, 90, 63, 45]
>>> 
>>> 


>>> 

>>> 

>>> 
>>> lst.insert(3, 68)
>>> print(lst)
[2, 3, 56, 68, 90, 63, 45]
>>> lst.pop()
45
>>> print(lst)
[2, 3, 56, 68, 90, 63]
>>> lst.remove(3)
>>> print(lst)
[2, 56, 68, 90, 63]
>>> lst.extend([3,5,6,8,9,6,6,5])
>>> print(lst)
[2, 56, 68, 90, 63, 3, 5, 6, 8, 9, 6, 6, 5]
>>> min(lst)
2
>>> max(lst)
90
>>> lst.remove(5)
>>> print(lst)
[2, 56, 68, 90, 63, 3, 6, 8, 9, 6, 6, 5]
>>> lst.index(8)
7
>>> lst.index(90)
3
>>> min(lst)
2
>>> max(lst)
90
>>> sum(lst)
322
>>> lst.count(6)
3
>>> lst.count(5)
1
>>> lst.count(7)
0
>>> new_lst = lst.copy()
>>> print(new_lst)
[2, 56, 68, 90, 63, 3, 6, 8, 9, 6, 6, 5]
>>> lst.sort()
>>> new_lst = lst.copy()
>>> lst.append(6)
>>> print(new_lst)
[2, 3, 5, 6, 6, 6, 8, 9, 56, 63, 68, 90]
>>> print(lst)
[2, 3, 5, 6, 6, 6, 8, 9, 56, 63, 68, 90, 6]
>>> lst.sort()
>>> print(lst)
[2, 3, 5, 6, 6, 6, 6, 8, 9, 56, 63, 68, 90]
>>> lst.reverse()
>>> print(lst)
[90, 68, 63, 56, 9, 8, 6, 6, 6, 6, 5, 3, 2]
>>> lst = [2,44,21,0,86]
>>> print(lst.reverse())
None
>>> lst.reverse()
>>> print(lst)
[2, 44, 21, 0, 86]
>>> lst.reverse()
>>> print(lst)
[86, 0, 21, 44, 2]
>>> lst.clear()
>>> print(lst)
[]
>>> lst = [4,6,7,8,9,6,5]
>>> del lst[2:5]
>>> print(lst)
[4, 6, 6, 5]
>>> new = ["Abdsd", "afhkjhf", 9]
>>> # nested list
>>> nest = [lst, new]
>>> print(nest)
[[4, 6, 6, 5], ['Abdsd', 'afhkjhf', 9]]
>>> lst.index(9)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    lst.index(9)
ValueError: 9 is not in list
>>> lst[1].index(9)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    lst[1].index(9)
AttributeError: 'int' object has no attribute 'index'
>>> lst[1][2]
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    lst[1][2]
TypeError: 'int' object is not subscriptable
>>> nest[1].index(9)
2
>>> nest[1][2]
9
>>> lst.index(6)
1
>>> tup = (2,4,5,3,2,5)
>>> print(tup)
(2, 4, 5, 3, 2, 5)
>>> tup.count(5)
2
>>> tup.index(4)
1
>>> tup.index(5)
2
>>> print(tup[2])
5
>>> tup[2] = 6
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    tup[2] = 6
TypeError: 'tuple' object does not support item assignment
>>> # tuple immutable
>>> # list mutable
>>> # set
>>> st = {2,6,4,7,8,2,6}
>>> print(st)
{2, 4, 6, 7, 8}
>>> print(st)
{2, 4, 6, 7, 8}
>>> st[2] = 3
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    st[2] = 3
TypeError: 'set' object does not support item assignment
>>> st[3]
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    st[3]
TypeError: 'set' object is not subscriptable
>>> # List - Mutable
>>> # Tuple and Set - Immmutable
>>> 
