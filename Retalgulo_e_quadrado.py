class Rectangle:
    def __init__(self, width, height):
        self.height = height
        self.width = width

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return self.height * 2 + self.width * 2

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        return f'{"*" * self.height}\n' * self.width

    def get_amount_inside(self, other_picture):
        return int(self.get_area() / other_picture.get_area())

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'


class Square(Rectangle):
    def __init__(self, side):
        self.height = side
        self.width = side

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.height = height
        self.width = height

    def set_side(self, side):
        self.height = side
        self.width = side

    def __str__(self):
        return f'Square(side={self.width})'
