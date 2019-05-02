Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
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

>>> ps2("he2f")



[0, 1, 1, 0]
2
>>> def ps(pas):
	spec='''~!@#$%^&*()_+-={[}]|\:;""''<,>.?/'''
	a="qwertyuiopasdfghjklzxcvbnm"
	b=a.upper()

	
>>> def ps(pas):
	spec='''~!@#$%^&*()_+-={[}]|\:;""''<,>.?/'''
	a="qwertyuiopasdfghjklzxcvbnm"
	b=a.upper()
	res=[x for x in pas if x in a]
	res+=[x for x in pas if x in b]
	res+=[x for x in pas if x in spec]
	print(res)

	
>>> ps("ge")
['g', 'e']
>>> ps("ge2fafa")
['g', 'e', 'f', 'a', 'f', 'a']
>>> def ps(pas):
	num="1234567890"
	spec='''~!@#$%^&*()_+-={[}]|\:;""''<,>.?/'''
	a="qwertyuiopasdfghjklzxcvbnm"
	b=a.upper()
	c=[0,0,0,0]
	res=[c[0]=1 for x in pas if x in a]
	res+=[c[1]=1 for x in pas if x in b]
	res+=[c[2]=1 for x in pas if x in spec]
	res+=[c[3]=1 for x in pas if x in num]	
	print(c)
	
SyntaxError: invalid syntax
>>> 
>>> def ps(pas):
	num="1234567890"
	spec='''~!@#$%^&*()_+-={[}]|\:;""''<,>.?/'''
	a="qwertyuiopasdfghjklzxcvbnm"
	b=a.upper()
	c=[0,0,0,0]
	res=[x for x in pas if x in a]
	res+=[x for x in pas if x in b]
	res+=[x for x in pas if x in spec]
	res+=[x for x in pas if x in num]
	print(res)

	
>>> ps("ge2fafa")
['g', 'e', 'f', 'a', 'f', 'a', '2']
>>> ps("ge2fafa@'")
['g', 'e', 'f', 'a', 'f', 'a', '@', "'", '2']
>>> def ps(pas):
	num="1234567890"
	spec='''~!@#$%^&*()_+-={[}]|\:;""''<,>.?/'''
	a="qwertyuiopasdfghjklzxcvbnm"
	b=a.upper()
	u=[x for x in pas if x in a]
	l=[x for x in pas if x in b]
	s=[x for x in pas if x in spec]
	n=[x for x in pas if x in num]
	count=0
	res=[u,l,s,n]
	for i in range(len(res)):
		if len(res[i])>0:
			count+=1
		if len(res[i])>1:
			count+=1.5
		if len(res[i])==0:
			count=0
			break
	return count

>>> print(ps("2"))
0
>>> print(ps("aB@2"))
4
>>> def ps(pas):
	num="1234567890"
	spec='''~!@#$%^&*()_+-={[}]|\:;""''<,>.?/'''
	a="qwertyuiopasdfghjklzxcvbnm"
	b=a.upper()
	u=[x for x in pas if x in a]
	l=[x for x in pas if x in b]
	s=[x for x in pas if x in spec]
	n=[x for x in pas if x in num]
	count=0
	res=[u,l,s,n]
	for i in range(len(res)):
		if len(res[i])>0:
			count+=1
		if len(res[i])>1:
			count+=1.5
		if len(res[i])==0:
			count=0
			break
	if(len(pas)>8):
		count=10
	return count

>>> print(ps("aB@2"))
4
>>> print(ps("aB@dasdasd2"))
10
>>>



