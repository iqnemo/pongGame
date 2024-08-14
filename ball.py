from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("White")
        self.penup()
        self.shape("circle")
        self.x_move = 10
        self.y_move = 10

    def move(self):
        xpos = self.xcor() + self.x_move
        ypos = self.ycor() + self.y_move
        self.goto(xpos, ypos)

    def bounce_y(self):
        self.y_move *= -1


    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
