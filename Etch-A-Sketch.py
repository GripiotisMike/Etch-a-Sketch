from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
screen = Screen()


def move_forwards():
    tim.forward(10)


def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)


def move_backwards():
    tim.backward(10)


def clear_screen():
    screen.reset()




screen.listen()
screen.onkey(fun=move_forwards, key="w")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(move_backwards, "s")
screen.onkey(clear_screen, "c")
screen.exitonclick()
