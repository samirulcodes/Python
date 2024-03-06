<!-- >>> import sys
>>> sys.getrefcount(24601)
3
>>> sys.getrefcount('aman') 
3
>>> sys.getrefcount('hitesh') 
3
>>> sys.getrefcount(1)        
90

>>> a=3
>>> a='aman'
>>> a=3.3
>>> print(a)
3.3
>>> a=5
>>> b=2
>>> a
5
>>> b
2
>>> a=a+2
>>> a
7

>>> mylistOne=[1,2,3]
>>> mylistTwo=mylistOne
>>> mylistOne='aman'    
>>> mylistTwo           
[1, 2, 3]
>>> mylistOne        
'aman'
>>> mylistOne=[1,2,3]   
>>> mylistTwo           
[1, 2, 3]
>>> mylistOne
[1, 2, 3]
>>> mylistOne[0]=30
>>> mylistOne       
[30, 2, 3]
>>> mylistTwo 
[1, 2, 3]

>>> l1=[1,2,3]
>>> l2=l1
>>> l1
[1, 2, 3]
>>> l2
[1, 2, 3]
>>> l1[0]=24
>>> l1
[24, 2, 3]
>>> l2
[24, 2, 3]

>>> p1=[1,2,3]
>>> p2=p1
>>> p2=[1,2,3]
>>> p1[0]=10
>>> p1
[10, 2, 3]
>>> p2
[1, 2, 3]

>>> h1=[1,2,3]
>>> h2=h1[:]
>>> h1
[1, 2, 3]
>>> h2
[1, 2, 3]
>>> h1[0]=4
>>> h1
[4, 2, 3]
>>> h2
[1, 2, 3]

>>> n=[1,2,3]
>>> m=n
>>> m
[1, 2, 3]
>>> n
[1, 2, 3]
>>> m==n
True
>>> m is n
True
>>> n=[1,2,3]
>>> m==n
True
>>> m=[1,2,3]
>>> m==n
True
>>> m is n
 False   <!-- because m has another reference and n has another reference 
>>> -->