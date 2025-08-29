import random
print ("Welcome to the Rock, Paper, Scissors game:")
ask_for_help = input ("Press Enter to continue or type (Help) for the rules help ").lower ()
if ask_for_help :
    print ("             ************ Rules ************              ")
    print ("          1) You choose and the computer chooses          ")
    print ("          2) Rock smashes Scissors -> Rock wins           ")
    print ("          3) Scissors cut Paper -> Scissors win           ")
    print ("          4) Paper covers Rock -> Paper wins              ")

#-------------------------------------------------------------------------------------------
ran_ans=random.randint(0,2)
#-------------------------------------------------------------------------------------------
rps = ["""
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)
""","""
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)
""","""
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___) 
"""]
#-------------------------------------------------------------------------------------------
if ran_ans == 0 :
    ans_form_computer="Rock"
elif ran_ans == 1 :
    ans_form_computer="Paper"
else:
    ans_form_computer="Scissors"

the_ans = input ("Enter your choice (Rock, Paper, Scissors) ").capitalize()
#-------------------------------------------------------------------------------------------
if the_ans == "Rock":
    ans_form_user = rps[0]
    print("\nYou chose:\n")
    print(ans_form_user)
elif the_ans == "Paper":
    ans_form_user = rps[1]
    print("\nYou chose:\n")
    print(ans_form_user)
elif the_ans == "Scissors":
    ans_form_user = rps[2]
    print("\nYou chose:\n")
    print(ans_form_user)
else:
    print("Invalid choice. Please run the program again and choose rock, paper, scissors")
#-------------------------------------------------------------------------------------------
#* if the user win
if (the_ans == "Rock" and ran_ans == 2) or (the_ans == "Paper" and ran_ans == 0) or (the_ans == "Scissors" and ran_ans == 1) :
    print("\nComputer choice:\n")
    print(rps[ran_ans])
    print(f"You Win 🎉🎉🎉 : {the_ans} beat {ans_form_computer}")
#* if the user lose
elif (the_ans == "Rock" and ran_ans == 1) or (the_ans == "Paper" and ran_ans == 2) or (the_ans == "Scissors" and ran_ans == 0):
    print("\nComputer choice:\n")
    print(rps[ran_ans])
    print(f"You Lose: {ans_form_computer} beat {the_ans}")
#* if it's tie
else :
    print("\nComputer choice:\n")
    print(rps[ran_ans])
    print(f"Thats a Tie")