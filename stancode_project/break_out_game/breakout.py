"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    original_x = graphics.ball.x
    original_y = graphics.ball.y
    lives = NUM_LIVES
    dx = graphics.get_dx()
    dy = graphics.get_dy()
    # Add the animation loop here!
    while True:
        graphics.renew_label()
        # assign dx and dy when the user click the mouse
        if dx == 0 and dy == 0:
            dx = graphics.get_dx()
            dy = graphics.get_dy()
        # keep the ball moving
        graphics.ball.move(dx, dy)
        pause(FRAME_RATE)
        graphics.get_object(graphics.ball.x, graphics.ball.y)
        if graphics.get_object(graphics.ball.x, graphics.ball.y) is not None:
            if graphics.remove_object():
                # remove the object and bounce only once
                if dy < 0:
                    dy = -dy
            if graphics.get_object(graphics.ball.x, graphics.ball.y) is graphics.paddle:
                # if the ball y is inside the paddle, then it will bounce only once
                if dy > 0:
                    dy = -dy
                if graphics.ball.x < 0 or graphics.ball.x > graphics.window.width - graphics.ball.width:
                    dx = graphics.set_new_speed()
                    dx = -dx
            else:
                dy = -dy
                if graphics.ball.x < 0 or graphics.ball.x > graphics.window.width - graphics.ball.width:
                    dx = graphics.set_new_speed()
                    dx = -dx
                if graphics.ball.y > 0:
                    graphics.remove_object()
                    if graphics.ball.y <= 0:
                        # if the ball is inside the boarder, then the ball will only bounce once
                        if dy > 0:
                            dy = -dy
                    else:
                        dy = dy
        if graphics.ball.x < 0:
            # left boarder
            dx = graphics.set_new_speed()
            # if the ball is inside the boarder, then the ball will only bounce once
            if dx < 0:
                dx = -dx
        if graphics.ball.x > graphics.window.width - graphics.ball.width:
            # right boarder
            dx = graphics.set_new_speed()
            # if the ball is inside the boarder, then the ball will only bounce once
            if dx > 0:
                dx = -dx
        if graphics.ball.y < 0:
            # top boarder
            # if the ball is inside the boarder, then the ball will only bounce once
            if dy < 0:
                dy = -dy
        if graphics.ball.y > graphics.window.height - graphics.ball.height:
            # bottom
            graphics.ball.move(original_x - graphics.ball.x, original_y - graphics.ball.y)
            lives -= 1
            graphics.reset()
            # get the new dx and dy after reset function
            dx = graphics.get_dx()
            dy = graphics.get_dy()
            if lives == 0:
                graphics.ball.move(original_x - graphics.ball.x, original_y - graphics.ball.y)
                graphics.game_over()
                break
        if graphics.deleted_bricks == graphics.brick_col*graphics.brick_rows:
            graphics.ball.move(original_x - graphics.ball.x, original_y - graphics.ball.y)
            graphics.game_over()
            break


if __name__ == '__main__':
    main()
