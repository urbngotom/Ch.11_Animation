'''
# 11.0 Jedi Training (50pts)  Name:________________



 
CHAPTER 11 FINAL CODE QUESTIONS: (10pts)
--------------------------------
1.) Where is the ball's original location?
The ball originally starts at (320, 240)

2.) What are the variables dx and dy?
dx is the horizontal velocity or change in x-pixels. dy is the vertical velocity or change in y-pixels.

3.) How many pixels/sec does the ball move in the x-direction?
180 pixels/sec

4.) How many pixels/sec does the ball move in the y-direction?
120 pixels/sec

5.) Which method is run 60 times/second?
MyGame.on_draw(self)

6.) What does this code do?   self.dx *= -1
Switches the x-direction of the object

7.) What does this code do?  self.pos_y += self.dy
Adds the change in y-pixels to the y-position. It makes the object move vertically.

8.) What is the width of the window?
640

9.) What is this code checking?  self.pos_y > SH - self.rad:
Checking if the ball's y-position is greater than the screen height - the radius of the ball. If this happens, this means the ball is going off screen at the top.

10.) What is this code checking? if self.pos_x < self.rad
Checking to see if the ball's x-position is smaller than the radius of the ball. If this happens, this means the ball is going off screen to the left.
'''






'''
30 BOX BOUNCE PROGRAM (20pts)
---------------------
You will want to incorporate lists to modify the
Ball Bounce Program to create the following:

1.) Screen size 600 x 600
2.) Draw four 30px wide side rails on all four sides of the window
3.) Make each side rail a different color.
4.) Draw 30 black boxes(squares) of random size from 10-50 pixels
5.) Animate them starting at random speeds from -300 to +300 pixels/second. 
6.) All boxes must be moving.
7.) Start all boxes in random positions between the rails.
8.) Bounce boxes off of the side rails when the box edge hits the side rail.
9.) When the box bounces change its color to the rail it just hit.
10.)Title the window 30 Boxes

Helpful Hints:
1.) When you initialize the MyGame class create an empty list called self.boxlist=[] to hold all of your boxes.
2.) Then use a for i in range(30): list to instantiate boxes and append them to the list.
3.) In the on_draw section use: for box in self.boxlist: box.draw_box()
4.) Also in the on_draw section draw the side rails.
5.) In the on_update section use: for box in self.boxlist: box.update_box()
'''
# import arcade
# import random
# SW = 600
# SH = 600
#
# class Box():
#     def __init__(self, x, y, dx, dy, box_size):
#         self.x = x
#         self.y = y
#         self.color = arcade.color.WHITE
#         self.dx = dx
#         self.dy = dy
#         self.box_size = box_size
#
#     def draw_box(self):
#         arcade.draw_rectangle_filled(self.x, self.y, self.box_size, self.box_size, self.color)
#
#
#     def update_box(self):
#         self.x += self.dx
#         self.y += self.dy
#
#         if self.x <= 30:
#             self.dx *= -1
#             self.color = arcade.color.WISTERIA
#         if self.x >= SW-30:
#             self.dx *= -1
#             self.color = arcade.color.FAWN
#         if self.y <= 30:
#             self.dy *= -1
#             self.color = arcade.color.LIGHT_BLUE
#         if self.y >= SH-30:
#             self.dy *= -1
#             self.color = arcade.color.LIGHT_GREEN
#
#
#
# class MyGame(arcade.Window):
#     def __init__(self, width, height, title):
#         super().__init__(width, height, title)
#         self.box_list = []
#         for i in range(30):
#             dx = random.randint(-5, 5)
#             dy = random.randint(-5, 5)
#             box_size = random.randint(10, 50)
#             position_x = random.randint(35, SW-35)
#             position_y = random.randint(35, SH-35)
#             self.box = Box(position_x, position_y, dx, dy, box_size)
#             self.box_list.append(self.box)
#
#
#     def on_draw(self):
#         arcade.start_render()
#         arcade.draw_rectangle_filled(0, SH / 2, SW / 20, SH, arcade.color.WISTERIA)
#         arcade.draw_rectangle_filled(SW / 2, 0, SW, SH / 20, arcade.color.LIGHT_BLUE)
#         arcade.draw_rectangle_filled(SW, SH / 2, SW / 20, SH, arcade.color.FAWN)
#         arcade.draw_rectangle_filled(SW / 2, SH, SW, SH / 20, arcade.color.LIGHT_GREEN)
#         for box in self.box_list:
#             box.draw_box()
#
#     def on_update(self, dt):
#         for box in self.box_list:
#             box.update_box()
#
# def main():
#     window = MyGame(SW, SH, "Drawing Example")
#     arcade.run()
#
#
# if __name__ == "__main__":
#     main()






'''
SNOWFALL  (20pts)
--------
Try to create the snowfall animation by meeting
the following requirements:

1.) Create a 600 x 600 window with black background
2.) Window title equals "Snowfall"
3.) Crossbars 10 px wide. Snow must be outside!
4.) Make snowflake radius random between 1-3
5.) Randomly start snowflakes anywhere in the window.
6.) Random downward speed of -4 to -1
7.) Start snowflakes again at random x from 0-600 and random y from 600-700
8.) Generate 300 snowflakes
9.) Color snowflake #1 red just for fun.
10.) All other snowflakes should be white.
'''

# import arcade
# import random
# SW = 600
# SH = 600
#
# class Snowflake():
#     def __init__(self, x, y, dy, radius, color):
#         self.x = x
#         self.y = y
#         self.dy = dy
#         self.radius = radius
#         self.color = color
#
#     def draw_flake(self):
#         arcade.draw_circle_filled(self.x, self.y, self.radius, self.color)
#
#     def update_flake(self):
#         self.y += self.dy
#         if self.y < 0:
#             self.y = random.randint(600, 700)
#             self.x = random.randint(0, 600)
#
# class MyGame(arcade.Window):
#     def __init__(self, width, height, title):
#         super().__init__(width, height, title)
#         arcade.set_background_color(arcade.color.BLACK)
#         self.flake_list = []
#         for i in range(300):
#             radius = random.randint(1, 3)
#             dy = random.randint(-4, -1)
#             position_x = random.randint(radius, SW-radius)
#             position_y = random.randint(radius, SH-radius)
#             color = arcade.color.WHITE
#             if i == 0:
#                 color = arcade.color.RED
#             self.flake = Snowflake(position_x, position_y, dy, radius, color)
#             self.flake_list.append(self.flake)
#
#
#     def on_draw(self):
#         arcade.start_render()
#         for flake in self.flake_list:
#             flake.draw_flake()
#         arcade.draw_rectangle_filled(SW/2, SH/2, SW/60, SH, arcade.color.BROWN)
#         arcade.draw_rectangle_filled(SW / 2, SH / 2, SW, SH/60, arcade.color.BROWN)
#
#
#     def on_update(self, dt):
#         for flake in self.flake_list:
#             flake.update_flake()
#
# def main():
#     window = MyGame(SW, SH, "Snowfall")
#     arcade.run()
#
# if __name__ == "__main__":
#     main()