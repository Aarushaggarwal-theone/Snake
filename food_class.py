from turtle import Turtle
from random import randint
class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        xcor = randint(-250, 250)
        ycor = randint(-250, 250)
        self.color('purple')
        self.goto(xcor, ycor)
        
        
        
        