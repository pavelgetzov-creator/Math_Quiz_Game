import tkinter as tk
import random as rd
from pygame import mixer

mixer.init()

app = tk.Tk()
app.title("Math Quiz")
app.geometry("600x600")
app.config(bg="#0f172a")


app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

menu_frame = tk.Frame(app)
menu_frame.grid(row=0, column=0)
menu_frame.config(bg="#0f172a")

mode_frame = tk.Frame(app)
mode_frame.config(bg="#0f172a")

game_frame = tk.Frame(app)
game_frame.config(bg="#0f172a")

leaderboard_frame = tk.Frame(app)
leaderboard_frame.config(bg="#0f172a")


score = 0
correct_answer= 0
selected_time = 30
time_left = 60
timer_job = None
leaderboard_time = 30

def generate_question():
    global correct_answer, chosen_mode
    max_num1 = 20
    max_num2 = 20

    if chosen_mode == "*" or chosen_mode == "/":
        max_num1 = 10
        max_num2 = 10


    num1 = rd.randint(1, max_num1)
    num2 = rd.randint(1, max_num2)

    if chosen_mode == "-" and num1 < num2:
            num1, num2 = num2, num1
    
    if chosen_mode == "/":
        num1 = num1 * num2


    if chosen_mode == "+":
        correct_answer = num1 + num2
    elif chosen_mode == "-":
        correct_answer = num1 - num2
    elif chosen_mode == "*":
        correct_answer = num1 * num2
    elif chosen_mode == "/":
        correct_answer = num1 // num2

    


    question_label.config(text=f"How much is {num1} {chosen_mode} {num2}?")

def check_answer(event = None):
    global score

    if time_left == 0:
        return

    if submit_button["state"] == "disabled":
        return

    try:
        user_answer = int(answer_entry.get())
    except ValueError:
        return
    answer_entry.delete(0, tk.END)
    
    if user_answer == correct_answer:
        score = score +1
        score_label.config(text=f"Score: {score}")
        answer_entry.config(bg="#10b981")
        generate_question()
        mixer.music.load("correct.mp3")
        mixer.music.play()
        
    else:
        answer_entry.config(bg="#f43f5e")
        mixer.music.load("incorrect.mp3")
        mixer.music.play()

    app.after(300, lambda: answer_entry.config(bg="#1e293b"))
    


def countdown():
    global time_left, timer_job

    if time_left > 0 :
        time_left = time_left -1
        timer_label.config(text=f"Time: {time_left}")
        timer_job = app.after(1000,countdown)
    else:
        question_label.config(text="Game Over!",fg="#f43f5e")
        answer_entry.config(state="disabled")
        submit_button.config(state="disabled")

        save_score()
        update_leaderboard()

def save_score():
    global score, chosen_mode, selected_time

    player_name = name_entry.get()

    if player_name == "":
        player_name = "Anonymous"

    with open("scores.txt", "a", encoding="utf-8") as file:
        file.write(f"{player_name}|{chosen_mode}|{selected_time}|{score}\n")


