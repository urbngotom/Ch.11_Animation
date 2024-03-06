'''
ANIMATION PROJECT
-----------------
Your choice!!! Have fun and be creative.

'''
import arcade
import random
SW = 600
SH = 600

class Rain():
    def __init__(self, x, y, dy, droplet_length, color):
        self.x = x
        self.y = y
        self.dy = dy
        self.droplet_length = droplet_length
        self.color = color

    def draw_rain(self):
        arcade.draw_line(self.x, self.y, self.x, self.y + self.droplet_length, self.color)

    def update_rain(self):
        self.y += self.dy
        if self.y < 0:
            self.y = random.randint(600, 700)
            self.x = random.randint(0, 600)

class Clouds():
    def __init__(self, x, y, dx, radius, color):
        self.x = x
        self.y = y
        self.dx = dx
        self.radius = radius
        self.color = color

    def draw_clouds(self):
        arcade.draw_circle_filled(self.x, self.y, self.radius, self.color)

    def update_clouds(self):
        self.x += self.dx
        if self.x >= SW + self.radius:
            self.x = -70

class Lightning():
    def __init__(self, x, dx):
        self.x = x
        self.dx = dx
        self.color = arcade.color.DARK_MIDNIGHT_BLUE

    def draw_lightning(self):
        point_list = ((self.x, 600), (self.x-40, 400), (self.x, 300), (self.x-20, 200), (self.x+80, 300), (self.x+40, 400), (self.x+80, 600))
        arcade.draw_polygon_filled(point_list, self.color)

    def update_lightning(self):
        self.x += self.dx
        if self.x+80 > SW or self.x-40 < 0:
            self.dx *= -1

        for i in range(100):
            strike_chance = random.randint(1, 10)
            if strike_chance == 10:
                self.color = arcade.color.YELLOW
                arcade.set_background_color(arcade.color.WHITE)

            else:
                self.color = arcade.color.DARK_MIDNIGHT_BLUE
                arcade.set_background_color(arcade.color.DARK_MIDNIGHT_BLUE)

class Building_Windows():
    def __init__(self):
        self.foreground_window_color = (230, 231, 161)
        self.background_window_color = (161, 158, 124)

    def draw_windows(self):
        #foreground building windows
        for i in range(4):
            ywindow_offset = 250
            if i == 0:
                xwindow_offset = 35
            else:
                xwindow_offset = 30 + 180 * i
            for i in range(2):
                for i in range(4):
                    arcade.draw_rectangle_filled(xwindow_offset, ywindow_offset, 30, 50, self.foreground_window_color)
                    arcade.draw_line(xwindow_offset - 15, ywindow_offset, xwindow_offset + 15, ywindow_offset,
                                     arcade.color.BLACK)
                    arcade.draw_line(xwindow_offset, ywindow_offset - 25, xwindow_offset, ywindow_offset + 25,
                                     arcade.color.BLACK)
                    ywindow_offset -= 80

        #background building windows
        for i in range(3):
            ywindow_offset = 350
            if i == 0:
                xwindow_offset = 120
            else:
                xwindow_offset = 120 + 180 * i
            for i in range(2):
                for i in range(4):
                    arcade.draw_rectangle_filled(xwindow_offset, ywindow_offset, 90, 50, self.background_window_color)
                    arcade.draw_line(xwindow_offset - 45, ywindow_offset, xwindow_offset + 45, ywindow_offset,
                                     arcade.color.BLACK)
                    arcade.draw_line(xwindow_offset, ywindow_offset - 25, xwindow_offset, ywindow_offset + 25,
                                     arcade.color.BLACK)
                    ywindow_offset -= 80
    def update_windows(self):
        self.foreground_window_color = arcade.color.DIM_GRAY
        self.background_window_color = arcade.color.EERIE_BLACK

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.DARK_MIDNIGHT_BLUE)
        self.clock = 0

        #cloud initalization
        self.clouds_list = []
        x = -640
        for i in range(9):
            self.clouds = Clouds(x, SH, 5, 70, arcade.color.GRAY)
            self.clouds_list.append(self.clouds)
            x += 80

        #rain inititalization
        self.rain_list = []
        for i in range(300):
            radius = random.randint(1, 3)
            dy = random.randint(-4, -1)
            position_x = random.randint(0, 600)
            position_y = random.randint(0, 600)
            droplet_length = random.randint(10, 40)
            color = arcade.color.BLUE
            self.rain = Rain(position_x, position_y, dy, droplet_length, color)
            self.rain_list.append(self.rain)


        #lightning initialization
        self.lightning = Lightning(300, 2)

        #windows initialization
        self.windows = Building_Windows()


    def on_draw(self):
        arcade.start_render()
        self.lightning.draw_lightning()

        #rectangular buildings in foreground
        offset = 30
        for i in range(4):
            arcade.draw_rectangle_filled(offset, 50, 90, 500, (55, 55, 55))
            offset += 180

        #rectangular buildings in background
        offset = 120
        for i in range(3):
            arcade.draw_rectangle_filled(offset, 50, 90, 700, (40, 40, 40))
            offset += 180

        self.windows.draw_windows()

        for rain in self.rain_list:
            rain.draw_rain()

        for clouds in self.clouds_list:
            clouds.draw_clouds()


    def on_update(self, dt):
        self.clock += dt

        for rain in self.rain_list:
            rain.update_rain()

        for clouds in self.clouds_list:
            clouds.update_clouds()

        if self.clock >= 7:
            self.lightning.update_lightning()
        if self.clock >= 8:
            self.windows.update_windows()


def main():
    window = MyGame(SW, SH, "Tommy Ngo - Blackout")
    arcade.run()

if __name__ == "__main__":
    main()