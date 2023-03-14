from turtle import Turtle
class Bullet(Turtle):
    def __init__(self):
        super(Bullet, self).__init__()
        self.color("purple")
        self.penup()
        self.right(90)
        self.enemies_bullet = []
        self.player_bullet = []
        self.move()
        self.player_shot()

    def move(self):
        self.forward(2)

    def player_shot(self) -> object:
        new_bullet = Turtle()
        new_bullet.right(180)
        new_bullet.color("lightgreen")
        self.player_bullet.append(new_bullet)


