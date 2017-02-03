from flask import Flask, render_template, request, session, redirect, jsonify
from test import *
import random

app = Flask(__name__)

app.secret_key = "A3k0izUH2Exn8qSY5w01uwNnN0WCQ1F1"

@app.route("/answer_question")

def answer_question():
    if request.args.get('user_answer') == session["last_answer"]:
        question = "Ви калєга"
        session["x_prev"], session["y_prev"] = session["x"], session["y"]
    else:
        question = "Ви погарячкували"
        session["location"] -= 3
        # write down x, y as x_prev, y_prev
        session["x_prev"], session["y_prev"] = session["x"], session["y"]
        # find new x, y
        session["x"], session["y"] = find_coords(session["location"])
    return jsonify(x=session["x"],
                   y=session["y"],
                   x_prev=session["x_prev"],
                   y_prev=session["y_prev"],
                   type_sent="diceit",
                   question=question,
                   name_main_button="Dice it!",
                   location=session["location"])

@app.route("/return_twenty")

def return_twenty():
    session["location"] -= 20
    # write down x, y as x_prev, y_prev
    session["x_prev"], session["y_prev"] = session["x"], session["y"]
    # find new x, y
    session["x"], session["y"] = find_coords(session["location"])
    return jsonify(x=session["x"],
                   y=session["y"],
                   x_prev=session["x_prev"],
                   y_prev=session["y_prev"],
                   type_sent="diceit",
                   question="Кидайте...",
                   name_main_button="Dice it!",
                   location=session["location"])

@app.route("/pass_three")

def pass_twenty():
    session["location"] += 20
    # write down x, y as x_prev, y_prev
    session["x_prev"], session["y_prev"] = session["x"], session["y"]
    # find new x, y
    session["x"], session["y"] = find_coords(session["location"])
    return jsonify(x=session["x"],
                   y=session["y"],
                   x_prev=session["x_prev"],
                   y_prev=session["y_prev"],
                   type_sent="diceit",
                   question="Кидайте...",
                   name_main_button="Dice it!",
                   location=session["location"])

@app.route("/pass_three")

def pass_three():
    session["location"] += 3
    # write down x, y as x_prev, y_prev
    session["x_prev"], session["y_prev"] = session["x"], session["y"]
    # find new x, y
    session["x"], session["y"] = find_coords(session["location"])
    return jsonify(x=session["x"],
                   y=session["y"],
                   x_prev=session["x_prev"],
                   y_prev=session["y_prev"],
                   type_sent="diceit",
                   question="Кидайте...",
                   name_main_button="Dice it!",
                   location=session["location"])

@app.route("/diceit")

def dice_type():
    #generate dice1 and dice2
    dice1, dice2 = dice_generator()
    #find total location with dice1 and dice2
    session["location"] += dice1 + dice2
    #write down x, y as x_prev, y_prev
    session["x_prev"], session["y_prev"] = session["x"], session["y"]
    #find new x, y
    session["x"], session["y"] = find_coords(session["location"])
    #find what_to_do
    result = check_position(session["location"])
    if result[1].strip() == "3":
        #pass_three
        type_sent = "pass_tree"
        #reload
        name_main_button = "Pass!"
        answers = []
    elif result[1].strip() == "2":
        #pass_twenty
        type_sent = "pass_twenty"
        name_main_button = "Pass!"
        answers = []
    elif result[1].strip() == "5":
        #Nothing, Dice it!
        type_sent = "diceit"
        name_main_button = "Dice it!"
        answers = []
    elif result[1].strip() == "0":
        #return_twenty
        type_sent = "return_twenty"
        name_main_button = "Return!"
        answers = []
    else:
        #question
        type_sent = "answer_question"
        name_main_button = "Answer!"
        session["last_answer"] = result[1]
        answers = result[1:]
        random.shuffle(answers)
    return jsonify(dice1=dice1,
                   dice2=dice2,
                   x=session["x"],
                   y=session["y"],
                   x_prev=session["x_prev"],
                   y_prev=session["y_prev"],
                   type_sent=type_sent,
                   question=result[0],
                   name_main_button=name_main_button,
                   answers=answers,
                   location=session["location"])

@app.route("/restart")

def restart_game():
    #KK
    return render_template("monopoly.html")

@app.route("/")

def beginning():
    session["location"] = 0
    session["x"], session["y"] = find_coords(0)
    session["x_prev"], session["y_prev"] = session["x"], session["y"]
    return render_template("main.html",
                           x=session["x"],
                           y=session["y"],
                           )
if __name__ == "__main__":
    app.run(debug=True)
