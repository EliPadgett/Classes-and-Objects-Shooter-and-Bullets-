from turtle import *
import random

def generate_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"

def playing_area():
    pen = Turtle()
    pen.ht()
    pen.speed(0)
    pen.color('teal')
    pen.begin_fill()
    pen.goto(-240,240)
    pen.goto(240,240)
    pen.goto(240,-240)
    pen.goto(-240,-240)
    pen.goto(-240,240)
    pen.end_fill()
    
class Player(Turtle):
    def __init__(self, x, y, playercolor, screen, right_key, left_key, fire_key, health):
        super().__init__()
        self.ht()
        self.speed(0)
        self.color(playercolor)
        self.playercolor = playercolor
        self.penup()
        self.goto(x,y)
        self.setheading(90)
        self.shape("turtle")
        self.bullets = []
        self.alive = True
        self.color = color
        self.st()
        self.health = 3
        screen.onkeypress(self.turn_left, left_key)
        screen.onkeypress(self.turn_right, right_key)
        screen.onkeypress(self.fire, fire_key)

    def fire(self):
        self.bullets.append(Bullet(self))

    def turn_left(self):
        self.left(10)

    def turn_right(self):
        self.right(10)

    def move(self):
        self.forward(4)
        if self.xcor() > 230 or self.xcor() < -230:
            self.setheading(180 - self.heading())
        if self.ycor() > 230 or self.ycor() < -230:
            self.setheading(-self.heading())
    

class Bullet(Turtle):
    def __init__(self, player):
        super().__init__()
        self.ht()
        self.speed(0)
        self.shape("triangle")
        self.pu()
        self.goto(player.xcor(),player.ycor())
        self.color(player.playercolor)
        self.setheading(player.heading())
        self.forward(15)
        self.player = player
        self.showturtle()

    def move(self):
        self.forward(10)
        if self.xcor() > 230 or self.xcor() < -230 or self.ycor() > 230 or self.ycor() < -230:
            self.kill()
    
    def kill(self):
        if self in self.player.bullets:
            self.ht()
            self.player.bullets.remove(self)


screen = Screen()
screen.bgcolor("black")
screen.setup(520,520)
# Key Binding. Connects key presses and mouse clicks with function calls
screen.listen()


playing_area()

p1 = Player(-100, 0, "red",screen, "d", "a",'space')
p2 = Player(100,0,"blue",screen, "Right","Left",'/')

while p1.alive and p2.alive:
    p1.move()
    for bullet in p1.bullets:
        bullet.move()
        if bullet.distance(p2) <=20:
            bullet.ht()
            p1.bullets.remove(bullet)
            p2.health -= 1
    p2.move()
    for bullet in p2.bullets:
        bullet.move()
        if bullet.distance(p1) <=20:
            bullet.ht()
            p2.bullets.remove(bullet)
            p1.health -= 1
    



screen.exitonclick()