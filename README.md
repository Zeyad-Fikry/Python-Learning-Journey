# ⚙️ Python Mini Projects 

A curated collection of Python projects designed to demonstrate core programming skills and best practices. Each project emphasizes practical applications, including input handling, data structures, and interactive game logic.

These projects serve as both a learning portfolio and a showcase of foundational Python proficiency.

---

## 📂 Projects

# ==================================

# 🏝️ Project 3 - Treasure Hunt Adventure  

This project is a **text-based adventure game** written in Python.  
You explore an island, choose doors, and open mysterious boxes — but beware, not everything hides treasure!  
 

---

## 🚀 Description  
The game is simple but fun:  
- You arrive on an island 🌴.  
- Two doors appear before you: 🚪 **red** or 🚪 **blue**.  
- Choosing the red door leads you to three boxes 🎁 — only one has treasure 💰.  
- Choosing the blue door means… game over 🐊.  
- Make the wrong choice, and you’ll meet snakes 🐍 or spiders 🕷️!  

This project is a great practice for **if/elif/else statements, input handling, and string formatting**.  

---

## 🎮 How to Play  
1. Make sure you have **Python 3.x** installed.  
2. Run the game:  
   ```bash
   python project_3.py

# ==================================

# 📚 Project 4 - Personal Library Manager  

This project is a **simple Python program** that helps you keep track of the books you own, the books you wish to have, and lets you update your library as you acquire or donate books.  

---

## 🚀 Description  
The program allows you to:  
- Add books you already own.  
- Create a wishlist of books you want in the future.  
- Move a book from your wishlist to your library once you acquire it.  
- Donate (remove) a book from your library.  

It’s an interactive way to practice **lists, input handling, and conditionals** in Python.  

---

## 🎮 How to Run  
1. Make sure you have **Python 3.x** installed.  
2. Run the script:  
   ```bash
   python project_4.py
   
# ==================================

# 💸 Project 4.1 - Whose Wallet?  

A fun little Python program that randomly selects someone from a group of names to pay the bill.  
It’s like a digital dice roll for deciding **“who’s paying for dinner tonight?”** 🍽️  


---

## 🚀 Description  
- The program asks you to input a list of names separated by commas.  
- It then **randomly picks one person** from the list using the `random` module.  
- That person is declared the one who will take their wallet out 💳.  

This project is a simple introduction to **lists, string splitting, random selection, and user input** in Python.  

---

## 🎮 How to Run  
1. Make sure you have **Python 3.x** installed.  
2. Run the program:  
   ```bash
   python project_4.1.py
   
# ==================================

# 🍎🥛 Project 4.2 - List Operations Playground  

A beginner-friendly Python project to practice **list manipulation** using nested lists.  
This script demonstrates how to **insert, append, remove, and update items** in lists.  


---

## 🚀 Description  
- The program begins with a nested list containing fruits and drinks.  
- It then performs multiple list operations such as:  
  - **Insert** new elements at specific positions  
  - **Append** new items to a list  
  - **Remove** existing elements  
  - **Add a completely new sublist**  

This is a simple project to learn the basics of **list indexing, methods, and dynamic updates**.  

---

## 🎮 How to Run  
1. Make sure you have **Python 3.x** installed.  
2. Run the program:  
   ```bash
   python project_4.2.py
   
# ==================================

# 🐇 Project 4.3 - Place the Rabbit  

A fun beginner-friendly Python game where the user decides where to place a **rabbit 🐇** inside a 3x3 field of grass 🌿.  


---

## 🚀 Description  
- The program starts with a **3x3 grid** filled with grass (`🌿`).  
- The user is asked to **enter a row and column** to place the rabbit.  
- The chosen grass spot (`🌿`) is replaced by the rabbit (`🐇`).  
- If the user enters an invalid number, an error message is shown.  

This project is a small step towards learning **2D grid representation** and **list manipulation** in Python.  

---

## 🎮 How to Play  
1. Run the program:  
   ```bash
   python project_4.3.py
   
# ==================================

# 🐇 Project 4.3.1 - Place the Rabbit (Optimized)

An improved version of **Project 4.3**, where the player chooses where to place a rabbit 🐇 in a 3x3 field of grass 🌿.

Started on **04/07/2024** as part of my Python mini-projects.  

---

## 🚀 Description
- The field is represented as a **2D list (3x3 grid)**.  
- The player enters a row and column (e.g., `23` → row 2, column 3).  
- The chosen spot (`🌿`) is replaced with the rabbit (`🐇`).  
- Compared to Project 4.3, this version is **shorter, cleaner, and uses direct list indexing** instead of many `if` statements.

---

## 🎮 How to Play
1. Run the program:
   ```bash
   python project_4.3.1.py
   
# ==================================

# ✊✋✌️ Project 5 - Rock, Paper, Scissors Game

A fun **Rock–Paper–Scissors** game written in Python 🎮.  

---

## 🚀 Description
- The player competes against the computer in the classic **Rock, Paper, Scissors** game.  
- Includes **ASCII art** for Rock, Paper, and Scissors.  
- Rules can be displayed by typing `Help` before starting.  
- The program determines **win, lose, or tie** based on both choices.

---

