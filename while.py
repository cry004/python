from random import choice
questions = ["Q1:  ","Q2:  ","Q3:  "]
question = choice(questions)
answer = input(question).strip().lower()

while answer != "just because":
    answer = input("Why? ").strip().lower()
print("Oh..Okay")
