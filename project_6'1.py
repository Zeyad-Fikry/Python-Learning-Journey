import random
ran_num = random.randint(1,11)
num_form_user = int(input("Guess a number between 1 and 10: "))
while num_form_user != ran_num:
    if num_form_user > ran_num:
        num_form_user = int(input("Too high! Guess again: "))
    else :
        num_form_user = int(input("Too low! Guess again: "))
print ("Congratulations! You guess the number!")