
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a Hangman game in Python to practice string manipulation, loops, conditionals, random word selection, and user input handling.

## 📝 Tasks

### 🛠️ Create the Game Setup

#### Description
Set up the core game data needed to play Hangman, including a predefined list of words and the logic to choose one word randomly.

#### Requirements
Completed program should:

- Define a predefined list of words for the game.
- Randomly select one word from that list at the start of each game.
- Initialize values to track guessed letters and remaining incorrect attempts.


### 🛠️ Implement the Gameplay Loop

#### Description
Build the main game loop that accepts letter guesses, updates progress, and ends with a clear result when the player wins or runs out of attempts.

#### Requirements
Completed program should:

- Accept one letter guess at a time from the user.
- Show current word progress using underscores for unknown letters (for example, `_ _ _ _`).
- Decrease and display incorrect guesses remaining when a wrong letter is entered.
- End the game when the full word is guessed or attempts are exhausted.
- Display a clear win message or lose message at the end.
