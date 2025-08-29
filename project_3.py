print("""
─────▄───▄
─▄█▄─█▀█▀█─▄█▄
▀▀████▄█▄████▀▀
─────▀█▀█▀
""")
print("welcome to my island!")
print("There are two doors in front of you. 🚪 a red door and 🚪 a blue door")
door = input("Which door do you want to open? ").lower()
if door == "red":
    print("Great! now you entered a room.")
    print("you found three boxes: 🎁 white, 🎁 black, 🎁 green")
    box = input("which box do you open? ").lower()

    if box == "white":
        print("Oops! You opened aa box filled with snakes 🐍🐍🐍")
    elif box == "black":
        print("Oops! You opened aa box filled with spiders 🕷️ 🕷️ 🕷️")
    elif box == "green":
        print("congratulations! You found the treasure! 💰💰💰")
    else:
        print("Invalid choice! ")

elif door == "blue":
    print("Oops! You chose the crocodile door.")
    print("Game over!")

else:
    print("Invalid choice! ")