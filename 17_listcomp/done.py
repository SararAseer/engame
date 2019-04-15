Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> def p1(s):
	return [str(x)+str(x) for x in range(s)]

>>> p1(4)
['00', '11', '22', '33']
>>> def p1(s):
	return [str(x)+str(x) for x in range(s)]

>>> 
>>> def p1(s):
	return [str(x*2)+str(x*2) for x in range(s)]

>>> p1(4)
['00', '22', '44', '66']
>>> p1(5)
['00', '22', '44', '66', '88']
>>> def p1(s):
	int i=0;
	
SyntaxError: invalid syntax
>>> def p1(s):
	int i=0
	
SyntaxError: invalid syntax
>>> def p1(s):
	res=[]
	i=0
	while(True):
		if (i%22 == 0)
		
SyntaxError: invalid syntax
>>> def p1(s):
	res=[]
	i=0
	while(True):
		if (i%22 == 0)
		
SyntaxError: invalid syntax
>>> def p1(s):
	res=[]
	i=0
	while(True):
		if (i%22 == 0):
			res.append(str(i))
		i+=22
	return res

>>> pls
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    pls
NameError: name 'pls' is not defined
>>> pl(4)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    pl(4)
NameError: name 'pl' is not defined
>>> p1(3)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    p1(3)
  File "<pyshell#26>", line 6, in p1
    res.append(str(i))
KeyboardInterrupt

>>> def p2(s):
	res=[]
	i=0
	k=0
	while(k<=s):
		if (i%22 == 0):
			res.append(str(i))
		i+=22
		k++1return res
		
SyntaxError: invalid syntax
>>> def p2(s):
	res=[]
	i=0
	k=0
	while(k<=s):
		if (i%22 == 0):
			res.append(str(i))
		i+=22
		k++1return res
		
SyntaxError: invalid syntax
>>> def p2(s):
	res=[]
	i=0
	k=0
	while(k<=s):
		if (i%22 == 0):
			res.append(str(i))
		i+=22
		k+=1
		return res

	
>>> def p1(s):
	return [str(x*2)+str(x*2) for x in range(s)]

>>> def p2(s):
	res=[]
	i=0
	k=0
	while(k<=s):
		if (i%22 == 0):
			res.append(str(i))
		i+=22
		k+=1
		return res

	
>>> p2(4)
['0']
>>> def p1(s):
	return [str(x*2)+str(x*2) for x in range(s)]def p2(s):
		res=[]
		i=0
		k=0
		while(k<=s):
			if (i%22 == 0):
				res.append(str(i))
			i+=22
			k+=1
			return res
		
SyntaxError: invalid syntax
>>> def p2(s):
	res=[]
	i=0
	k=0
	while(k<=s):
		res.append(str(i))
		i+=22
		k+=1
		return res

	
>>> p2(4)
['0']
>>> 
>>> def p2(s):
	res=[]
	i=0
	k=0
	while(k<=s):
		res+=[str(i)]
		i+=22
		k+=1
		return res

	
>>> p2(4)
['0']
>>> def p2(s):
	res=[]
	i=0
	k=0
	while(k<=s):
		res+=[str(i)]
		i+=22
		k+=1
	return res

>>> p2(4)
['0', '22', '44', '66', '88']
>>> def p22(s):
	res=[]
	i=0:
		
SyntaxError: invalid syntax
>>> def p22(s):
	res=[]
	i=0
	while(i<=s):
		res+=[7+i*10]
		i+=1
	return res

>>> p22(5)
[7, 17, 27, 37, 47, 57]
>>> def p1(s):
	return [str(x*2)+str(x*2) for x in range(s)]

>>> def p23(s):
	return [str(x)+str(7) for x in range(s)]

>>> p23(4)
['07', '17', '27', '37']
>>> def p23(s):
	res=[7]
	return res+=[str(x+1)+str(7) for x in range(s-1)]
SyntaxError: invalid syntax
>>> 
>>> def p23(s):
	return [str((x*10)+7) for x in range(s)]

>>> p23(4)
['7', '17', '27', '37']
>>> def p3(s):
	return [x x x for x in range(s)]
SyntaxError: invalid syntax
>>> def p3(s):
	return [x,x,x, for x in range(s)]
SyntaxError: invalid syntax
>>> 
>>> def p3(s):
	res=[0,0,0]
	res+=[x%3+res[s-3] for x in range(s)]
	return res

>>> def p3(s):
	res=[0,0,0]
	res+=[x%3+res[s-3] for x in range(s)]
	return res

>>> p3(6)
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    p3(6)
  File "<pyshell#79>", line 3, in p3
    res+=[x%3+res[s-3] for x in range(s)]
  File "<pyshell#79>", line 3, in <listcomp>
    res+=[x%3+res[s-3] for x in range(s)]
