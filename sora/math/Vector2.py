import math

class Vector2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def add(self, vector2):
        self.x += vector2.x
        self.y += vector2.y

    def subtract(self, vector2):
        self.x -= vector2.x
        self.y -= vector2.y

    def multiply(self, scalar : float):
        self.x *= scalar
        self.y *= scalar

    def divide(self, scalar : float):
        self.x /= scalar
        self.y /= scalar

    def setValues(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def lengthSquared(self):
        return self.x * self.x + self.y * self.y

    def normalize(self):
        length = self.length()
        if length > 0:
            self.x = self.x / length
            self.y = self.y / length
    
    def isNormalized(self):
        if self.x >= -1 and self.x <= 1 and self.y >= -1 and self.y <= 1:
            return True
        return False

    def dot(self, vector2):
        return self.x * vector2.x + self.y * vector2.y

    def cross(self, vector2):
        return self.x * vector2.y - self.y * vector2.x

    def lerp(self, vector, value : float):
        x = self.x * (1 - value) + vector2.x * value
        y = self.y * (1 - value) + vector2.y * value
        return Vector2(x, y)

    def rotate(self, degress):
        sin = math.sin(degress * math.pi / 180)
        cos = math.cos(degress * math.pi / 180)
        x = (cos * self.x) - (sin * self.y)
        y = (sin * self.x) + (cos * self.y)
        return Vector2(x, y)

    def rotateRad(self, radians):
        x = self.x * math.cos(radians) - self.y * math.sin(radians)
        y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector2(x, y)

    def copy(self):
        return Vector2(self.x, self.y)

    def zero(self):
        self.x = 0
        self.y = 0