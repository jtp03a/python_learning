from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")

running = True

while running:
  s.update()
  time.sleep(0.1)

  snake.move_snake()

# Detect collision with food
  if snake.snake_head.distance(food) < 15:
    scoreboard.inc_score()
    food.rand_loc()
    snake.inc_snake()

# Detect collision with wall
  if snake.snake_head.xcor() > 295 or snake.snake_head.xcor() < -295 or snake.snake_head.ycor() > 295 or snake.snake_head.ycor() < -295:
    running = False
    scoreboard.game_over()

# Detect collision with tail
  for segment in snake.snake_body[1:]:
    if snake.snake_head.distance(segment) < 10:
      running = False
      scoreboard.game_over()



  
  

# snake_body = []
# current_snake_length = 3

# x_pos = 0

# for _ in range(current_snake_length):
#   snake_body.append(Snake_Turtle(shape="square", color="white", speed="fastest"))

# for segment in snake_body:
#   segment.penup()
#   segment.goto(x_pos, 0)
#   x_pos -= 20

# s.update()

# snake_is_moving = True

# while snake_is_moving:
#   s.update()
#   time.sleep(0.1)
  



s.exitonclick()