from constants import BALL_RADIUS, BALL_SPEED, BAR_HEIGHT, BAR_WIDTH, HEIGHT, WIDTH

class Ball:
    def __init__(self):
        self.position = [WIDTH // 2, HEIGHT // 2]
        self.speed = BALL_SPEED

    def bounce(self):
        self.position[0] += self.speed[0]
        self.position[1] += self.speed[1]

        if self.position[0] <= BALL_RADIUS or self.position[0] >= WIDTH - BALL_RADIUS:
            self.speed[0] = -self.speed[0]
            return True
        if self.position[1] <= BALL_RADIUS:
            self.speed[1] = -self.speed[1]
            return True

        return False
    
    def collides_with(self, bar):
        if self.position[0] > bar.position \
            and self.position[0] < bar.position + BAR_WIDTH \
            and self.position[1] >= HEIGHT - BAR_HEIGHT - BALL_RADIUS:
            self.speed[1] = -self.speed[1]

            offset_from_center = self.position[0] - (bar.position + BAR_WIDTH / 2)

            self.speed[0] = (offset_from_center / (BAR_WIDTH / 2)) * 5

            return True

        return False

