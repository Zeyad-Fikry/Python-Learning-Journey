import random
import string
print ("Welcome to the Password Generator ")
length =  int(input ("Enter the total number of characters in the password: "))
num_of_letters = int(input ("Enter the number of letters in the password: "))
num_of_numbers = int(input ("Enter the number of numbers in the password: "))
num_of_symbols = int(input ("Enter the number of symbols in the password: "))
if num_of_letters + num_of_numbers + num_of_symbols == length:
    ran_let=random.choices(string.ascii_letters, k = num_of_letters )
    ran_num=random.choices(string.digits, k = num_of_numbers )
    ran_sym=random.choices(string.punctuation, k = num_of_symbols ) 
    ran_total = ran_num+ran_let+ran_sym
    random.shuffle(ran_total)
    print("Generated password: "+"".join(ran_total))
else :
    print ("Invalid input. The sum of letters, numbers, symbols doesn't match the password")
