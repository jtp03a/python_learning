import Turtle

STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]

class Snake(Turtle):
  def __init__(self):
    self.snake_body = []
    self.create_snake()
    self.move_snake()

    def create_snake(self):
      for position in STARTING_POSITIONS:
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.snake_body.append(new_segment)

    def move_snake(self):
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
          new_x = self.snake_body[seg_num - 1].xcor()
          new_y = self.snake_body[seg_num - 1].ycor()
          self.snake_body[seg_num].goto(new_x, new_y)
          self.snake_body[0].forward(20)
