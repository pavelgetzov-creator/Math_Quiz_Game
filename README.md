# 🧮 Math Quiz Game

Hey there! This is a simple, fun, and fast-paced desktop math game built with Python. If you want to test your mental math skills or just beat your own high score under pressure, give it a shot!

---

## ✨ Cool Stuff About It

* **Fresh Questions:** No hardcoded math here. The game throws random addition problems at you every single time.
* **Beat the Clock:** You get exactly 60 seconds to answer as many questions as you can. Speed matters!
* **The Leaderboard:** Your top 3 best runs are saved locally in a `scores.txt` file, so you can track your progress or challenge a friend.
* **Looks Great:** Designed with a clean, dark theme inspired by modern UI colors (Tailwind palette) so it's easy on the eyes.
* **No Mouse Needed:** You can hit `Enter` to type your name, start the game, and submit your answers instantly.
* **No Setup Needed:** I made a ready-to-go `.exe` file, meaning anyone can play it without messing around with Python installations.

---

## 🚀 How to Play

You've got two ways to get this running:

### Option 1: Just play it (Easiest)
1. Look over at the **Releases** section on the right side of this page.
2. Download the `MathQuiz.exe` file.
3. Double-click to open it and start playing! 
   *(Quick heads-up: Windows might pop up a warning since it doesn't recognize the publisher yet. Just click **"More info"** and then **"Run anyway"**).*

### Option 2: Run the code (For techy folks)
If you want to look at the source code or run it through your terminal:
1. **Clone this repo:**
   ```bash
   git clone https://github.com
   ```
2. **Jump into the folder:**
   ```bash
   cd YOUR-REPOSITORY-NAME
   ```
3. **Fire it up:**
   ```bash
   python main.py
   ```

---

## 🎮 Game Rules

1. Type your name on the home screen (or leave it blank to play as `Anonymous`).
2. Hit **Play Game** or press `Enter`.
3. Type your answer and smash `Enter` to submit.
4. When the timer hits 0, check out the leaderboard to see if you made the Top 3.
5. Click **Play Again** to reset the clock and try to beat your record!

---

## 🛠️ Under the Hood

Built simply using **Python 3.13.3, **Tkinter** for the graphics, the built-in **Random** library for the numbers, and compiled into a standalone app using **PyInstaller**.
