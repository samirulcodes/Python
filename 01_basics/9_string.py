# >>> chai="lemon tea"     
# >>> chai
# 'lemon tea'
# >>> print(chai)
# lemon tea
# >>> chai="black coffee"
# >>> chai[0]
# 'b'
# >>> first_char=chai[0]
# >>> print(first_char)
# b
# >>> slice_chai=chai[0:5]
# >>> print(slice_chai)
# black
# >>> num="0123456789"
# >>> num[:]
# '0123456789'
# >>> num[2:]
# '23456789'
# >>> num[:6] 
# '012345'
# >>> num[0:7:2] 
# '0246'
# >>> num[0:7:3] 
# '036'
# >>> num[0:7:4] 
# '04'
# >>> num[0:7:-2] 
# >>> num[1:-7]  
# '12'
# >>> chai
# 'black coffee'
# >>> print(chai.lower())
# black coffee
# >>> print(chai.upper()) 
# BLACK COFFEE
# >>> chai="  masala coffee  "
# >>> chai
# '  masala coffee  '
# >>> print(chai.strip())
# masala coffee
# >>> chai="butter tea"
# >>> print(chai.replace("butter","normal"))
# normal tea
# >>> chai
# 'butter tea'
# >>> chai="Lemon,Ginger,Masala,Butter"
# >>> print(chai.split())
# ['Lemon,Ginger,Masala,Butter']
# >>> chai="Lemon, Ginger, Masala, Butter" 
# >>> print(chai.split())
# ['Lemon,', 'Ginger,', 'Masala,', 'Butter']
# >>> print(chai.split(", ")) 
# ['Lemon', 'Ginger', 'Masala', 'Butter']
# >>> chai= "Butter Coffee"               
# >>> print(chai.find("Coffee"))
# 7
# >>> print(chai.find("coffee")) 
# -1
# >>> chai= "Butter Coffee Coffee Coffee" 
# >>> print(chai.count("coffee")) 
# 0
# >>> print(chai.count("Coffee")) 
# 3
# >>> chai="Masala"
# >>> quantity=2
# >>> order="I order {} cup of {} Chai"
# >>> print(order.format(quantity,chai))
# I order 2 cup of Masala Chai
# >>> chai=["Masala", "Lemon", "Mint"]
# >>> chai
# ['Masala', 'Lemon', 'Mint']
#     print("".join(chai)) 
# MasalaLemonMint
# >>> print(" ".join(chai)) 
# Masala Lemon Mint
# >>> print("- ".join(chai)) 
# Masala- Lemon- Mint
# >>> print(",  ".join(chai)) 
# Masala,  Lemon,  Mint
# >>> chai="Butter Coffee"
# >>> print(len(chai))
# 13
# >>> chai
# 'Butter Coffee'
# >>> for i in chai:
# ...     print(i)
# ... 
# B
# u
# t
# t
# e
# r

# C
# o
# f
# f
# e
# e
# >>> chai="He said, \"Masala chai is awesome\" "
# >>> chai
# 'He said, "Masala chai is awesome" '
# >>> chai="Masala\nchai"
# >>> chai
# 'Masala\nchai'
# >>> print(chai)
# Masala
# chai
# >>> chai=r"Masala\nchai"        
# >>> print(chai)
# Masala\nchai
# >>> chai=r"c:\user\pwd"
# >>> print(chai)
# c:\user\pwd
# >>> chai="c:\\user\\pwd"  
# >>> chai
# 'c:\\user\\pwd'
# >>> print(chai)
# c:\user\pwd
# >>> chai
# 'c:\\user\\pwd'

# chai="Masala Chai"
# >>> print("Butter" in chai)
# False
# >>> print("Masala" in chai)
# True
# >>>
