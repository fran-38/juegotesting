import random

class Food:
    def __init__(self, snake_body):
        self.position = self.random_position(snake_body)

    def random_position(self, forbidden):
        while True:
            x = random.randint(0, 29) * 20
            y = random.randint(0, 29) * 20
            if (x, y) not in forbidden:
                return (x, y)

    def relocate(self, forbidden):
        self.position = self.random_position(forbidden)

    def get_position(self):
        return self.position

    def set_position(self, new_pos):
        self.position = new_pos

    def is_eaten_by(self, snake_head):
        return self.position == snake_head

    def avoid_obstacles(self, forbidden):
        return self.random_position(forbidden)

    def spawn_near_center(self, forbidden):
        center_area = [(x, y) for x in range(240, 360, 20) for y in range(240, 360, 20)]
        random.shuffle(center_area)
        for pos in center_area:
            if pos not in forbidden:
                self.position = pos
                return

    def spawn_in_corner(self, forbidden):
        corners = [(0, 0), (580, 0), (0, 580), (580, 580)]
        random.shuffle(corners)
        for pos in corners:
            if pos not in forbidden:
                self.position = pos
                return
