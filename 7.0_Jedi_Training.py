#Sign your name:________________

'''
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PUCK-MAN.
'''
import arcade

GraphW = 500
GraphH = 400
arcade.open_window(GraphW, GraphH, "Jedi Training Ch.07-01")
arcade.set_background_color(arcade.color.ALMOND)
arcade.start_render()
for x in range(0, GraphW+1, 20):
    arcade.draw_line(x, 0, x, GraphH, (0, 0, 0))
for y in range(0, GraphH+1, 20):
    arcade.draw_line(0, y, GraphW, y, (0, 0, 0))
arcade.draw_circle_filled(GraphW-40, 10, 3, arcade.color.RED)
arcade.draw_circle_filled(GraphW/2, GraphH/2, 40, arcade.color.WISTERIA)
arcade.draw_rectangle_filled(50, GraphH-30, 60, 20, arcade.color.PHLOX)
arcade.draw_rectangle_filled(200, 260, 40, 20, arcade.color.BLUSH, -45)
arcade.draw_line(80, 20, 120, 60, arcade.color.BLUE)
arcade.draw_text("I love you, I know", 20, 175, arcade.color.BRICK_RED, font_size=20)
arcade.draw_ellipse_filled(100, 100, 120, 40, arcade.color.AMBER)
arcade.draw_arc_filled(400, 320, 120, 120, arcade.color.YELLOW, 35, 325)
arcade.finish_render()
arcade.run()
