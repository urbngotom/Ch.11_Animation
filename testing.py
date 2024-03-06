import arcade
import random
SW = 640
SH = 480

class Ball():
    def __init__(self, x, y, dx, dy, radius, color):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.radius = radius
        self.color = color

    def draw_ball(self):
        arcade.draw_circle_filled(self.x, self.y, self.radius, self.color)

    def update_ball(self):
        self.x += self.dx
        self.y += self.dy

        if self.x <= self.radius or self.x >= SW-self.radius:
            self.dx *= -1
        if self.y <= self.radius or self.y >= SH-self.radius:
            self.dy *= -1

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ASH_GREY)
        self.ball_list = []
        for i in range(200):
            radius = random.randint(10, 30)
            dx = random.randrange(-5, 6, 2)
            dy = random.randrange(-5, 6, 2)
            position_x = random.randint(radius, SW-radius)
            position_y = random.randint(radius, SH-radius)
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.ball = Ball(position_x, position_y, dx, dy, radius, color)
            self.ball_list.append(self.ball)


    def on_draw(self):
        arcade.start_render()
        for ball in self.ball_list:
            ball.draw_ball()

    def on_update(self, dt):
        for ball in self.ball_list:
            ball.update_ball()

def main():
    window = MyGame(SW, SH, "Drawing Example")
    arcade.run()

if __name__ == "__main__":
    main()