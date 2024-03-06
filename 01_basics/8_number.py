''' 
>>> x=2
>>> y=3
>>> z=4
>>> x+y
5
>>> 40+2.2
42.2
>>> int(2.2)
2
>>> float(40)
40.0
>>> 'samirul'+'islam'
'samirulislam'
>>> x,y,z
(2, 3, 4)
>>> x+2,y*2,z/2
(4, 6, 2.0)
>>> y%2
1
>>> z**2
16
>>> 100**2
10000
>>> 2**100 
1267650600228229401496703205376
>>> 
>>> result=1/3.0
>>> result
0.3333333333333333
>>> repr('aman')
"'aman'"
>>> str('aman')
'aman'
>>> print('aman')
aman

 1 < 2    
True
>>> 5.0==5.0
True
>>> 5.0==5
True
>>> 4.0!=5
True

>>> x=1
>>> y=2
>>> z=3
>>> x<y<z
True
>>> x<y and y<z
True
>>> x<y or y>z
True
>>> 1==2 < 3
False
>>> import math
>>> math.floor(3.9)
3
math.floor(-3.9)     
-4
>>> math.trunc(2.9)
2
>>> math.trunc(-2.9) 
-2
>>> 2+1j
(2+1j)
>>> (2+1j)* 3
(6+3j)
>>> 0o20
16
>>> 0xff
255
>>> 0b1000
8
>>> oct(64)
'0o100'
>>> hex(64)
'0x40'
>>> bin(1000)
'0b1111101000'
>>> bin(8)
'0b1000'
>>> int('64',8)
52
>>> int('64',16) 
100

>>> int('1000',2) 
8
>>> x=1
>>> x<<2
4
>>> x<<3
8
>>> x | y  
3
>>> import random
>>> random.random()
0.9355308022309511
>>> random.random()
0.37470660686121204
>>> random.randint(1,10) 
2
>>> random.randint(1,10)
2
>>> random.randint(1,10)
10
>>> random.randint(1,10)
8

>>> arr=['aman', 'samirul', 'chai', 'coffee']  
>>> random.choice(arr)
'coffee'
>>>
>>> random.choice(arr)
'samirul'
>>> random.choice(arr)
'samirul'
>>> random.choice(arr)
'chai'
>>> random.choice(arr)
'coffee'
>>> random.choice(arr)
'aman'
>>> random.choice(arr)
'aman'
>>> random.shuffle(arr) 
>>> arr
['aman', 'samirul', 'chai', 'coffee']
>>> arr
['aman', 'samirul', 'chai', 'coffee']
>>> random.shuffle(arr)
>>> arr
['aman', 'coffee', 'chai', 'samirul']
>>> 0.1+0.1+0.4
0.6000000000000001
>>> 0.1+0.1+0.1
0.30000000000000004
>>> 0.1+0.1+0.1-0.3
5.551115123125783e-17
>>> from decimal import Decimal
>>> Decimal('0.1')+Decimal('0.1')+Decimal('0.1')
Decimal('0.3')
>>> Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-Decimal('0.3
')
Decimal('0.0')

>>> from fractions import Fraction 
>>> myFrac=Fraction(2,7)
>>> myFrac
Fraction(2, 7)
>>> myFrac=Fraction(2,10) 
>>> myFrac
Fraction(1, 5)
>>>
>>> set1={1,2,3,4}
>>> set1 & {1,3}  (and) &--> intersection 
{1, 3}

>>> set1 |  {1,3}   (or) |--> union
{1, 2, 3, 4}
>>> set1 - {1,2,3,4} 
set()
>>> set1 | {1,3,6}   
{1, 2, 3, 4, 6}
>>> set1
{1, 2, 3, 4}
>>> type({})
<class 'dict'>
>>> type(set1) 
<class 'set'>
>>> type(True)
<class 'bool'>
>>> True==1
True
>>> False==0
True
>>> True is 1
<stdin>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
False
>>> True+2 
3
'''