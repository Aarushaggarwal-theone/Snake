from turtle import Turtle
from food_class import Food

x_cor = 20
class Snake():
    
    """
    The Snake class represents the snake in a simple turtle graphics game.

    Attributes:
    - turtles (list): A list containing Turtle objects representing the segments of the snake.

    Methods:
    - __init__(): Initializes a new Snake object, creates the initial snake design, and sets it in motion.
    - design(): Creates the initial design of the snake with two segments.
    - move(): Moves the snake by updating the positions of its segments.
    - up(): Changes the snake's direction to upward if not already moving downward.
    - down(): Changes the snake's direction to downward if not already moving upward.
    - left(): Changes the snake's direction to leftward if not already moving rightward.
    - right(): Changes the snake's direction to rightward if not already moving leftward.
    - grow(): Adds a new segment to the snake, extending its length.
    """
    
    def __init__(self):
        self.turtles = []
        self.design()
        self.move()
        
        
    def design(self):
        for i in range(0, 2):
            x_cor = i * -20
            tim = Turtle()
            tim.shape('square')
            tim.color('white')
            tim.penup()
            tim.setpos(x_cor, 0)
            self.turtles.append(tim)
            
    def move(self):
        for i in range(len(self.turtles)-1, -1, -1):
            if self.turtles[i] == self.turtles[0]:
                self.turtles[i].forward(20)
                    
            else:
                turtle_x = self.turtles[i-1].xcor()
                turtle_y = self.turtles[i-1].ycor()
                
                self.turtles[i].goto(turtle_x, turtle_y)
                
    def up(self):
        if self.turtles[0].heading() != 270:
            self.turtles[0].setheading(90)
        
    def down(self):
        if self.turtles[0].heading() != 90:
            self.turtles[0].setheading(270)
        
    def left(self):
        if self.turtles[0].heading() != 0:
            self.turtles[0].setheading(180)
        
    def right(self):
        if self.turtles[0].heading() != 180:
            self.turtles[0].setheading(0)
            
    def grow(self):
        tim = Turtle()
        tim.hideturtle()
        tim.shape('square')
        tim.color('white')
        tim.penup()
        tim.goto(self.turtles[-1].xcor()-20, self.turtles[-1].ycor())
        tim.showturtle()
        self.turtles.append(tim)
