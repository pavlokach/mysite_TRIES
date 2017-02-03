from flask import Flask, render_template, request, session, redirect
from test import *
import random

app = Flask(__name__)

app.secret_key = "A3k0izUH2Exn8qSY5w01uwNnN0WCQ1F1"
player1 = Player('player1')
player2 = Player('player2')
@app.route("/diceit")
def dice_type():
    dice1, dice2 = dice_generator()
    session["location"] += dice1 + dice2
    if session["location"] >= 40:
        session["location"] -= 40
    session["x"], session["y"] = find_coords(session["location"])
    result = check_position(session["location"])

@app.route("/restart")

def new():
    player1 = Player('player1')
    global player1
    return render_template("monopoly.html")

@app.route("/", methods=['GET', 'POST'])

def profile():
    print("########")
    for i in request.form:
        print(i,"= ", end="")
        try:
            print(request.form[i])
        except: print("ERR=)")
    print("########")
    ####LAPS ENDING####
    if request.form["type_sent"] == "first_time":
        x, y = find_coords(0)
        session["x"], session["y"] = x, y
        session["location"] = 0
        return render_template("main.html", type_sent="dice", name_main_button="Let's start!", field_status="0",
        question="", answers=[], x=x, y=y)
    elif request.form["type_sent"] == "dice":
        dice1, dice2 = dice_generator()
        session["location"] += dice1 + dice2
        if session["location"] >= 40:
            session["location"] -= 40
        session["x"], session["y"] = find_coords(session["location"])
        x, y = session["x"], session["y"]
        result = check_position(session["location"])
        if len(result) == 4:
            session["question"] = result[1]
            question = result[0]
            answers = result[1:]
            random.shuffle(answers)
            return render_template("main.html", type_sent="answer_question", name_main_button="Send answer!", field_status="0",
        question=question, answers=answers, x=x, y=y, dice1=dice1, dice2=dice2)
        elif len(result) == 3:
            return render_template("main.html", type_sent="pass_three", name_main_button="Pass!", field_status="0",
        question=result[0], answers=[], x=x, y=y, dice1=dice1, dice2=dice2)
        elif len(result) == 2:
            return render_template("main.html", type_sent="pass_twenty", name_main_button="Pass!", field_status="0",
        question=result[0], answers=[], x=x, y=y, dice1=dice1, dice2=dice2)
        elif len(result) == 5:
            return render_template("main.html", type_sent="dice", name_main_button="Dice it!", field_status="0",
        question=result[0], answers=[], x=x, y=y, dice1=dice1, dice2=dice2)
        else:
            return render_template("main.html", type_sent="return_twenty", name_main_button="Return!", field_status="0",
        question=result[0], answers=[], x=x, y=y, dice1=dice1, dice2=dice2)
    elif request.form["type_sent"] == "answer_question":
        if request.form["user_answer"] == session["question"]:
            x, y = session["x"], session["y"]
            question = "Ви Калєга=))"
        else:
            session["location"] -= 3
            if session["location"] < 0:
                session["location"] += 40
            session["x"], session["y"] = find_coords(session["location"])
            x, y = session["x"], session["y"]
            question = "Ви погарячкували=))"
        return render_template("main.html", type_sent="dice", name_main_button="Dice it!", field_status="0",
        question=question, answers=[], x=x, y=y)
    elif request.form["type_sent"] == "pass_three" or request.form["type_sent"] == "return_twenty" or request.form["type_sent"] == "pass_twenty":
        if request.form["type_sent"] == "pass_three":
            session["location"] += 3
            if session["location"] >= 40:
                session["location"] -= 40
            session["x"], session["y"] = find_coords(session["location"])
            x, y = session["x"], session["y"]
        elif request.form["type_sent"] == "pass_twenty":
            session["location"] += 20
            if session["location"] >= 40:
                session["location"] -= 40
            session["x"], session["y"] = find_coords(session["location"])
            x, y = session["x"], session["y"]
        else:
            session["location"] -= 20
            if session["location"] >= 40:
                session["location"] -= 40
            session["x"], session["y"] = find_coords(session["location"])
            x, y = session["x"], session["y"]
        return render_template("main.html", type_sent="dice", name_main_button="Dice it!", field_status="0",
        question="Кидайте=)", answers=[], x=x, y=y)
if __name__ == "__main__":
    app.run(debug=True)
