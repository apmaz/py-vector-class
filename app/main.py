import math
class Vector:
    def __init__(self, x: int | float, y: int | float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector((self.x + other.x), (self.y + other.y))

    def __sub__(self, other):
        return Vector((self.x - other.x), (self.y - other.y))

    def __mul__(self, other):
        if not isinstance(other, Vector):
            return Vector((self.x * other), (self.y * other))
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple):
        return Vector(end_point[0] - start_point[0], end_point[1] - start_point[1])

    def get_length(self):
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2))

    def get_normalized(self):
        return Vector(self.x / self.get_length(),  self.y / self.get_length())

    def angle_between(self, other):
        return round(math.degrees(math.acos(self * other / (self.get_length() * other.get_length()))))

    def get_angle(self):
        if self.x > 0 and self.y > 0:
            return round((math.degrees(math.atan(self.x / self.y))))
        elif self.x < 0 and self.y > 0:
            return round((math.degrees(math.pi + math.atan(self.x / self.y))))
        elif self.x < 0 and self.y < 0:
            return round((math.degrees(2 * math.pi + math.atan(self.x / self.y))))

    def rotate(self, rotate: int):
        x = (math.cos(math.radians(rotate)) * self.x) - (math.sin(math.radians(rotate)) * self.y)
        y = (math.sin(math.radians(rotate)) * self.x) + (math.cos(math.radians(rotate)) * self.y)
        return Vector(x, y)

