# >>> tea_varities=["Black","Green","Oolong","White"] 
# >>> print(tea_varities)
# ['Black', 'Green', 'Oolong', 'White']
# >>> print(tea_varities[2]) 
# Oolong
# >>> print(tea_varities[-1]) 
# White
# >>> print(tea_varities[1:3]) 
# ['Green', 'Oolong']
# >>> print(tea_varities[:2])    
# ['Black', 'Green']
# >>> print(tea_varities[2:]) 
# ['Oolong', 'White']
# >>> print(tea_varities[1:3:2]) 
# ['Green']
# >>> tea_varities[2]="Coffee"
# >>> print(tea_varities)
# ['Black', 'Green', 'Coffee', 'White']
# >>> tea_varities[1:2]       
# ['Green']
# >>> tea_varities[1:2]="Lemon"
# >>> print(tea_varities)
# ['Black', 'L', 'e', 'm', 'o', 'n', 'Coffee', 'White']
# >>> tea_varities=["Black","Green","Oolong","White"]
# >>> print(tea_varities)
# ['Black', 'Green', 'Oolong', 'White']
# >>> tea_varities[1:2]  
# ['Green']

# >>> tea_varities[1:2]=["Lemon"] 
# >>> print(tea_varities)
# ['Black', 'Lemon', 'Oolong', 'White']
# >>> tea_varities[1:3]           
# ['Lemon', 'Oolong']
# >>> tea_varities[1:3]=["Green","Masala"]
# >>> print(tea_varities)
# ['Black', 'Green', 'Masala', 'White']
# >>> tea_varities[1:1]   
# []
# >>> tea_varities[1:1]=["test","test"]
# >>> print(tea_varities)
# ['Black', 'test', 'test', 'Green', 'Masala', 'White']
# >>> tea_varities[1:2]  
# ['test']
# >>> tea_varities[1:3] 
# ['test', 'test']
# >>> tea_varities[1:3]=[]
# >>> print(tea_varities)
# ['Black', 'Green', 'Masala', 'White']

# >>> print(tea_varities)
# ['Black', 'Green', 'Masala', 'White']
# >>> for tea in tea_varities:
# ...     print(tea)
# ... 
# Black
# Green
# Masala
# White
# >>> 
# >>> for tea in tea_varities:
# ... 
# ...     print(tea, end="-") 
# Black-Green-Masala-White->>> 
# >>>     print(tea, end=",") 
# >>> for tea in tea_varities:
# ...     print(tea, end=",")  
# ... 
# Black,Green,Masala,White,>>> 

# >>> tea_varities.append("Oolong")
# >>> tea_varities
# ['Black', 'Green', 'Masala', 'White', 'Oolong']

# >>> if "Oolong" in tea_varities:   
# ...     print("I have Oolong Tea")
# ... 
# I have Oolong Tea

# >>> tea_varities.pop()             
# 'Oolong'

# >>> tea_varities.remove("Green")
# >>> tea_varities
# ['Black', 'Masala', 'White']

# >>> tea_varities.insert(1,"green")
# >>> tea_varities
# ['Black', 'green', 'Masala', 'White']
# >>> 
# >>> tea_varities_copy=tea_varities
# >>> tea_varities_copy
# ['Black', 'green', 'Masala', 'White']
# >>> 
# >>> tea_varities_copy.append("Lemon")
# >>> tea_varities_copy                
# ['Black', 'green', 'Masala', 'White', 'Lemon']
# >>>          
# >>> range(10)                        
# range(0, 10)
# >>> 
# >>> print(range(10))
# range(0, 10)
# >>> y=range(10))
# >>> y=range(10)
# >>> y
# range(0, 10)
# >>>
# >>> squared_num=[x**2 for x in range(10)]
# >>> squared_num
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# >>>
# >>> cubed_num=[x**3 for x in range(10)]
# >>> cubed_num
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]