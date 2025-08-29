import string
The_sen = input ("Enter the sentence ")
The_sen_without_pun = []
for The_letter in The_sen:
    if The_letter not in string.punctuation :
        The_sen_without_pun.append (The_letter)
print ("".join(The_sen_without_pun))