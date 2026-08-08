# Math Quiz Game 🚀

A sleek, interactive, and fast-paced desktop math quiz application built with **Python** and **Tkinter**. Challenge your mental math skills, customize your gameplay experience, and compete for the top spot on the local leaderboard!

## 🌟 Features

 Dynamic Main Menu: Enter your name and prepare for the challenge in a beautiful modern dark-themed interface.

Custom Time Settings: A toggle button lets you switch the match timer between 30 and 60 seconds before starting a game.
Multiple Game Modes Selection: A dedicated selection screen featuring 4 mathematical operations:
Addition (+)
Subtraction (-)
Multiplication (*)
Division (//)
Smart Balancing Logic: Dynamic number constraints tailored per game mode to optimize gameplay fluidness:
Numbers range up to 20 for standard addition and subtraction.
Numbers downscale up to 10 for multiplication and division to keep calculations smooth.
Automatic number inversion during subtraction to prevent negative outputs.
Mathematical inverse multiplication algorithm for division to ensure zero-remainder whole answers.
Local Leaderboard: Saves player performance data in a local scores.txt file. Scores are recorded automatically at game over; view the Top 3 per mode (Addition, Subtraction, Multiplication, Division) any time by opening the Leaderboard screen.
Independent Leaderboard View: A dedicated toggle button on the leaderboard screen lets you switch between the 30-second and 60-second leaderboards at any time, regardless of which timer you're currently playing with.
Advanced Navigation Flow: Seamless switching between windows including standalone "Play Again", "Change Mode" (return to category grid), and "Back to Menu" (return to name entry screen) workflows.

## 🛠️ Requirements

To run this application from the source code, you only need **Python 3.x** installed on your system. Tkinter comes pre-installed with standard Python distributions.

bash
pip install pygame

You'll also need correct.mp3 and incorrect.mp3 sound files in the same folder as math_quiz.py — the game loads them to play a sound on every correct or incorrect answer.

## 🚀 How to Clone and Run

Follow these simple steps in your terminal to download and start playing the game on your local computer:

### 1. Clone the Repository
Clone this project directly from GitHub to your machine:
```bash
git clone https://github.com/pavelgetzov-creator/Math_Quiz_Game
```

### 2. Navigate into the Project Folder
Move your terminal position into the newly created directory:
```bash
cd Math_Quiz_Game
```

### 3. Run the Game
Execute the script using Python to launch the graphical user interface:
```bash
python math_quiz.py
```

## 📦 Building an Executable (.exe)

If you want to package this script into a standalone executable file so others can play it without installing Python, make sure you have `pyinstaller` installed and run:

```bash
pip install pyinstaller
pyinstaller --clean --onefile --noconsole math_quiz.py
```
*Note: After building, your executable will be located inside the `dist/` directory. Remember to keep a blank `scores.txt` file in the same directory as the executable.*

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
