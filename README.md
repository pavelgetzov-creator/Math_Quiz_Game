# Math Quiz Game 🚀

A sleek, interactive, and fast-paced desktop math quiz application built with **Python** and **Tkinter**. Challenge your mental math skills, customize your gameplay experience, and compete for the top spot on the local leaderboard!

## 🌟 Features

- **Dynamic Main Menu:** Enter your name and prepare for the challenge in a beautiful modern dark-themed interface.
- **Custom Time Settings:** Features an interactive sliding bar (`tk.Scale`) allowing you to set the match timer anywhere from 10 to 120 seconds.
- **Automated Math Logic:** Generates random addition questions dynamically while ensuring proper answer validation.
- **Local Leaderboard:** Saves player performance data securely in a local `scores.txt` file and displays the Top 3 highest scores automatically at game over.
- **Seamless Navigation:** Easily jump back and forth between the active game and the main menu using the integrated "Back to Menu" and "Play Again" flows.
- **Safe State Management:** Built-in safeguards to prevent clock-doubling speed bugs and multi-profile sync glitches.

## 🛠️ Requirements

To run this application from the source code, you only need **Python 3.x** installed on your system. Tkinter comes pre-installed with standard Python distributions.

## 🚀 How to Clone and Run

Follow these simple steps in your terminal to download and start playing the game on your local computer:

### 1. Clone the Repository
Clone this project directly from GitHub to your machine:
```bash
git clone https://github.com
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