## 📜 Rules
1. You choose **Rock, Paper, or Scissors**.  
2. The computer also randomly chooses.  
3. Game logic:
   - Rock smashes Scissors → Rock wins 🪨✂️  
   - Scissors cut Paper → Scissors win ✂️📄  
   - Paper covers Rock → Paper wins 📄🪨  
   - Same choice → Tie 🤝  

---

## 🎮 How to Play
1. Run the program:
   ```bash
   python project_5.py
   
# ==================================

# ✅ Project 5'1 - Task Progress Tracker  

📌 A simple Python program that helps you organize your daily tasks into **Done ✅** and **Ongoing ⏳** lists.   

---

## 📖 Description  
- The user enters tasks separated by commas.  
- The program asks for each task if it is finished or not.  
- Finished tasks go into a **Done list ✅**.  
- Unfinished tasks go into an **Ongoing list ⏳**.  
- At the end, the program can show a **progress report**.  

---

## 🎮 How to Play
1. Run the program:
   ```bash
   python project_5'1.py
   
# ==================================

# 🛒 Project 5'2 - iShop Calculator  

A simple **shopping basket calculator** written in Python 🧮.  

---

## 🚀 Description  
- The program asks the user **how many items** are in the basket.  
- For each item, the user enters the **name** and its **price**.  
- The program stores all names in an `items` list and prices in a `price` list.  
- At the end, the user can choose to:  
  - View the full **list of items 🛍️**.  
  - View the **total cost 💲**.  

---

## 🎮 How to Play  
1. Run the program:  
   ```bash
   python project_5'2.py
   
# ==================================

# 👥 Project 5'3 - Friends' Name Abbreviator  

A Python program that takes your friends' **first and last names** and converts them into **abbreviations** 🔤.  

---

## 🚀 Description  
- The program asks the user to enter multiple friends' **first and last names**, separated by commas.  
- Converts the input into a list of names.  
- Splits each name into **first name** and **last name**.  
- Prints both names as lists (for clarity).  
- Finally, it prints the **abbreviated version** of each name, e.g.  
  - `"John Smith"` → `"J.S."`  
  - `"Alice Brown"` → `"A.B."`  

---

## 🎮 How to Play  
1. Run the program:  
   ```bash
   python project_5'3.py
   
# ==================================

# 🔄 Project 5'4 - Reverse Sentence  

A Python program that takes a sentence from the user and prints it **reversed word by word** 📝.  

---

## 🚀 Description  
- The user enters a full sentence.  
- The program splits the sentence into a list of words.  
- Then it rebuilds the sentence **in reverse order**.  
- There are **two methods** shown in the code:  
  1. Using a loop and appending each word in reverse order.  
  2. A shorter version using **list slicing (`[::-1]`)**.  

---

## 🎮 How to Play  
1. Run the program:  
   ```bash
   python project_5'4.py
   
# ==================================

# ✂️ Project 5'5 - Remove Punctuation  

A simple Python program that removes **punctuation marks** from a given sentence 📝.  

---

## 🚀 Description  
- The program asks the user to enter a sentence.  
- It checks every character in the sentence.  
- If the character is **not punctuation**, it is added to a new list.  
- Finally, the cleaned sentence is printed **without punctuation**.  
- Uses Python's built-in **`string.punctuation`** for all punctuation marks.  

---

## 🎮 How to Play  
1. Run the program:  
   ```bash
   python project_5'5.py
   
# ==================================

# 🔐 Project 6 - Password Generator  

A Python program that generates **strong random passwords** with customizable letters, numbers, and symbols.  

---

## 🚀 Description  
- The user specifies:  
  - Total password length.  
  - Number of **letters** (A–Z, a–z).  
  - Number of **digits** (0–9).  
  - Number of **symbols** (punctuation).  
- The program uses Python’s **`random`** and **`string`** modules.  
- It validates that the sum of letters, digits, and symbols matches the total length.  
- Finally, it generates a **secure password** by shuffling all characters randomly.  

---

## 🎮 How to Play  
1. Run the program:  
   ```bash
   python project_6.py
   
# ==================================

# 🎯 Project 6.1 - Number Guessing Game  

A simple **Number Guessing Game** built with Python 🕹️.  

---

## 🚀 Description  
- The program generates a **random number** between **1 and 10**.  
- The player tries to guess the number.  
- If the guess is **too high** or **too low**, the program gives hints until the correct number is guessed.  
- When the player guesses correctly, a **congratulations message** is displayed 🎉.  

---

## 🎮 How to Play  
1. Run the program:  
   ```bash
   python project_6.1.py
   
# ==================================

# 🔠 Project 7 - Hangman Game  

A classic **Hangman Game** built in Python 🎮.  

---

## 🚀 Description  
- The game randomly selects a **word** from a list (`["bad", "good", "ugly"]`).  
- The word is hidden with underscores (`_ _ _`).  
- The player guesses letters one by one.  
- If the letter is in the word, it’s revealed in its correct position.  
- If the guess is wrong, a **hangman drawing** progresses step by step.  
- The player has **6 tries** to guess the word before the game ends.  
- The program also prevents **repeated guesses**.  

---

## 🎮 How to Play  
1. Run the program:  
   ```bash
   python project_7.py
