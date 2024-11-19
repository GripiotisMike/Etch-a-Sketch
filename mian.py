# Importing the required modules
from turtle import Turtle, Screen

# Create a Turtle object named tim
tim = Turtle()
tim.shape("turtle")  # Setting the turtle's shape to "turtle"

# Create a Screen object
screen = Screen()

# Function to move the turtle forwards by 10 units
def move_forwards():
    tim.forward(10)

# Function to turn the turtle left by 10 degrees
def turn_left():
    tim.left(10)

# Function to turn the turtle right by 10 degrees
def turn_right():
    tim.right(10)

# Function to move the turtle backwards by 10 units
def move_backwards():
    tim.backward(10)

# Function to clear the screen and reset the turtle's position
def clear_screen():
    screen.reset()

# Listen for keyboard input and bind specific keys to functions
screen.listen()  # Start listening for key events

# Key bindings: Map the keys to respective functions
screen.onkey(fun=move_forwards, key="w")  # 'w' for moving forwards
screen.onkey(turn_left, "a")              # 'a' for turning left
screen.onkey(turn_right, "d")             # 'd' for turning right
screen.onkey(move_backwards, "s")         # 's' for moving backwards
screen.onkey(clear_screen, "c")           # 'c' for clearing the screen

# Exit the program when the screen is clicked
screen.exitonclick()