IndexError: list index out of range

>>> def p3(s):
	res=[0,0,0]
	res+=[x%3+res[s-3] for x in range(s-3)]
	return res

>>> p3(6)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    p3(6)
  File "<pyshell#82>", line 3, in p3
    res+=[x%3+res[s-3] for x in range(s-3)]
  File "<pyshell#82>", line 3, in <listcomp>
    res+=[x%3+res[s-3] for x in range(s-3)]
IndexError: list index out of range
>>> def p3(s):
	res=[0,0,0]
	res+=[x%3+res[s-3] for x in range(s+3)]
	return res

>>> p3(6)
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    p3(6)
  File "<pyshell#85>", line 3, in p3
    res+=[x%3+res[s-3] for x in range(s+3)]
  File "<pyshell#85>", line 3, in <listcomp>
    res+=[x%3+res[s-3] for x in range(s+3)]
IndexError: list index out of range
>>> def p3(s):
	res=[0,0,0]
	res+=[x%3+res[s-s%3] for x in range(s)]
	return res

>>> p3(6)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    p3(6)
  File "<pyshell#88>", line 3, in p3
    res+=[x%3+res[s-s%3] for x in range(s)]
  File "<pyshell#88>", line 3, in <listcomp>
    res+=[x%3+res[s-s%3] for x in range(s)]
IndexError: list index out of range
>>> def p3(s):
	res=[0,0,0]
	res+=[x%3+res[s-3] for x in range(3,s)]
	return res

>>> p3(6)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    p3(6)
  File "<pyshell#91>", line 3, in p3
    res+=[x%3+res[s-3] for x in range(3,s)]
  File "<pyshell#91>", line 3, in <listcomp>
    res+=[x%3+res[s-3] for x in range(3,s)]
IndexError: list index out of range
>>> def p3(s):
	res=[0,0,0]
	res+=[x%3+res[s-3] for x in range(3,s+1)]
	return res

>>> def p3(s):
	res=[0,0,0]
	res+=[x%3+res[s-3] for x in range(3,s)]
	return res

>>> def p3(s):
	res=[0,0,0]
	res+=[x%3+res[s-3] for x in range(3,s+1)]
	return res

>>> p3(6)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    p3(6)
  File "<pyshell#98>", line 3, in p3
    res+=[x%3+res[s-3] for x in range(3,s+1)]
  File "<pyshell#98>", line 3, in <listcomp>
    res+=[x%3+res[s-3] for x in range(3,s+1)]
IndexError: list index out of range
>>> def p3(s):
	res=[0,0,0]
	res+=[x%3+res[x-3] for x in range(3,s+1)]
	return res

>>> p3(6)
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    p3(6)
  File "<pyshell#101>", line 3, in p3
    res+=[x%3+res[x-3] for x in range(3,s+1)]
  File "<pyshell#101>", line 3, in <listcomp>
    res+=[x%3+res[x-3] for x in range(3,s+1)]
IndexError: list index out of range
>>> def p3(s):
	res=[x%3+res[x-3] for x in range(3,s+1)]
	return res

>>> p3(6)
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    p3(6)
  File "<pyshell#104>", line 2, in p3
    res=[x%3+res[x-3] for x in range(3,s+1)]
  File "<pyshell#104>", line 2, in <listcomp>
    res=[x%3+res[x-3] for x in range(3,s+1)]
NameError: free variable 'res' referenced before assignment in enclosing scope
>>> def p3(s)
	res=[x%3+res[x-3] for x in range(3,s+1)]
	return res
SyntaxError: invalid syntax
>>> 
>>> def p3(s):
	res=[0,0,0]
	res+=[x%3+res[x-3] for x in range(3,s+1)]
	return res

>>> def p3(s):
	res=[0,0,0]
	res+=[x%3+res[x-3] for x in range(3,s)]
	return res

>>> p3(6)
[0, 0, 0, 0, 1, 2]
>>> def p3(s):
	res=[0,0,0]
	res+=[x%3+res[x-3] for x in range(3,s)]
	return res

>>> p3(20)
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    p3(20)
  File "<pyshell#114>", line 3, in p3
    res+=[x%3+res[x-3] for x in range(3,s)]
  File "<pyshell#114>", line 3, in <listcomp>
    res+=[x%3+res[x-3] for x in range(3,s)]
IndexError: list index out of range
>>> p3(24)
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    p3(24)
  File "<pyshell#114>", line 3, in p3
    res+=[x%3+res[x-3] for x in range(3,s)]
  File "<pyshell#114>", line 3, in <listcomp>
    res+=[x%3+res[x-3] for x in range(3,s)]
