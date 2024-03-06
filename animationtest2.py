import arcade
import random
SW = 600
SH = 600

class Car():
    def __init__(self, x, y, dx, dy, rotate):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.rotate = rotate
        self.color = [random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)]

    def draw_car(self):
        arcade.draw_rectangle_filled(self.x, self.y, 50, 100, self.color, self.rotate)

    def update_car(self):
        self.y += self.dy
        self.x += self.dx
        if self.y >= 700:
            self.x = 650
            self.y = 300
            self.dy = 0
            self.dx = -5
            self.rotate = 90
        if self.x <= -100:
            self.dy = 5
            self.dx = 0
            self.x = 300
            self.y = -50
            self.rotate = 0



class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.RED)
        self.clock = 0
        self.car_list = []

        #car instantiation
        for i in range(-100, -1800, -300):
            self.car = Car(300, i, 0, 5, 0)
            self.car_list.append(self.car)


    def on_draw(self):
        arcade.start_render()
        #road
        arcade.draw_rectangle_filled(300, 300, 50, SH, arcade.color.BLACK)
        arcade.draw_rectangle_filled(300, 300, SW, 50, arcade.color.BLACK)

        #cars
        for car in self.car_list:
            car.draw_car()


    def on_update(self, dt):
        self.clock += dt

        #moving cars
        for car in self.car_list:
            car.update_car()

        #flickering background
        if self.clock >= 1:
            arcade.set_background_color(arcade.color.BLUE)
        if self.clock >= 2:
            arcade.set_background_color(arcade.color.WHITE)
        if self.clock >= 3:
            arcade.set_background_color(arcade.color.RED)
            self.clock = 0




def main():
    window = MyGame(SW, SH, "UHS PARKING LOT!")
    arcade.run()

if __name__ == "__main__":
    main()