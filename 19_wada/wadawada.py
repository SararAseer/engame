Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> def union(a,b):
	return [[x] for x in a for y in b if x==y]

>>> union([21,12],[3,4,12])
[[12]]
>>> def union(a,b):
	return [[x,y] for x in a for y in b]

>>> union([21,12],[3,4,12])
[[21, 3], [21, 4], [21, 12], [12, 3], [12, 4], [12, 12]]
>>> def union(a,b):
	return [x,y for x in a for y in b]
SyntaxError: invalid syntax
>>> 
>>> def union(a,b):
	return [z for z in [x for x in a]+[y for y in b]if z not in a]

>>> union([21,12],[3,4,12])
[3, 4]
>>> def union(a,b):
	return [z for z in [x for x in a]+[y for y in b]if z not in a && b]
SyntaxError: invalid syntax
>>> def union(a,b):
	return [z for z in [x for x in a]+[y for y in b]if z not in a]+[z for z in [x for x in a]+[y for y in b]if z  in b]

>>> union([21,12],[3,4,12])
[3, 4, 12, 3, 4, 12]
>>> def union(a,b):
	return [z for z in [x for x in a]+[y for y in b]if z not in a]+[z for z in [x for x in a]+[y for y in b]if z  not in b]

>>> union([21,12],[3,4,12])
[3, 4, 21]
>>> def union(a,b):
	return [z for z in [x for x in a]+[y for y in b]if z not  a]+[z for z in [x for x in a]+[y for y in b]if z  not in b]
SyntaxError: invalid syntax
def union(a,b):
	return [z for z in [x for x in a]+[y for y in b]if z not  a]+[z for z in [x for x in a]+[y for y in b]if z  not in b]
>>> def union(a,b):
	return [z for z in [x for x in a]+[y for y in b]if z in  a]+[z for z in [x for x in a]+[y for y in b]if z  not in b]

>>> union([21,12],[3,4,12])
[21, 12, 12, 21]
>>> def union(a,b):
	return [z for z in [x for x in a]+[y for y in b]]+[z for z in [x for x in a]+[y for y in b]if z  not in b]

>>> def union(a,b):
	return [z for z in [x for x in a]+[y for y in b]if z not in a && b]
SyntaxError: invalid syntax
>>> def union(a,b):
	return [z for z in [x for x in a]+[y for y in b]if y not in a]

>>> union([21,12],[3,4,12])
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    union([21,12],[3,4,12])
  File "<pyshell#27>", line 2, in union
    return [z for z in [x for x in a]+[y for y in b]if y not in a]
  File "<pyshell#27>", line 2, in <listcomp>
    return [z for z in [x for x in a]+[y for y in b]if y not in a]
NameError: name 'y' is not defined
>>> def union(a,b):
	return [z for z in [x for x in a]+[y for y in b]if y not in a]
def union(a,b):
	return [z for z in [x for x in a]+[y for y in b]if z not in a and b]
SyntaxError: invalid syntax
>>> def union(a,b):
	return [z for z in [x for x in a]+[y for y in b]if z not in a and b]

>>> union([21,12],[3,4,12])
[3, 4]
>>> def union(a,b):
	return [z for z in [x for x in a]+[y for y in b]if z not in a and b]+[z for z in [x for x in a]+[y for y in b]if z in a and b]

>>> union([21,12],[3,4,12])
[3, 4, 21, 12, 12]
>>> def union(a,b):
	return [z for z in [x for x in a]+[y for y in b]if z not in a and b]

	
>>> union([21,12],[3,4,12])
[3, 4]
>>> def union(a,b):
	return [z for z in [x for x in a]+[y for y in b]]

>>> union([21,12],[3,4,12])
[21, 12, 3, 4, 12]
>>> def union(a,b):
	return [x for x in a for y in b if x==y]

>>> union([21,12],[3,4,12])
[12]
>>> def union(a,b):
	return [x for x in a for y in b if x==y]+[x for x in a for y in b if x!=y]