IndexError: list index out of range
>>> p3(18)
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    p3(18)
  File "<pyshell#114>", line 3, in p3
    res+=[x%3+res[x-3] for x in range(3,s)]
  File "<pyshell#114>", line 3, in <listcomp>
    res+=[x%3+res[x-3] for x in range(3,s)]
IndexError: list index out of range
>>> p3(6)
[0, 0, 0, 0, 1, 2]
>>> p3(7)
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    p3(7)
  File "<pyshell#114>", line 3, in p3
    res+=[x%3+res[x-3] for x in range(3,s)]
  File "<pyshell#114>", line 3, in <listcomp>
    res+=[x%3+res[x-3] for x in range(3,s)]
IndexError: list index out of range
>>> p3(9)
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    p3(9)
  File "<pyshell#114>", line 3, in p3
    res+=[x%3+res[x-3] for x in range(3,s)]
  File "<pyshell#114>", line 3, in <listcomp>
    res+=[x%3+res[x-3] for x in range(3,s)]
IndexError: list index out of range
>>> def p3(s):
	res=[0,0,0]
	res+=[x%3+res[x-3] for x in range(3,s)]
	return res

>>> p3(6)
[0, 0, 0, 0, 1, 2]
>>> p3(21.0)
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    p3(21.0)
  File "<pyshell#122>", line 3, in p3
    res+=[x%3+res[x-3] for x in range(3,s)]
TypeError: 'float' object cannot be interpreted as an integer
>>> p3(21)
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    p3(21)
  File "<pyshell#122>", line 3, in p3
    res+=[x%3+res[x-3] for x in range(3,s)]
  File "<pyshell#122>", line 3, in <listcomp>
    res+=[x%3+res[x-3] for x in range(3,s)]
IndexError: list index out of range
>>> def p3(s):	
	return [x%3*x/3 for x in range(s)]

>>> p3(21)
[0.0, 0.3333333333333333, 1.3333333333333333, 0.0, 1.3333333333333333, 3.3333333333333335, 0.0, 2.3333333333333335, 5.333333333333333, 0.0, 3.3333333333333335, 7.333333333333333, 0.0, 4.333333333333333, 9.333333333333334, 0.0, 5.333333333333333, 11.333333333333334, 0.0, 6.333333333333333, 13.333333333333334]
>>> [0.0, 0.3333333333333333, 1.3333333333333333, 0.0, 1.3333333333333333, 3.3333333333333335, 0.0, 2.3333333333333335, 5.333333333333333, 0.0, 3.3333333333333335, 7.333333333333333, 0.0, 4.333333333333333, 9.333333333333334, 0.0, 5.333333333333333, 11.333333333333334, 0.0, 6.333333333333333, 13.333333333333334]
[0.0, 0.3333333333333333, 1.3333333333333333, 0.0, 1.3333333333333333, 3.3333333333333335, 0.0, 2.3333333333333335, 5.333333333333333, 0.0, 3.3333333333333335, 7.333333333333333, 0.0, 4.333333333333333, 9.333333333333334, 0.0, 5.333333333333333, 11.333333333333334, 0.0, 6.333333333333333, 13.333333333333334]
>>> p3(9)
[0.0, 0.3333333333333333, 1.3333333333333333, 0.0, 1.3333333333333333, 3.3333333333333335, 0.0, 2.3333333333333335, 5.333333333333333]
>>> 5/3
1.6666666666666667
>>> int(5/3)
1
>>> def p3(s):
	return [x%3*int(x/3) for x in range(s)]

>>> p3(9)
[0, 0, 0, 0, 1, 2, 0, 2, 4]
>>> def fr():
    a = []
    nums = [2,3,4,5,6,7,8,9]
    notprime = [0,2,3,5,7]
    for i in range(100):
        for x in nums:
            if i in notprime:
                break 
            if i % x == 0:
                a.append(i)
                break
    return a

>>> def al():
    aet = [i for i in range(100) for x in [2, 3, 4, 5, 6, 7, 8, 9] if i % x == 0 and i not in [0, 2, 3, 5, 7]]
    return list(set(aet))

>>> def sl(l):
    a = [i for i in range(1, l + 1) if l % i == 0]
    return a

>>> def sll(l):
    a = [[l[x][i] for x in range(len(l))] for i in range(len(l[0]))]
    return a

>>> def dada():
    a, b = [], True
    for i in range(2, 101):
        b = True
        for x in range(2, i):
            if i % x == 0:
                b = False
                break 
        if b: a.append(i)
    return a

>>> def sixth(l):
    a = [1]
    for i in range (2, l + 1):
        if l % i == 0: a.append(i)
    return a

>>> def seventh(l):
    a = []
    for i in range(len(l[0])):
        b = []
        for x in range(len(l)):
            b.append(l[x][i])
        a.append(temp)
    return a

>>> 
