from turtle import Turtle, Screen
import time
from snake_class import Snake
from food_class import Food


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)

snake = Snake()
snake.design()

food = Food()
game_on = True

score = 0

score_turtle = Turtle()
score_turtle.penup()
score_turtle.goto(0, 270)
score_turtle.color('white')
score_turtle.write(f"Score: {score}", align='center', font = ('Arial', 20, 'bold'))

while game_on:

    for i in snake.turtles[1:-1]:
    
        if snake.turtles[0].distance(i) <=5:

            game_on = False


    score_turtle.hideturtle()
   
    screen.update()
    
    snake.move()
    
    if snake.turtles[0].distance(food.position()) <= 20:
    
        score_turtle.hideturtle()
        
        food.hideturtle()
        food = Food()
        
        score +=1
        
        score_turtle.color('white')
        score_turtle.clear()
        score_turtle.showturtle()
        score_turtle.write(f"Score: {score}", align='center', font = ('Arial', 20, 'bold'))
        score_turtle.goto(0, 270)
    
        snake.grow()
        
    if snake.turtles[0].xcor() <= -280 or snake.turtles[0].xcor() >= 280:
        game_on = False
    
    elif snake.turtles[0].ycor() <= -280 or snake.turtles[0].ycor() >= 280:
        game_on = False
    

    time.sleep(0.1)
   
    screen.listen()
    screen.onkeypress(snake.up, "Up")
    screen.onkeypress(snake.down, "Down")
    screen.onkeypress(snake.left, "Left")
    screen.onkeypress(snake.right, "Right")

print(f'{score}')

screen.bye()
