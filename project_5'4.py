words = input("Enter a sentence: ").split(" ")
len_words = len(words)
rev_sentence = []
for x in range(len_words):
    rev_sentence.append( words[-(x+1)] )
print ("Reversed sentence: " +" ".join(rev_sentence))

#! anther way 

# words = input("Enter a sentence: ").split(" ")
# print ("Reversed sentence: "+" ".join(words[::-1]))