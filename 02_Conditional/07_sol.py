# customize a coffee order:"small","medium","large" with an option for "Extra shot" of expresso

order_size="Medium"
extra_shot=True

if extra_shot:
   coffee=order_size + " Coffee with an extra shot"
    
else:
    coffee=order_size+" Coffee"

print("order: ",coffee)
   