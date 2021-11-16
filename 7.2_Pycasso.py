'''
PYCASSO PROJECT
---------------
Your job is to make a cool picture. /
You must use multiple colors. /
You must have a coherent picture. No abstract art with random shapes. /
You must use multiple types of graphic functions (e.g. circles, rectangles, lines, etc.)
Somewhere you must include a WHILE or FOR loop to create a repeating pattern. /
Do not just redraw the same thing in the same location 10 times. /
You can contain multiple drawing commands in a loop, so you can draw multiple train cars for example. /
Please use comments and blank lines to make it easy to follow your program. /
If you have 5 lines that draw a robot, group them together with blank lines above and below. /
Then add a comment at the top telling the reader what you are drawing. /
IN THE WINDOW TITLE PLEASE PUT YOUR NAME./
When you are finished Pull Request your file to your instructor.
'''
# PAC-MAN w/ Pellets

ScreenW = 640
ScreenH = 480

import arcade # import drawing library

arcade.open_window(ScreenW, ScreenH, "Joseph Jarman") # Make a window
arcade.set_background_color((0, 0, 0)) # Black background
arcade.start_render() # Start drawing
arcade.draw_arc_filled(100, ScreenH/2, 50, 50, arcade.color.YELLOW, 35, 325) # PAC-MAN
for i in range(7, ScreenW+1, 20):
    arcade.draw_circle_filled(i+115, ScreenH/2, 3, arcade.color.WHITE) # Pellets
arcade.draw_rectangle_outline(ScreenW/2, ScreenH/2+50, ScreenW, 25, arcade.color.BLUE) # Top wall
arcade.draw_rectangle_outline(ScreenW/2, ScreenH/2-50, ScreenW, 25, arcade.color.BLUE) # Bottom wall
arcade.draw_text("High Score: 256", ScreenH/2, 440, (255, 255, 255), font_name="Kenney Pixel", font_size=25) # HIGH SCORE!
arcade.draw_text("1UP: 00", 10, 440, (255, 255, 255), font_name="Kenney Pixel", font_size=25) # 1UP Progress
arcade.finish_render() # Complete drawing
arcade.run() # render to the window, and show the user
