from tkinter import CENTER
import turtle
import random
import time

# screen setup
screen = turtle.Screen()
screen.title("worm game")
screen.setup(width=700, height=700)
screen.tracer(0)
screen.bgcolor("#1d1d1d")

# danger area
turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310, 250)
turtle.pendown()
turtle.color("red")
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()

# scoreboard
score = 0
delay = 0.1

# snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("green")
snake.penup()
snake.goto(0, 0)
snake.direction = 'stop'

# food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("yellow")
food.penup()
food.goto(30, 30)

old_food = []

# final score
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("white")
scoring.penup()
scoring.hideturtle()
scoring.goto(0, 300)
scoring.write("Score: 0", align="center", font=("Roboto", 24, "bold"))  # Initialize score as 0

# moves
def snake_up():
    if snake.direction != "down":
        snake.direction = "up"


def snake_down():
    if snake.direction != "up":
        snake.direction = "down"


def snake_right():
    if snake.direction != "left":
        snake.direction = "right"


def snake_left():
    if snake.direction != "right":
        snake.direction = "left"


def snake_move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)
    elif snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    elif snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)
    elif snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)


# binds
screen.listen()
screen.onkeypress(snake_up, "w")  # Changed "W" to "w"
screen.onkeypress(snake_down, "s")  # Changed "S" to "s"
screen.onkeypress(snake_right, "d")  # Changed "D" to "d"
screen.onkeypress(snake_left, "a")  # Changed "A" to "a"

# main
while True:
    screen.update()
    if snake.distance(food) < 20:
        x = random.randint(-290, 270)
        y = random.randint(-240, 240)
        food.goto(x, y)
        scoring.clear()
        score += 1
        scoring.write("Score: {}".format(score), align="center", font=("Roboto", 24, "bold"))

        # create food
        new_food = turtle.Turtle()
        new_food.speed(0)
        new_food.shape("square")
        new_food.color("red")
        new_food.penup()
        old_food.append(new_food)

    # add ball to snake
    for index in range(len(old_food) - 1, 0, -1):
        a = old_food[index - 1].xcor()
        b = old_food[index - 1].ycor()
        old_food[index].goto(a, b)

    if len(old_food) > 0:
        a = snake.xcor()
        b = snake.ycor()
        old_food[0].goto(a, b)

    snake_move()

    if (
        snake.xcor() > 280
        or snake.xcor() < -300
        or snake.ycor() > 240
        or snake.ycor() < -240
    ):
        time.sleep(1)
        screen.clear()
        screen.bgcolor("turquoise")
        scoring.goto(0, 0)
        scoring.write(
            "             GAME OVER \n Your score is {}".format(score),
            align="center",
            font=("Roboto", 30, "bold"),
        )
        break  # Added break to exit the game loop

    for f in old_food:
        if f.distance(snake) < 20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor("turquoise")
            scoring.goto(0, 0)
            scoring.write(
                "             GAME OVER \n Your score is {}".format(score),
                align="center",
                font=("Roboto", 30, "bold"),
            )
            break  # Added break to exit the game loop

    time.sleep(delay)

turtle.Terminator()
