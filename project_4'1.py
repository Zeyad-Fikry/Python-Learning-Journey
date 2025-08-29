import random
print("Welcome to 'whose wallet'")
print("You will give me a list of names, and I will pick a person to pay")
name_string = input("If you're ready, enter the names separated by comma\n")
names = name_string.split(", ")
#----------------------------------------------------------------
print (f"Please ask {random.choice(names)} to take his wallet out. Dinner is on him")
#----------------------------------------------------------------
# num_names = len(names)-1
# ran = random.randint(0,num_names)
# print (f"Please ask {names[ran]} to take his wallet out. Dinner is on him")