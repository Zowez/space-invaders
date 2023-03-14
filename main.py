import time
import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Space Invaders")
screen.setup(800, 800)
screen.tracer(0)


border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.forward(600)
    border_pen.left(90)
border_pen.hideturtle()


level_red_enemies = []
red_x = -250
red_y = 250
for i in range(11):

    new_enemy = turtle.Turtle()
    new_enemy.shape("turtle")
    new_enemy.shapesize(1.5, 1.5)
    new_enemy.penup()
    new_enemy.color("red")
    new_enemy.right(90)
    level_red_enemies.append(new_enemy)
    new_enemy.setposition(red_x, red_y)
    red_x = red_x + 40

level_orange_enemies = []
orange_x = -250
orange_y = 200
for i in range(11):

    new_enemy = turtle.Turtle()
    new_enemy.shape("turtle")
    new_enemy.shapesize(1.5, 1.5)
    new_enemy.penup()
    new_enemy.color("orange")
    new_enemy.right(90)
    level_orange_enemies.append(new_enemy)
    new_enemy.setposition(orange_x, orange_y)
    orange_x = orange_x + 40


level_yellow_enemies = []
yellow_x = -250
yellow_y = 150
for i in range(11):

    new_enemy = turtle.Turtle()
    new_enemy.shape("turtle")
    new_enemy.shapesize(1.5, 1.5)
    new_enemy.penup()
    new_enemy.color("yellow")
    new_enemy.right(90)
    level_yellow_enemies.append(new_enemy)
    new_enemy.setposition(yellow_x, yellow_y)
    yellow_x = yellow_x + 40


enemies = []
enemies.extend(level_red_enemies)
enemies.extend(level_orange_enemies)
enemies.extend(level_yellow_enemies)


player = turtle.Turtle()
player.left(90)
player.shape("triangle")
player.shapesize(4, 1)
player.color("green")
player.penup()
player.goto(0, -250)

bullets = []

def player_move_left():
    if player.xcor() > -250:
        player.goto(player.xcor()-10, player.ycor())

def player_move_right():
    if player.xcor() < 250:
        player.goto(player.xcor() + 10, player.ycor())

def player_shot():
    for b in bullets:
        if b.color() == ('lightgreen', 'lightgreen'):
            return 0
    new_bullet = turtle.Turtle()
    new_bullet.shapesize(1, 1)
    new_bullet.speed(0)
    new_bullet.left(90)
    new_bullet.penup()
    new_bullet.setposition(player.xcor(), player.ycor()+20)
    new_bullet.color("lightgreen")
    new_bullet.speed(3)
    bullets.append(new_bullet)

def enemies_shot():
    r = random.randint(1, 150)
    e = random.choice(enemies)
    if r == 2:

        new_bullet = turtle.Turtle()
        new_bullet.shapesize(1, 1)
        new_bullet.speed(0)
        new_bullet.right(90)
        new_bullet.penup()
        new_bullet.setposition(e.xcor(), e.ycor() + 20)
        new_bullet.color("pink")
        new_bullet.speed(3)
        bullets.append(new_bullet)

def bullet_move():
    for b in bullets:
        b.forward(5)


game_is_on = True

screen.listen()

screen.onkeypress(fun=player_move_right, key="Right")
screen.onkeypress(fun=player_move_left, key="Left")
screen.onkeypress(fun=player_shot, key="space")


move_speed = 1
collision = 0


heart_v = 3
heart = turtle.Turtle()
heart.penup()
heart.hideturtle()
heart.goto(250, 300)
heart.color("red")

score_v = 0
score = turtle.Turtle()
score.penup()
score.hideturtle()
score.goto(-250, 300)
score.color("white")


while game_is_on:
    heart.clear()
    score.clear()

    screen.update()
    time.sleep(0.01)

    for enemy in enemies:
        if enemy.xcor() > 270:
            move_speed = move_speed * -1
            collision = collision + 1

        if enemy.xcor() < -270:
            move_speed = move_speed * -1
            collision = collision + 1

    for enemy in enemies:
        if (collision/3) % 5 == 0 and collision != 0:
            enemy.goto(enemy.xcor() + move_speed, enemy.ycor()-30)
        else:
            enemy.goto(enemy.xcor() + move_speed, enemy.ycor())
    if (collision / 3) % 5 == 0 and collision != 0:
        collision = 0
        if move_speed > 0:
            move_speed = move_speed + 1
        if move_speed < 0:
            move_speed = move_speed - 1

    for enemy in enemies:
        for bullet in bullets:
            if bullet.color() == ('lightgreen', 'lightgreen') and enemy.distance(bullet) < 30:
                if enemy.color() == ('red', 'red'):
                    score_v = score_v + 3
                if enemy.color() == ('orange', 'orange'):
                    score_v = score_v + 2
                if enemy.color() == ('yellow', 'yellow'):
                    score_v = score_v + 1
                enemy.hideturtle()
                enemies.remove(enemy)
                bullet.reset()
                bullets.remove(bullet)

    for bullet in bullets:
        if bullet.ycor() > 300 or bullet.ycor() < -300:
            bullet.reset()
            bullets.remove(bullet)

    for bullet in bullets:
        if bullet.distance(player) < 45 and bullet.ycor() == player.ycor() + 10 and bullet.color() == ("pink", "pink"):
            heart_v = heart_v - 1
            player.goto(0, -250)
    for enemy in enemies:
        if enemy.distance(player) == 30:
            heart_v = 0

    if heart_v == 0:
        game_is_on = False
        game_over = turtle.Turtle()
        game_over.penup()
        game_over.hideturtle()
        game_over.color("blue")
        game_over.write("GAME OVER!", align="center", font=("Courier", 60, "bold"))

    heart.write(f"Heart:{heart_v}", align="center", font=("Courier", 40, "normal"))
    score.write(f"Score:{score_v}", align="center", font=("Courier", 40, "normal"))
    enemies_shot()
    bullet_move()


screen.exitonclick()