def update_leaderboard():
    
    all_add = []
    all_sub = []
    all_mul = []
    all_div = []

    try:
        with open("scores.txt", "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if "|" in line:
                    try:
                        parts = line.split("|")
                        if len(parts) == 4 and parts[-1].isdigit():
                            if int(parts[2]) == leaderboard_time:
                                if parts[1] == "+":
                                    all_add.append(line)
                                elif parts[1] == "-":
                                    all_sub.append(line)
                                elif parts[1] == "*":
                                    all_mul.append(line)
                                elif parts[1] == "/":
                                    all_div.append(line)
                    except Exception:
                        continue
    except FileNotFoundError:
        pass

   

    all_add.sort(key=lambda x: int(x.split("|")[-1]), reverse=True)
    all_sub.sort(key=lambda x: int(x.split("|")[-1]), reverse=True)
    all_mul.sort(key=lambda x: int(x.split("|")[-1]), reverse=True)
    all_div.sort(key=lambda x: int(x.split("|")[-1]), reverse=True)



    def format_top_3(scores_list):

        top_3 = scores_list[:3]
        lines = []
        for index, score_line in enumerate(top_3):
            parts = score_line.split("|")
            name = parts[0]
            mode = parts[1]
            points = parts[-1]
            lines.append(f"{index + 1}. Name: {name} Score: {points} pts")

        if not lines:
            lines.append("No scores yet.")
        return "\n".join(lines)

    leaderboard_text = f"🏆 HIGH SCORES ({leaderboard_time}s) 🏆\n\n"
    leaderboard_text += "➕ ADDITION:\n" + format_top_3(all_add) + "\n\n"
    leaderboard_text += "➖ SUBTRACTION:\n" + format_top_3(all_sub) + "\n\n"
    leaderboard_text += "✖️ MULTIPLICATION:\n" + format_top_3(all_mul) + "\n\n"
    leaderboard_text += "➗ DIVISION:\n" + format_top_3(all_div)

    leaderboard_label.config(text=leaderboard_text, justify="left")

def toggle_leaderboard_time():
    global leaderboard_time

    if leaderboard_time == 30:
        leaderboard_time = 60
        leaderboard_toggle.config(text="Leaderboard (60s)")
    else:
        leaderboard_time = 30
        leaderboard_toggle.config(text="Leaderboard (30s)")

    update_leaderboard()

def reset_game_state():
    global score, time_left, timer_job, selected_time

    if timer_job is not None:
        app.after_cancel(timer_job)
        timer_job = None

    score = 0
    
    time_left = selected_time
    answer_entry.config(state="normal")
    submit_button.config(state="normal")
    answer_entry.delete(0, tk.END)
    score_label.config(text="Scores: 0")
    timer_label.config(text=f"Time: {selected_time}")
    question_label.config(fg="#ffffff")


def restart_game():

    reset_game_state()

    generate_question()
    countdown()

    
def set_time(seconds):
    global selected_time, time_left

    selected_time = seconds


    time_left = selected_time
    timer_label.config(text=f"Time: {selected_time}")

def toggle_time_selection(button_widget):
    global selected_time

    if selected_time == 30:
        selected_time = 60
        button_widget.config(text="Time: 60 seconds")
    else:
        selected_time = 30
        button_widget.config(text="Time: 30 seconds")

    

def start_game(event=None):
    
    menu_frame.grid_forget()
    mode_frame.grid(row=0, column=0)
    

def start_quiz_mode(mode):
    global chosen_mode, time_left, selected_time

    chosen_mode = mode
    mode_frame.grid_forget()
    game_frame.grid(row=0, column=0)

    time_left = selected_time
    timer_label.config(text=f"Time: {time_left}")

    generate_question()
    countdown()
    answer_entry.focus_set()


def back_to_menu():   

    reset_game_state()

    name_entry.focus_set()
    game_frame.grid_forget()
    menu_frame.grid(row=0, column=0)


def back_to_mode():

    reset_game_state()

    name_entry.focus_set()
    game_frame.grid_forget()
    mode_frame.grid(row=0, column=0)


def leaderboard():

    update_leaderboard()

    reset_game_state()
    

    name_entry.focus_set()
    game_frame.grid_forget()
    leaderboard_frame.grid(row=0, column=0)

    

def back_from_leaderboard():
    leaderboard_frame.grid_forget()
    game_frame.grid(row=0, column=0)

#Бутони,лейбъли и полета от менюто
title_label = tk.Label(menu_frame, text="Welcome to Math Quiz!!",font=("Segoe UI", 20, "bold"), fg="#38bdf8", bg="#0f172a")
title_label.grid(row=0, column=0, pady=20)


enter_name_label = tk.Label(menu_frame, text="Enter your name: ",font=("Segoe UI", 12), fg="#ffffff", bg="#0f172a")
enter_name_label.grid(row=1, column=0, pady=25)

name_entry = tk.Entry(menu_frame, font=("Segoe UI", 12), bg="#1e293b", fg="#ffffff", bd=0, relief="flat", justify="center")
name_entry.grid(row=2, column=0, pady=5)



play_button = tk.Button(menu_frame, text="Play Game 🚀",font=("Segoe UI", 11, "bold"), bg="#10b981", fg="#ffffff", bd=0, relief="flat", command= start_game)
play_button.grid(row=5, column=0, padx= 20,pady= 8)

# Бутони,лейбъли и полета от режимите на играта
mode_label = tk.Label(mode_frame, text="Choose a mode:",font=("Segoe UI", 18, "bold"), fg="#38bdf8", bg="#0f172a")
mode_label.grid(row=0, column=0, pady=20)

addition_button = tk.Button(mode_frame, text="Addition ➕",font=("Segoe UI", 11, "bold"), bg="#10b981", fg="#ffffff", bd=0, relief="flat", padx=15, pady=5, command=lambda: start_quiz_mode("+"))
addition_button.grid(row=1, column=0, padx=10, pady=10)

subbtraction_button = tk.Button(mode_frame, text="Subtraction ➖",font=("Segoe UI", 11, "bold"), bg="#f43f5e", fg="#ffffff", bd=0, relief="flat", padx=15, pady=5, command=lambda: start_quiz_mode("-"))
subbtraction_button.grid(row=2, column=0, padx=10, pady=10)

multiplication_button = tk.Button(mode_frame, text="Multiplication ✖️",font=("Segoe UI", 11, "bold"), bg="#3b82f6", fg="#ffffff", bd=0, relief="flat", padx=15, pady=5, command=lambda: start_quiz_mode("*"))
multiplication_button.grid(row=3, column=0, padx=10, pady=10)

division_button = tk.Button(mode_frame, text="Division ➗",font=("Segoe UI", 11, "bold"), bg="#facc15", fg="#ffffff", bd=0, relief="flat", padx=15, pady=5, command=lambda: start_quiz_mode("/"))
division_button.grid(row=4, column=0, padx=10, pady=10)

mode_frame.grid_columnconfigure(0, weight=1)
mode_frame.grid_columnconfigure(1, weight=1)

# Бутони,лейбъли и полета от самата игра
answer_entry = tk.Entry(game_frame, font=("Segoe UI", 14), bg="#1e293b", fg="#ffffff", bd=0, relief="flat", justify="center")
answer_entry.grid(row=1, column=0, padx=10, pady=10)

submit_button = tk.Button(game_frame, text="Submit",font=("Segoe UI", 11, "bold"), bg="#10b981", fg="#ffffff", bd=0, relief="flat", padx=15, pady=5
, command=check_answer)
submit_button.grid(row=1, column=1, padx=10, pady=10)

restart_button = tk.Button(game_frame, text="Play Again 🔄",font=("Segoe UI", 10, "bold"), bg="#f43f5e", fg="#ffffff", bd=0, relief="flat", padx=15, pady=5, command=restart_game)
restart_button.grid(row=4, column=0, columnspan=2, pady=10)

question_label = tk.Label(game_frame,text="Press Start", font=("Segoe UI", 18, "bold"), fg="#ffffff", bg="#0f172a")
question_label.grid(row=0, column=0 ,pady=15 )

score_label = tk.Label(game_frame, text="Scores 0",font=("Segoe UI", 12), fg="#ffffff", bg="#0f172a")
score_label.grid(row=2, column=0, columnspan=2, pady= 15)

timer_label = tk.Label(game_frame, text="Time: 60",font=("Segoe UI", 12, "bold"), fg="#f43f5e", bg="#0f172a")
timer_label.grid(row=0, column=1, padx=10, pady=30)

time_button = tk.Button(menu_frame, text=f"Time: 30 seconds",command=lambda: toggle_time_selection(time_button),font=("Segoe UI", 10, "bold"), bg="#3b82f6", fg="#ffffff", bd=0, relief="flat", padx=15, pady=5)
time_button.grid(row=3, column=0, columnspan=2, pady=15)


game_frame.grid_columnconfigure(0, weight=1)
game_frame.grid_columnconfigure(1, weight=1)

back_to_menu_button = tk.Button(game_frame, text="Back to Menu",font=("Segoe UI", 10, "bold"), bg="#f43f5e", fg="#ffffff", bd=0, relief="flat", padx=15, pady=5, command=back_to_menu)
back_to_menu_button.grid(row=7, column=0, columnspan=2, pady=10)

back_to_mode_button = tk.Button(game_frame, text="Back to Modes 🎯",font=("Segoe UI", 10, "bold"), bg="#f43f5e", fg="#ffffff", bd=0, relief="flat", padx=15, pady=5, command=back_to_mode)
back_to_mode_button.grid(row=6, column=0, columnspan=2, pady=10)

leaderboard_label = tk.Label(leaderboard_frame, text="Top Scores: ", font=("Segoe UI", 11), fg="#38bdf8", bg="#1e293b", padx=15, pady=10)
leaderboard_label.grid(row=1, column=0, columnspan=2, pady=20)

leaderboard_button = tk.Button(game_frame, text="Leaderboard 🏆",font=("Segoe UI", 10, "bold"), bg="#facc15", fg="#ffffff", bd=0, relief="flat", padx=15, pady=5, command=leaderboard)
leaderboard_button.grid(row=5, column=0, columnspan=2, pady=10)

back_from_leaderboard_button = tk.Button(leaderboard_frame, text="Back to Game",font=("Segoe UI", 10, "bold"), bg="#f43f5e", fg="#ffffff", bd=0, relief="flat", padx=15, pady=5, command=back_from_leaderboard)
back_from_leaderboard_button.grid(row=2, column=0, columnspan=2, pady=10)

leaderboard_toggle = tk.Button(leaderboard_frame, text="Leaderboard (30s)",font=("Segoe UI", 10, "bold"), bg="#3b82f6", fg="#ffffff", bd=0, relief="flat", padx=15, pady=5, command=toggle_leaderboard_time)
leaderboard_toggle.grid(row=0, column=0, columnspan=2, pady=10)

name_entry.focus_set()
name_entry.bind("<Return>", start_game)
answer_entry.bind("<Return>", check_answer)
app.mainloop()
