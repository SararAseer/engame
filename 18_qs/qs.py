def ts(i):
	return [[x,y,(x**2+y**2)**.5] for x in range(i) for y in range(i) if int((x**2+y**2)**.5)==(x**2+y**2)**.5 and x+y>(x**2+y**2)**.5 and (x**2+y**2)**.5+y>x and (x**2+y**2)**.5+x>y]


    
def qs(l):
	if len(l)<=1:
		return l
	return qs([x for x in l if x<l[len(l)-1]])+[x for x in l if x==l[len(l)-1]]+qs([x for x in l if x>l[len(l)-1]])

