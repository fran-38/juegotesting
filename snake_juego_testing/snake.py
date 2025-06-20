class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)]
        self.direction = "RIGHT"

    def move(self):
        x, y = self.body[0]
        if self.direction == "UP":
            y -= 20
        elif self.direction == "DOWN":
            y += 20
        elif self.direction == "LEFT":
            x -= 20
        elif self.direction == "RIGHT":
            x += 20
        self.body = [(x, y)] + self.body[:-1]

    def change_direction(self, new_direction):
        opposite = {
            "UP": "DOWN", "DOWN": "UP",
            "LEFT": "RIGHT", "RIGHT": "LEFT"
        }
        if new_direction != opposite.get(self.direction):
            self.direction = new_direction

    def grow(self):
        self.body.append(self.body[-1])

    def head(self):
        return self.body[0]

    def check_collision(self):
        head = self.head()
        if head in self.body[1:]:
            return True
        x, y = head
        if x < 0 or x >= 600 or y < 0 or y >= 600:
            return True
        return False

    def reset(self):
        self.body = [(100, 100), (80, 100), (60, 100)]
        self.direction = "RIGHT"

    def length(self):
        return len(self.body)

    def segments(self):
        return self.body.copy()

    def get_direction(self):
        return self.direction

    def is_opposite(self, new_direction):
        opposites = {
            "UP": "DOWN", "DOWN": "UP",
            "LEFT": "RIGHT", "RIGHT": "LEFT"
        }
        return opposites[self.direction] == new_direction

    def can_change(self, new_direction):
        return not self.is_opposite(new_direction)

    def next_position(self):
        x, y = self.body[0]
        if self.direction == "UP":
            return (x, y - 20)
        elif self.direction == "DOWN":
            return (x, y + 20)
        elif self.direction == "LEFT":
            return (x - 20, y)
        elif self.direction == "RIGHT":
            return (x + 20, y)
        return (x, y)

    def overlaps(self, position):
        return position in self.body

    def contains(self, position):
        return self.overlaps(position)
