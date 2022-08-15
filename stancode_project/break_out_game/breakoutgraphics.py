"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random


BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        self.maybe_object_1 = None
        self.maybe_object_2 = None
        self.maybe_object_3 = None
        self.maybe_object_4 = None
        self.paddle_vx = None
        self.paddle_dx = None
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title= 'breakout')
        row_color = 'red'
        self.paddle_offset = paddle_offset
        self.paddle_height = paddle_height
        self.brick_rows = brick_rows
        self.brick_col = brick_cols
        # Draw bricks
        self.deleted_bricks = 0
        for i in range(self.brick_rows):
            for j in range(self.brick_col):
                # rainbow color
                if i == 2:
                    row_color = 'orange'
                if i == 4:
                    row_color = 'yellow'
                if i == 6:
                    row_color = 'green'
                if i == 8:
                    row_color = 'blue'
                if i == 10:
                    row_color = 'indigo'
                if i == 12:
                    row_color = 'purple'
                self.bricks = GRect(width=brick_width, height=brick_height,
                                    x=0+brick_width*j+brick_spacing*j, y=brick_offset+brick_height*i+brick_spacing*i)
                self.bricks.filled = True
                self.bricks.fill_color = row_color
                self.bricks.color = self.bricks.fill_color
                self.window.add(self.bricks)
        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height, x=window_width/2-paddle_width/2, y=window_height-paddle_offset)
        self.paddle.filled = True
        self.window.add(self. paddle)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2, x=window_width/2-ball_radius, y=window_height/2-ball_radius)
        self.ball.filled = True
        self.window.add(self.ball)
        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        # Initialize our mouse listeners
        self.has_turned_on = False
        onmousemoved(self.paddle_move)
        onmouseclicked(self.set_ball_speed)
        self.label = GLabel(self.deleted_bricks)
        self.window.add(self.label, x=0, y=self.label.height)

    def renew_label(self):
        self.label.text = self.deleted_bricks

    def set_ball_speed(self, mouse):
        # only the first click will start the function to reset __dx and __dy
        if self.has_turned_on is False:
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx
            self.__dy = INITIAL_Y_SPEED
            self.has_turned_on = True

    def reset(self):
        self.__dx = 0
        self.__dy = 0
        self.has_turned_on = False

    def set_new_speed(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        return self.__dx

    def get_dx(self):
        # getter to get __dx for user
        return self.__dx

    def get_dy(self):
        # getter to get __dy for user
        return self.__dy

    def paddle_move(self, mouse):
        if mouse.x - self.paddle.width/2 < 0 or mouse.x + self.paddle.width/2 > self.window.width:
            self.paddle_dx = 0
        else:
            self.paddle_dx = mouse.x - self.paddle.x - self.paddle.width / 2
        self.paddle.move(self.paddle_dx, 0)

    def game_over(self):
        over = GLabel('GAME OVER')
        over.font = '-40'
        over.color = 'red'
        self.window.add(over, x=self.window.width/2-over.width/2, y=self.window.height/2)

    def get_object(self, new_ball_x, new_ball_y):
        self.maybe_object_1 = self.window.get_object_at(new_ball_x, new_ball_y)
        self.maybe_object_2 = self.window.get_object_at(new_ball_x + self.ball.width, new_ball_y)
        self.maybe_object_3 = self.window.get_object_at(new_ball_x, new_ball_y + self.ball.height)
        self.maybe_object_4 = self.window.get_object_at(new_ball_x + self.ball.width, new_ball_y + self.ball.height)
        if self.maybe_object_1:
            return self.maybe_object_1
        elif self.maybe_object_2:
            return self.maybe_object_2
        elif self.maybe_object_3:
            return self.maybe_object_3
        elif self.maybe_object_4:
            return self.maybe_object_4
        else:
            return None

    def remove_object(self):
        if self.maybe_object_1 and self.maybe_object_1 is not self.paddle:
            self.window.remove(self.maybe_object_1)
            self.deleted_bricks += 1
        elif self.maybe_object_2 and self.maybe_object_2 is not self.paddle:
            self.window.remove(self.maybe_object_2)
            self.deleted_bricks += 1
        elif self.maybe_object_3 and self.maybe_object_3 is not self.paddle:
            self.window.remove(self.maybe_object_3)
            self.deleted_bricks += 1
        elif self.maybe_object_4 and self.maybe_object_4 is not self.paddle:
            self.window.remove(self.maybe_object_4)
            self.deleted_bricks += 1

    def all_clear(self):
        if self.deleted_bricks == self.brick_rows * self.brick_col:
            return True
        return False







