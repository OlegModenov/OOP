class Triangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_triangle_str(self):
        return f"Triangle({self.x}, {self.y}, {self.width}, {self.height})"


triangle = Triangle(0, 0, 10, 20)
print(triangle.get_triangle_str())


