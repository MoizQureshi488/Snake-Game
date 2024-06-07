import turtle
import random
import time

delay = 0.1
score = 0
high_score = 0

# Setting up the screen
wn = turtle.Screen()
wn.title('Snake Game by Moiz')
wn.bgcolor('green')
wn.setup(width=600, height=600)
wn.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('white')
head.penup()
head.goto(0, 0)
head.direction = 'stop'

# SNAKE FOOD
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(0, 100)

# Snake body
segments = []

# Functions to control the direction of the head
def go_up():
    if head.direction != 'down':
        head.direction = 'up'

def go_down():
    if head.direction != 'up':
        head.direction = 'down'

def go_left():
    if head.direction != 'right':
        head.direction = 'left'

def go_right():
    if head.direction != 'left':
        head.direction = 'right'

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, 'w')
wn.onkeypress(go_down, 's')
wn.onkeypress(go_left, 'a')
wn.onkeypress(go_right, 'd')

# Functions to move the snake
def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)

# Output score and high score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(0, 260)
score_pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Function to reset the game
def reset_game():
    global score, high_score
    time.sleep(1)
    head.goto(0, 0)
    head.direction = 'stop'
    # Hide the segments
    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()
    # Reset score
    score = 0
    score_pen.clear()
    score_pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

# Function to handle collision
def check_collision():
    global high_score
    # Check for collision with borders
    if (
        head.xcor() > 290 or head.xcor() < -290 or
        head.ycor() > 290 or head.ycor() < -290
    ):
        reset_game()
        if score > high_score:
            high_score = score
        return True
    # Check for collision with self
    for segment in segments:
        if head.distance(segment) < 20:
            reset_game()
            if score > high_score:
                high_score = score
            return True
    return False

# Main game loop
while True:
    wn.update()
    move()

    # Check for collision
    if check_collision():
        continue

    # Check for collision with food
    if head.distance(food) < 20:
        # Move the food to a random position
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score

        score_pen.clear()
        score_pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

        # Add a segment to the snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    time.sleep(delay)

wn.mainloop()

