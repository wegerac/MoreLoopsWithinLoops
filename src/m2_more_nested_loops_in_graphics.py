"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Andrew Weger.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to test them. """
    run_test_draw_upside_down_wall()


def run_test_draw_upside_down_wall():
    """ Tests the    draw_upside_down_wall    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, 'Upside-down wall, Tests 1 and 2')

    rectangle = rg.Rectangle(rg.Point(125, 230), rg.Point(155, 250))
    draw_upside_down_wall(rectangle, 8, window)

    rectangle = rg.Rectangle(rg.Point(375, 175), rg.Point(425, 225))
    draw_upside_down_wall(rectangle, 4, window)

    window.close_on_mouse_click()


def draw_upside_down_wall(rectangle, n, window):
    """
    See   MoreWalls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an "upside-down wall" on the given window, where:
      -- The BOTTOM of the wall is a single "brick"
            that is the given rg.Rectangle.
      -- There are n rows in the wall.
      -- Each row is a row of "bricks" that are the same size
            as the given rg.Rectangle.
      -- Each row has one more brick than the row below it.
      -- Each row is centered on the bottom row.

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is nonnegative.
    """
    # ------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #     Some tests are already written for you (above).
    # ------------------------------------------------------------------
    movex = rectangle.get_upper_right_corner().x - rectangle.get_lower_left_corner().x
    movey = rectangle.get_upper_right_corner().y - rectangle.get_lower_left_corner().y
    p1 = rectangle.get_lower_left_corner()
    p2 = rectangle.get_upper_right_corner()
    rectangle.attach_to(window)
    window.render()
    for k in range(n):
        for x in range(k + 1):
            xmov = (x * movex)/2
            ymov = x * movey
            p1r = rg.Point(p1.x - xmov, p1.y + ymov)
            p2r = rg.Point(p2.x - xmov, p2.y + ymov)
            rect = rg.Rectangle(p1r,p2r)
            rect.attach_to(window)
            window.render()
        np1 = rect.get_upper_right_corner()
        np2 = rect.get_lower_left_corner()
        for j in range(k):

            np1.x  = np1.x + movex
            np2.x = np2.x + movex
            new = rg.Rectangle(np1, np2)
            new.attach_to(window)
            window.render()



# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
