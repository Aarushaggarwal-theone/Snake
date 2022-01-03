from turtle import Turtle
from food_class import Food

x_cor = 20
class Snake():
    
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