>>> union([21,12],[3,4,12])
[12, 21, 21, 21, 12, 12]
>>> def union(a,b):
	return [x for x in a for y in b if x==y]+[y for y in b for x in a if x!=y]

>>> union([21,12],[3,4,12])
[12, 3, 3, 4, 4, 12]

>>> def union(a,b):
	return [x for x in a for y in b if x==y]+[y for y in b if y not in a]

>>> union([21,12],[3,4,12])
[12, 3, 4]
>>> def union(a,b):
	return [x for x in a for y in b if x==y]+[y for y in b if y not in a]+[x for x in a if y not in b]

>>> union([21,12],[3,4,12])
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    union([21,12],[3,4,12])
  File "<pyshell#56>", line 2, in union
    return [x for x in a for y in b if x==y]+[y for y in b if y not in a]+[x for x in a if y not in b]
  File "<pyshell#56>", line 2, in <listcomp>
    return [x for x in a for y in b if x==y]+[y for y in b if y not in a]+[x for x in a if y not in b]
NameError: name 'y' is not defined
>>> def union(a,b):
	return [x for x in a for y in b if x==y]+[y for y in b if y not in a]+[x for x in a if x not in b]

>>> union([21,12],[3,4,12])
[12, 3, 4, 21]
>>> def cartpord(a,b):
	return [[x,y] for x in a for y in b]

>>> cartpod([1,2],[red,white])
Traceback (most recent call last):

  File "<pyshell#64>", line 1, in <module>
    cartpod([1,2],[red,white])
NameError: name 'cartpod' is not defined
>>> cartpord([1,2],[red,white])
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    cartpord([1,2],[red,white])
NameError: name 'red' is not defined

>>> cartpord([1,2],["red","white"])
[[1, 'red'], [1, 'white'], [2, 'red'], [2, 'white']]

>>> def intersec(a,b):
	return [x for x in a for y in b if a==b]

>>> union([21,12],[3,4,12])
[12, 3, 4, 21]
>>> intersec([21,12],[3,4,12])
[]

>>> def intersec(a,b):
	return [x for x in a for y in b if x==y]

>>> intersec([21,12],[3,4,12])
[12]
>>> def symdif(a,b):
	return [x for x in a for y in b if x!=y]

>>> intersec([21,12],[3,4,12])
[12]
>>> symdif([21,12],[3,4,12])
[21, 21, 21, 12, 12]

>>> def symdif(a,b):
	return [x for x in a if x not in b]

>>> [21, 21, 21, 12, 12][21, 21, 21, 12, 12]
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    [21, 21, 21, 12, 12][21, 21, 21, 12, 12]

TypeError: list indices must be integers or slices, not tuple
>>> symdif([21,12],[3,4,12])
[21]
>>> [21, 21, 21, 12, 12][21, 21, 21, 12, 12]
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    [21, 21, 21, 12, 12][21, 21, 21, 12, 12]
TypeError: list indices must be integers or slices, not tuple
>>> def symdif(a,b):
	return [x for x in a if x not in b] +[x for x in b if x not in a]

>>> symdif([21,12],[3,4,12])
[21, 3, 4]
>>> def setfifa(a,b):
	return [x for x in a if a not in b]

>>> symdif([21,12],[3,4,12])
[21, 3, 4]
>>> def setfifa(a,b):
	return [x for x in a if a not in b]

>>> setfifa([21,12],[3,4,12])
[21, 12]

>>> def setfifa(a,b):
	return [x for x in a if x not in b]

>>> setfifa([21,12],[3,4,12])
[21]
>>> ##wda
>>> def union(a,b):
	return [x for x in a for y in b if x==y]+[y for y in b if y not in a]+[x for x in a if x not in b]

>>> def cartpord(a,b):
	return [[x,y] for x in a for y in b]

>>> def intersec(a,b):
	return [x for x in a for y in b if x==y]

>>> def symdif(a,b):
	return [x for x in a if x not in b] +[x for x in b if x not in a]

>>> def setfifa(a,b):
	return [x for x in a if x not in b]

>>> 
