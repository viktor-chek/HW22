class Field:
    @staticmethod
    def set_unit(y: float, x: float, unit: object):
        print(f"{y}, {x}, {unit}")


class Unit:
    def __init__(self, state, field_):
        self.x = None
        self.y = None
        self.state = state
        self.speed = 1
        self.field = field_

    def move(self, direction: str, y: float, x: float):
        self.y = y
        self.x = x

        speed = self._get_speed()

        if direction == 'UP':
            self.field.set_unit(y=self.y + speed, x=self.x, unit=self)
        elif direction == 'DOWN':
            self.field.set_unit(y=self.y - speed, x=self.x, unit=self)
        elif direction == 'LEFT':
            self.field.set_unit(y=self.y, x=self.x - speed, unit=self)
        elif direction == 'RIGHT':
            self.field.set_unit(y=self.y, x=self.x + speed, unit=self)

    def _get_speed(self):
        if self.state == 'fly':
            return self.speed * 1.2
        elif self.state == 'crawl':
            return self.speed * 0.5
        else:
            raise ValueError('"fly" or "crawl"')


field = Field()
unit_one = Unit("fly", field)
unit_one.move("DOWN", 2, 4)
