from constants import BAR_SPEED, BAR_WIDTH, WIDTH


class Bar:
    def __init__(self):
        self.position = (WIDTH - BAR_WIDTH) // 2

    def move_left(self):
        self.position -= BAR_SPEED
        if self.position < 0:
            self.position = 0

    def move_right(self):
        self.position += BAR_SPEED
        if self.position > WIDTH - BAR_WIDTH:
            self.position = WIDTH - BAR_WIDTH
