# >>> chai_types={"Masala":"Spicy","Ginger":"Zesty","Green":"Mild"}
# >>> chai_types  
# {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}

# >>> chai_types["Masala"] 
# 'Spicy'

# >>> chai_types.get("Ginger")
# 'Zesty'

# >>> chai_types.get("Gingery") # it will return nothing

# >>> chai_types["Masalaa"]   # throws an error(key error)

#  chai_types["Green"]="Fresh"
# >>> chai_types
# {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}

# >>> for chai in chai_types:
# ...     print(chai)
# ... 
# Masala
# Ginger
# Green

# >>> for chai in chai_types:
# ...     print(chai , chai_types[chai])
# ... 
# Masala Spicy
# Ginger Zesty
# Green Fresh

# >>> for key,value in chai_types.items(): #items() is a method for accessing both key and value in dictionary
#     # here items="masala":"spicy"
# ...     print(key, value)
# ... 
# Masala Spicy
# Ginger Zesty
# Green Fresh

# >>> if "Masala" in chai_types:
# ...     print(" I have Masala Chai ")
# ... 
#  I have Masala Chai

# >>> print(len(chai_types))
# 3

# >>> chai_types["Coffe"]="Black" # Adding new item
# >>> chai_types # printing
# {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh', 'Coffe': 'Black'}

# >>> chai_types.pop("Ginger") # pop--> whatever you want to remove just pass key value
# 'Zesty'
# >>> chai_types
# {'Masala': 'Spicy', 'Green': 'Fresh', 'Coffe': 'Black'}


# >>> chai_types.popitem()  # popitem--> it remove last item   
# ('Coffe', 'Black')
# >>> chai_types
# {'Masala': 'Spicy', 'Green': 'Fresh'}

#  tea_shop={
# ... "chai":{"Masala":"Spicy", "Ginger":"Zesty"},
# ... "Tea":{"Green":"Mild","black":"Strong"}
# ... }
# >>> print(tea_shop)  
# {'chai': {'Masala': 'Spicy', 'Ginger': 'Zesty'}, 'Tea': {'Green': 'Mild', 'black': 'Strong'}}

# >>> tea_shop["chai"] #Acessing chai 
# {'Masala': 'Spicy', 'Ginger': 'Zesty'}
           
# >>> tea_shop["chai"] ["Ginger"] #Acessing Ginger
# 'Zesty'

# squared_num={x:x**2 for x in range(6)}
# >>> squared_num   #printing                        
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# >>> squared_num.clear()
# >>> squared_num  #printing      
# {} #--> output

# declaring key and value in different variable and adding them

#  keys=["Masala", "Ginger", "Lemon"]
# >>> print(keys)
# ['Masala', 'Ginger', 'Lemon']

# >>> default_value="Delicious" # declaring value
# >>> new_dict= dict.fromkeys(keys, default_value) 
# >>> new_dict   # printing                                 
# {'Masala': 'Delicious', 'Ginger': 'Delicious', 'Lemon': 'Delicious'}

# >>> new_dict= dict.fromkeys(keys, keys) # when passing both key ---> o/p--?
# >>> new_dict #printing
# {'Masala': ['Masala', 'Ginger', 'Lemon'], 'Ginger': ['Masala', 'Ginger', 'Lemon'], 'Lemon': ['Masala', 'Ginger', 'Lemon']}  