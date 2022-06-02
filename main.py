import turtle
import pandas

screen = turtle.Screen()
screen.title("The US States Guessing Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

score = 0
game_on = True
correct_guesses = []
while game_on:
    answer = turtle.textinput(title=(f"{score}/50 States Guessed!"), prompt="Make a Guess!").title()

    data = pandas.read_csv("50_states.csv")

    states_list = data["state"].to_list()
    x_list = data["x"].to_list()
    y_list = data["y"].to_list()

    def correct(x, y, state):
        new_turtle = turtle.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        new_turtle.goto(x, y)
        new_turtle.write(state)

    if answer == "Exit":
        loss_list = []
        for i in states_list:
            if i not in correct_guesses:
                loss_list.append(i)
        print(loss_list)
        break

    for state in states_list:
        if answer == state:
            index = states_list.index(state)
            x = x_list[index]
            y = y_list[index]
            correct(x, y, state)

            if answer not in correct_guesses:
                correct_guesses.append(answer)
                score += 1


    if score == 50:
        game_on = False






turtle.mainloop()