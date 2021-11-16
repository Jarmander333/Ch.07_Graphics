'''
FLAG PROJECT
---------------
Make your flag 260 pixels tall
Use the scaling image on the website to determine other dimensions
The hexadecimal colors for the official flag are red:#BF0A30 and blue:#002868
Title the window, "The Stars and Stripes"
I used a draw_text command and used 20 pt. asterisks for the stars.
We will have a competition to see who can make this flag in the least lines of code.
The record is 16! You will have to use some loops to achieve this.
'''
#imports
import arcade
#variable
y = 260
x = y * 1.9
stripe = 0.0769 * y
v = 10
m = 40
c = y * 0.5385
d = y * 0.76
#make window
arcade.open_window(x, y, "The Stars and Stripes")
#set background color to white
arcade.set_background_color(arcade.color.WHITE)
# start window rendering
arcade.start_render()
#make 13 stripes
for i in range(v, y+1, m):
    arcade.draw_line(0, i, x, i, (191, 10, 48), stripe)
#make blue rectangle
arcade.draw_lrtb_rectangle_filled(0, d, y, y - c, (0, 40, 104))
for i in range(7, 10, 10):
    arcade.draw_text("*", y-10, i, arcade.color.WHITE, font_size=12)
arcade.finish_render()
arcade.run()
