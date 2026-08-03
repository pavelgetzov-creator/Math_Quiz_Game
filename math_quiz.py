import tkinter as tk
import random as rd

app = tk.Tk()
app.title("Math Quiz")
app.geometry("400x400")
app.config(bg="#0f172a")


app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

menu_frame = tk.Frame(app)
menu_frame.grid(row=0, column=0)
menu_frame.config(bg="#0f172a")

game_frame = tk.Frame(app)
game_frame.config(bg="#0f172a")

score = 0
correct_answer = 0
time_left = 60


def generate_question():
    global correct_answer 

    num1 = rd.randint(1,20)
    num2 = rd.randint(1,20)

    correct_answer = num1 + num2

    question_label.config(text=f"How much is {num1} + {num2}?")

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
    if user_answer == correct_answer:
        score = score +1
        score_label.config(text=f"Score: {score}")

    answer_entry.delete(0, tk.END)
    generate_question()


def countdown():
    global time_left

    if time_left > 0 :
        time_left = time_left -1
        timer_label.config(text=f"Time: {time_left}")
        app.after(1000,countdown)
    else:
        question_label.config(text="Game Over!",fg="#f43f5e")
        answer_entry.config(state="disabled")
        submit_button.config(state="disabled")
        update_leaderboard()

def update_leaderboard():
    global score
    

    player_name = name_entry.get()
    

    if player_name == "":
        player_name = "Anonymous"

    with open("scores.txt", "a", encoding="utf-8") as file:
        file.write(f"{player_name}: {score}\n")
    all_scores = []

    try:
        with open("scores.txt", "r", encoding="utf-8") as file:
            for line in file:
                all_scores.append(line.strip())
    except FileNotFoundError:
        pass

    

    all_scores.sort(key=lambda x: int(x.split(": ")[1]), reverse=True)
    top_scores = all_scores[:3]
    formatted_scores = []

    for index, score_line in enumerate(top_scores):
            formatted_scores.append(f"{index + 1}. {score_line}")


    leaderboard_text = "Top Scores:\n" + "\n".join(formatted_scores)
    leaderboard_label.config(text=leaderboard_text)

def restart_game():
    global score, time_left

    score = 0
    time_left = 60

    answer_entry.config(state="normal")
    submit_button.config(state="normal")
    answer_entry.delete(0, tk.END)
    score_label.config(text="Scores: 0")
    timer_label.config(text="Time: 60")
    question_label.config(fg="#ffffff")


    generate_question()
    countdown()

def start_game(event=None):
    menu_frame.pack_forget()
    game_frame.grid(row=0, column=0)


    generate_question()
    countdown()
    answer_entry.focus_set()


#Бутони,лейбъли и полета от менюто
title_label = tk.Label(menu_frame, text="Welcome to Math Quiz!!",font=("Segoe UI", 20, "bold"), fg="#38bdf8", bg="#0f172a")
title_label.pack(pady=20)


enter_name_label = tk.Label(menu_frame, text="Enter your name: ",font=("Segoe UI", 12), fg="#ffffff", bg="#0f172a")
enter_name_label.pack(pady=25)

name_entry = tk.Entry(menu_frame, font=("Segoe UI", 12), bg="#1e293b", fg="#ffffff", bd=0, relief="flat", justify="center")
name_entry.pack(pady=5)


play_button = tk.Button(menu_frame, text="Play Game 🚀",font=("Segoe UI", 11, "bold"), bg="#10b981", fg="#ffffff", bd=0, relief="flat", command= start_game)
play_button.pack(padx= 20,pady= 8)


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

leaderboard_label = tk.Label(game_frame, text="Top Scores: ", font=("Segoe UI", 11), fg="#38bdf8", bg="#1e293b", padx=15, pady=10)
leaderboard_label.grid(row=3, column=0, columnspan=2, pady=20)

game_frame.grid_columnconfigure(0, weight=1)
game_frame.grid_columnconfigure(1, weight=1)






name_entry.focus_set()
name_entry.bind("<Return>", start_game)
answer_entry.bind("<Return>", check_answer)
app.mainloop()