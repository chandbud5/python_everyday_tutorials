Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2+3
5
>>> 2-3
-1
>>> 2/3
0.6666666666666666
>>> 3//2
1
>>> 9%4
1
>>> 3**2
9
>>> 3*5
15
>>> 2+=
SyntaxError: invalid syntax
>>> 2+=1
SyntaxError: cannot assign to literal
>>> "Hello World"
'Hello World'
>>> "Hello " + "World"
'Hello World'
>>> 10 * "Chand"
'ChandChandChandChandChandChandChandChandChandChand'
>>> print("Hello world")
Hello world
>>> print('Hello')
Hello
>>> print("Chand's")
Chand's
>>> print('Chand's "LAptop"')
      
SyntaxError: invalid syntax
>>> print("Chand\"s")
Chand"s
>>> print(r"Chand's "Laptop"")
SyntaxError: invalid syntax
>>> print(r,"Chand's "Laptop"")
SyntaxError: invalid syntax
>>> print(r"Chand's")
Chand's
>>> print(r'"lapro"')
"lapro"
>>> print("Laptop is of \telusko")
Laptop is of 	elusko
>>> print("name is \navin")
name is 
avin
>>> print("\title")
	itle
>>> print("\\title")
\title
>>> print(len("chand"))
5
>>> print(len("Chand Bud"))
9
>>> a = 9
>>> print(a)
9
>>> b = a + 5
>>> print(b)
14
>>> 89+6+5
100
>>> x =8
>>> x += 1
>>> print(x)
9
>>> x *= 3
>>> print(x)
27
>>> x -=1
>>> print(x)
26
>>> print(x /= 2)
SyntaxError: invalid syntax
>>> x /= 2
>>> print(x)
13.0
>>>  print("Hellop")
 
SyntaxError: unexpected indent
>>> print(x+=2)
SyntaxError: invalid syntax
>>> a = "chand"
>>> print(a)
chand
>>> a*10
'chandchandchandchandchandchandchandchandchandchand'

>>> print = 10
>>> print(print)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    print(print)
TypeError: 'int' object is not callable
>>> # int
>>> # float
>>> # string
>>> # bool
>>> # long

>>> type(a)
<class 'str'>
>>> type('a')
<class 'str'>
>>> type(4)
<class 'int'>
>>> type(5.4)
<class 'float'>
\
>>> boolean
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    boolean
NameError: name 'boolean' is not defined
>>> s = True
>>> type(s)
<class 'bool'>
>>> x = 5.8
>>> type(x)
<class 'float'>
>>> int(x)
5
>>> type(x)
<class 'float'>
>>> float(5)
5.0
>>> x = True
>>> int(x)
1
>>> _ + 4
5
>>> # immutable
>>> # mutable
>>> n =  "Chand"
>>> n[1:4]
'han'
>>> n[2:]
'and'
>>> n[-1:-3]
''
>>> n[-3:-1]
'an'
>>> n[-1:3]
''
>>> n[-3:5]
'and'
>>> n[2]
'a'
>>> n[2] = "b"
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    n[2] = "b"
TypeError: 'str' object does not support item assignment
>>> n[2] = 'a'
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    n[2] = 'a'
TypeError: 'str' object does not support item assignment
>>> n = ("chand")
>>> n[0]
'c'
>>> n[3] = x
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    n[3] = x
TypeError: 'str' object does not support item assignment
>>> 
