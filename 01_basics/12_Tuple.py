# this program is done on shell , this is inly for notes
# immutable

# >>> tea_types=("Black", "Green", "Lemon")
# >>> print(tea_types)
# ('Black', 'Green', 'Lemon') # o/p
 
# >>> tea_types[0]
# 'Black'

# >>> tea_types[-1] 
# 'Lemon'

# >>> tea_types[1:] 
# ('Green', 'Lemon')

# >>> tea_types[0]="Oolong" # trwos an error because it is immutable so it can't be changed

# >>> len(tea_types)
# 3

# >>> more_tea=("Herbal","Coffee")
# >>> all_tea=more_tea + tea_types

# >>> print(all_tea)
# ('Herbal', 'Coffee', 'Black', 'Green', 'Lemon')

# >>> if "Green" in all_tea:      
# ...     print(" I have Green Tea") 
# ...
#  I have Green Tea # o/p
 
 
# >>> more_tea=("Herbal", "Ginger", "Herbal") # chnaging the reference of more_tea
# >>> print(more_tea)
# ('Herbal', 'Ginger', 'Herbal')


# >>> more_tea.count("Herbal")
# 2
# >>> more_tea.count("Coffee") 
# 0

# >>> tea_types
# ('Black', 'Green', 'Lemon')
# >>> 
# >>> (black, green, lemon)=tea_types  # here (black, green, lemon) -> treat as a variable
# >>> black
# 'Black'
# >>> green
# 'Green'
# >>> Green

# >>> type(tea_types)
# <class 'tuple'>

# Nested tuple
# ("",(1,2,3),"")