from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super(Paddle, self).__init__()
        self.shape("triangle")
        self.color("green")
        self.shapesize(5,1)
        self.penup()
        self.goto(0,-260)
        self.left(90)


    def move_right(self):
        if self.xcor() < 420:
            x = self.xcor()
            self.goto(x+20,-260)

    def move_left(self):
        if self.xcor() > -420:
            x = self.xcor()
            self.goto(x - 20, -260)