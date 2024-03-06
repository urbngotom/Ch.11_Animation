import arcade
SW = 600
SH = 600

class Electron():
    def __init__(self, x, y, dx, dy, radius, color):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.radius = radius
        self.color = color

    def draw_electron(self):
        arcade.draw_circle_filled(self.x, self.y, self.radius, self.color)
        arcade.draw_circle_outline(self.x, self.y, self.radius, arcade.color.BLACK, 1)

    def update_electron(self):
        self.x += self.dx
        self.y += self.dy
        if self.x <= self.radius:
            self.dx *= 0
            self.dy = 5
        if self.y >= SH-self.radius:
            self.dx = 5
            self.dy *= 0
        if self.x >= SW-self.radius and self.y >= 500:
            self.dx *= 0
            self.dy = -5
        if self.y < self.radius:
            self.x = 670
            self.y = 25
            self.dx = -5
            self.dy = 0

class Lightbulb():
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw_lightbulb(self):
        arcade.draw_circle_filled(self.x, self.y, self.radius, self.color)
        arcade.draw_circle_outline(self.x, self.y, self.radius, arcade.color.BLACK, 1)

    def update_lightbulb_on(self):
        self.color = arcade.color.YELLOW
        arcade.set_background_color(arcade.color.LIGHT_YELLOW)

    def update_lightbulb_off(self):
        self.color = arcade.color.LIGHT_GRAY
        arcade.set_background_color(arcade.color.BLACK)


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)
        self.clock = 0
        self.timer = 0
        self.electron_list = []

        #electron instantiation
        pos_x = 625
        for i in range(50):
            self.electron = Electron(pos_x, 25, -5, 0, 25, arcade.color.BRONZE)
            self.electron_list.append(self.electron)
            pos_x += 50

        #lightbulb instantiation
        self.lightbulb = Lightbulb(300, 450, 100, arcade.color.LIGHT_GRAY)



    def on_draw(self):
        arcade.start_render()
        #copper wire
        arcade.draw_rectangle_filled(300, 25, SW, 50, arcade.color.ANTIQUE_BRASS)
        arcade.draw_rectangle_filled(300, SH-25, SW, 50, arcade.color.ANTIQUE_BRASS)
        arcade.draw_rectangle_filled(25, 300, 50, SH, arcade.color.ANTIQUE_BRASS)
        arcade.draw_rectangle_filled(SW-25, 300, 50, SH, arcade.color.ANTIQUE_BRASS)

        # electrons
        for electron in self.electron_list:
            electron.draw_electron()

        #battery
        arcade.draw_rectangle_filled(575, 25, 50, 50, arcade.color.BLACK_OLIVE)
        arcade.draw_rectangle_outline(575, 25, 50, 50, arcade.color.BLACK, 1)
        arcade.draw_rectangle_filled(525, 25, 50, 50, arcade.color.COPPER)
        arcade.draw_rectangle_outline(525, 25, 50, 50, arcade.color.BLACK, 1)
        arcade.draw_rectangle_filled(499, 25, 4, 15, arcade.color.SILVER)
        arcade.draw_rectangle_outline(499, 25, 4, 15, arcade.color.BLACK, 1)

        #lightbulb
        self.lightbulb.draw_lightbulb()

        # lightbulb socket
        arcade.draw_rectangle_filled(SW / 2, 570, 100, 64, arcade.color.GRAY)
        offset = 0
        y = 592
        for i in range(7):
            arcade.draw_line(250, y-offset, 350, y-offset, arcade.color.BLACK)
            offset += 8

    def on_update(self, dt):
        self.clock += dt

        #moving electrons
        for electron in self.electron_list:
            electron.update_electron()

        #flickering light
        if self.clock >= 5:
            self.lightbulb.update_lightbulb_on()
            self.timer += dt
        if self.timer >= 1:
            self.lightbulb.update_lightbulb_off()
        if self.timer >= 2:
            self.lightbulb.update_lightbulb_on()
            self.timer = 0




def main():
    window = MyGame(SW, SH, "Electricity!")
    arcade.run()

if __name__ == "__main__":
    main()