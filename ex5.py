name = 'Zed A. Shaw'
age = 35  # not a lie
height = 74  # inches
correct_height = height * 2.54  # centimeters FTW
weight = 180  # lbs
correct_weight = weight * 0.453592  # kilogram FTW
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("If you use centimers and kilogram like me, this is the good measure :")
print(f"He is {correct_weight} kilogram heavy and {correct_height} centimers tall.")
print("Actually, that's not to heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending of the coffee.")

# tricky line !
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
