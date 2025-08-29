import random 
words = ["bad", "good", "ugly"]
random_word = random.choice(words)

_list = ["_"] * len(random_word)

print (" ".join(_list))
# print (random_word)

#-------------------------------------------------------------------
counter = 6

Hangman = ["""
  +---+
      |
      |
      |
      |
      |
=========""", """
  +---+
  |   |
      |
      |
      |
      |
=========""", """
  +---+
  |   |
  O   |
      |
      |
      |
=========""", """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""", """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""", r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""", r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""", r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""]

print (Hangman[0])


# print("\nYou have 6 more tries")

test_for_repeat_letter = []

while "_" in _list and counter  > 0  :

    letter_input = input ("Please guess a letter: ").lower()

    if letter_input in test_for_repeat_letter :
        print ("You already guessed that. Try again")
        print(f"You have {counter} more tries")
        continue
    
    test_for_repeat_letter.append(letter_input)

    for index in range (len(random_word)):
        if random_word[index] == letter_input :
            _list [index] = letter_input

    print (" ".join(_list))

    if letter_input  not in _list :
        counter -=1
        print (Hangman[-(counter+2)])
    print(f"You have {counter} more tries")



if counter == 0 :
    print ("\n\tYou lose!")
    print (Hangman[7])
else :
    print ("""
                *********
                *You Win
                ********* """)
