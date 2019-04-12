Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> nums=[range(8)]
>>> nums
[range(0, 8)]
>>> print(nums)
[range(0, 8)]

>>> for x in range(len(nums)):
	print(nums[x])

	
range(0, 8)
>>> [x for x in range(9)]
[0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> print(x for x in range(9))
<generator object <genexpr> at 0x110741c78>
>>> [x for x in p]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    [x for x in p]
NameError: name 'p' is not defined
>>> [x for x in 'p']
['p']
>>> [x for x in '123']
['1', '2', '3']
>>> p="dsadasdsada"
>>> L="ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
SyntaxError: invalid syntax
>>> L="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
>>> p="FaaraAwqwFCQJHBQF"
>>> [x for x in p if x in L]
['F', 'A', 'F', 'C', 'Q', 'J', 'H', 'B', 'Q', 'F']
>>> [1 if x for x in p x in L]
SyntaxError: invalid syntax
>>> 
=============================== RESTART: Shell ===============================
>>> def ps(pass):

        
	
SyntaxError: invalid syntax
>>> def ps(pas):
	b="abcdefghigklmnopqrstuvwxyz"
	c=b.Upper()

	
>>> "f".Upper()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    "f".Upper()
AttributeError: 'str' object has no attribute 'Upper'
>>> "f".upper()
'F'
>>> def ps(pas):
	count=0
	b="abcdefghigklmnopqrstuvwxyz"
	c=b.upper()
	x for x in pas if x in b count+=1
	
SyntaxError: invalid syntax
>>> def ps(pas):
	count=0
	b="abcdefghigklmnopqrstuvwxyz"
	c=b.upper()
	[x for x in pas if x in b count+=1]
	
SyntaxError: invalid syntax
>>> def ps(pas):
	count=0
	b="abcdefghigklmnopqrstuvwxyz"
	c=b.upper()
	[x for x in pas if x in b]

	
>>> def ps(pas):
	count=0
	b="abcdefghigklmnopqrstuvwxyz"
	c=b.upper()
	[x for x in pas if x in b:]
	
SyntaxError: invalid syntax
>>> def ps(pas):
	count=0
	b="abcdefghigklmnopqrstuvwxyz"
	c=b.upper()
	res=[x for x in pas if x in b || c]
	print res
	
SyntaxError: invalid syntax
>>> 
>>> def ps(pas):
	count=0
	b="abcdefghigklmnopqrstuvwxyz"
	c=b.upper()
	res=[x for x in pas if x in b or c]
	print res
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(res)?
>>> 
>>> def ps(pas):
	count=0
	b="abcdefghigklmnopqrstuvwxyz"
	c=b.upper()
	res=[x for x in pas if x in b or c]
	print(res)

	
>>> ps("dONG")
['d', 'O', 'N', 'G']
>>> ps("dObG@")
['d', 'O', 'b', 'G', '@']
>>> def ps(pas):
	count=0
	b="abcdefghigklmnopqrstuvwxyz"
	c=b.upper()
	res=[x for x in pas if x in b]
	print(res)

	
>>> ps("dONG")
['d']
>>> 	b="abcdefghigklmnopqrstuvwxyz"

SyntaxError: unexpected indent
>>> b="abcdefghigklmnopqrstuvwxyz"
>>> c=b.upper()
>>> print(c)
ABCDEFGHIGKLMNOPQRSTUVWXYZ
>>> def ps(pas):
	count=0
	b="abcdefghigklmnopqrstuvwxyz"
	c=b.upper()
	res=[x for x in pas if x in b]
	res.append([x for x in pas if x in c])
	print(res)

	
>>> ps("did")
['d', 'i', 'd', []]
>>> def ps(pas):
	count=0
	b="abcdefghigklmnopqrstuvwxyz"
	c=b.upper()
	res=[x for x in pas if x in b]
	res=res+[x for x in pas if x in c]
	print(res)

	
>>> ps("did")
['d', 'i', 'd']
>>> ps("did2")
['d', 'i', 'd']
>>> ps("did2D")
['d', 'i', 'd', 'D']
>>> def ps2(pas):
	boold=[0,0,0]
	for x in pas:
		if x>=65 and <=90:
			
SyntaxError: invalid syntax
>>> def ps2(pas):
	boold=[0,0,0]
	for x in pas:
		if x>=65 and x<=90:
			boold[0]=1

				
>>> def ps2(pas):
	boold=[0,0,0,0]
	count =0
	for x in pas:
		if x>=65 and x<=90:
			count+=1
		elif x>=97 and x<=122:
			count+=1
		elif isinstance(x, int):
			count+=1
		else
		
SyntaxError: invalid syntax
>>> def ps2(pas):
	boold=[0,0,0,0]
	count =0
	for x in pas:
		if x>=65 and x<=90 and boold[0]==0:
			count+=1
			boold[0]=1
		elif x>=97 and x<=122 and boold[1]==0:
			count+=1
			boold[1]=1
		elif isinstance(x, int) and boold[2]==0:
			count+=1
			boold[2]=1
		elif boold[3]==0:
			count+=1
			boold[3]=1
	return count

>>> print(pst("hello"))
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    print(pst("hello"))
NameError: name 'pst' is not defined
>>> print(ps2("hello"))
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    print(ps2("hello"))
  File "<pyshell#71>", line 5, in ps2
    if x>=65 and x<=90 and boold[0]==0:
TypeError: '>=' not supported between instances of 'str' and 'int'
>>> def ps2(pas):
	boold=[0,0,0,0]
	count =0
	for x in pas:
		a=ord(x)
		if a>=65 and a<=90 and boold[0]==0:
			count+=1
			boold[0]=1
		elif a>=97 and a<=122 and boold[1]==0:
			count+=1
			boold[1]=1
		elif isinstance(x, int) and boold[2]==0:
			count+=1
			boold[2]=1
		elif boold[3]==0:
			count+=1
			boold[3]=1
	return count

>>> print(ps2("hello"))
2
>>> def ps2(pas):
	boold=[0,0,0,0]
	count =0
	for x in pas:
		a=ord(x)
		if a>=65 and a<=90 and boold[0]==0:
			count+=1
			boold[0]=1
		elif a>=97 and a<=122 and boold[1]==0:
			count+=1
			boold[1]=1
		elif isinstance(x, int) and boold[2]==0:
			count+=1
			boold[2]=1
		elif (((a<65 and !isinstance(x, int)) or(a>90 and a<97) or(a>122))and boold[3]==0):
			count+=1
			boold[3]=1
	return count
SyntaxError: invalid syntax
>>> 
>>> def ps2(pas):
	boold=[0,0,0,0]
	count =0
	for x in pas:
		a=ord(x)
		if a>=65 and a<=90 and boold[0]==0:
			count+=1
			boold[0]=1
		elif a>=97 and a<=122 and boold[1]==0:
			count+=1
			boold[1]=1
		elif isinstance(x, int) and boold[2]==0:
			count+=1
			boold[2]=1
		elif (((a<65 and isinstance(x, int)==False) or(a>90 and a<97) or(a>122))and boold[3]==0):
			count+=1
			boold[3]=1
	return count

>>> print(ps2("hello"))
1
>>> print(ps2("hello2"))
2
>>> print(ps2("hello2F"))
3
>>> print(ps2("hello2F@"))
3
>>> print(ps2("hello2F@!"))
3
>>> def ps2(pas):
	boold=[0,0,0,0]
	spec="~!@#$%^&*()_+-={[}]|\:;"'<,>.?/"
	count =0
	for x in pas:
		a=ord(x)
		if a>=65 and a<=90 and boold[0]==0:
			count+=1
			boold[0]=1
		elif a>=97 and a<=122 and boold[1]==0:
			count+=1
			boold[1]=1
		elif isinstance(x, int) and boold[2]==0:
			count+=1
			boold[2]=1
		elif (x in spec and boold[3]==0):
			count+=1
			boold[3]=1
	return count
SyntaxError: EOL while scanning string literal
>>> def ps2(pas):
	boold=[0,0,0,0]
	spec='''~!@#$%^&*()_+-={[}]|\:;""''<,>.?/'''
	count =0
	for x in pas:
		a=ord(x)
		if a>=65 and a<=90 and boold[0]==0:
			count+=1
			boold[0]=1
		elif a>=97 and a<=122 and boold[1]==0:
			count+=1
			boold[1]=1
		elif isinstance(x, int) and boold[2]==0:
			count+=1
			boold[2]=1
		elif (x in spec and boold[3]==0):
			count+=1
			boold[3]=1
	return count

>>> print(ps2("hello2F@!"))
3
>>> def ps2(pas):
	boold=[0,0,0,0]
	spec='''~!@#$%^&*()_+-={[}]|\:;""''<,>.?/'''
	count =0
	for x in pas:
		a=ord(x)
		if a>=65 and a<=90 and boold[0]==0:
			count+=1
			boold[0]=1
		elif a>=97 and a<=122 and boold[1]==0:
			count+=1
			boold[1]=1
		elif isinstance(x, int) and boold[2]==0:
			count+=1
			boold[2]=1
		elif (x in spec and boold[3]==0):
			count+=1
			boold[3]=1
	print(boold)
	return count

>>> print(ps2("hello2F@!"))
[1, 1, 0, 1]
3
>>> isinstance("2", int)
False
>>> def ps2(pas):
	boold=[0,0,0,0]
	spec='''~!@#$%^&*()_+-={[}]|\:;""''<,>.?/'''
	count =0
	for x in pas:
		try: 
			if isinstance(int(x), int) && boold[2]==0:
			boold[2]==1
			count+=1;
		except ValueError:
			
		a=ord(x)
		if a>=65 and a<=90 and boold[0]==0:
			count+=1
			boold[0]=1
		elif a>=97 and a<=122 and boold[1]==0:
			count+=1
			boold[1]=1
		elif (x in spec and boold[3]==0):
			count+=1
			boold[3]=1
	print(boold)	
	return count
SyntaxError: invalid syntax
>>> 
>>> def ps2(pas):
	boold=[0,0,0,0]
	spec='''~!@#$%^&*()_+-={[}]|\:;""''<,>.?/'''
	count =0
	for x in pas:
		try:
			if isinstance(int(x), int) and boold[2]==0:
			boold[2]==1
			count+=1;
		except ValueError:

		a=ord(x)
		if a>=65 and a<=90 and boold[0]==0:
			count+=1
			boold[0]=1
		elif a>=97 and a<=122 and boold[1]==0:
			count+=1
			boold[1]=1
		elif (x in spec and boold[3]==0):
			count+=1
			boold[3]=1
	print(boold)
	return count
SyntaxError: expected an indented block
>>> 
>>> def ps2(pas):
	boold=[0,0,0,0]
	spec='''~!@#$%^&*()_+-={[}]|\:;""''<,>.?/'''
	count =0
	for x in pas:
		try:
			if isinstance(int(x), int) and boold[2]==0:
			boold[2]=1
			count+=1;
		except ValueError:

		a=ord(x)
		if a>=65 and a<=90 and boold[0]==0:
			count+=1
			boold[0]=1
		elif a>=97 and a<=122 and boold[1]==0:
			count+=1
			boold[1]=1
		elif (x in spec and boold[3]==0):
			count+=1
			boold[3]=1
	print(boold)
	return count
SyntaxError: expected an indented block
>>> def ps2(pas):
	boold=[0,0,0,0]
	spec='''~!@#$%^&*()_+-={[}]|\:;""''<,>.?/'''
	count =0
	for x in pas:
		try:
			if isinstance(int(x), int) and boold[2]==0:
				boold[2]=1
				count+=1;
		except ValueError:

		a=ord(x)
		if a>=65 and a<=90 and boold[0]==0:
			count+=1
			boold[0]=1
		elif a>=97 and a<=122 and boold[1]==0:
			count+=1
			boold[1]=1
		elif (x in spec and boold[3]==0):
			count+=1
			boold[3]=1
	print(boold)
	return count
SyntaxError: expected an indented block
>>> def ps2(pas):
	boold=[0,0,0,0]
	spec='''~!@#$%^&*()_+-={[}]|\:;""''<,>.?/'''
	count =0
	for x in pas:
		try:
			if isinstance(int(x), int) and boold[2]==0:
				boold[2]=1
				count+=1;
		except ValueError:
			print()
		a=ord(x)
		if a>=65 and a<=90 and boold[0]==0:
			count+=1
			boold[0]=1
		elif a>=97 and a<=122 and boold[1]==0:
			count+=1
			boold[1]=1
		elif (x in spec and boold[3]==0):
			count+=1
			boold[3]=1
	print(boold)
	return count

>>> print(ps2("hello2F@!"))








[1, 1, 1, 1]
4
>>> 
