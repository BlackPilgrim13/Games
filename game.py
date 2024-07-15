import turtle
import time
import snake
import food
import scoreboard


myscreen = turtle.Screen()
myscreen.setup(width = 600, height = 600)
myscreen.bgcolor("white")
myscreen.title("My Snake Game")
myscreen.tracer(0)

snake = snake.Snake()
food = food.Food()
scoreboard = scoreboard.ScoreBoard()

myscreen.listen()
myscreen.onkey(snake.up, "Up")
myscreen.onkey(snake.down, "Down")
myscreen.onkey(snake.left, "Left")
myscreen.onkey(snake.right, "Right")

game_on = True

while game_on:
    myscreen.update()
    time.sleep(0.1)
    snake.move()
        
    if snake.segments[0].distance(food) < 15:
        snake.extend()
        food.refresh()
        scoreboard.increase_score()
        
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        scoreboard.game_over()
        game_on = False
    
    for segment in snake.segments:
        if segment == snake.segments[0]:
            pass
        
        elif snake.segments[0].distance(segment) < 10:
            game_on = False
            scoreboard.reset()
            snake.reset()




































myscreen.exitonclick()