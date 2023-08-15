'''
# 11.0 Jedi Training (50pts)  Name:________________
 
CHAPTER 11 FINAL CODE QUESTIONS: (10pts)
--------------------------------
1.) Where is the ball's original location?

2.) What are the variables dx and dy?

3.) How many pixels/sec does the ball move in the x-direction?

4.) How many pixels/sec does the ball move in the y-direction?

5.) Which method is run 60 times/second?

6.) What does this code do?   self.dx *= -1

7.) What does this code do?  self.pos_y += self.dy

8.) What is the width of the window?

9.) What is this code checking?  self.pos_y > SH - self.rad:

10.) What is this code checking? if self.pos_x < self.rad
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
