class ShapeFactory(object):

    def getShape(self):
        return self.shape_name

class Circle(ShapeFactory):
    def __init__(self):
        self.shape_name = "Circle"

    def draw(self):
        print('draw circle')

class Rectangle(ShapeFactory):
    def __init__(self):
        self.shape_name = "Rectangle"

    def draw(self):
        print('draw rectangle')

class ShapeInterfaceFactory(object):
    def create(self):
        return NotImplementedError

class ShapeCircle(ShapeInterfaceFactory):
    def create(self):
        return Circle()

class ShapeRectangle(ShapeInterfaceFactory):
    def create(self):
        return Rectangle()

class Shape(ShapeInterfaceFactory):
    def __new__(cls, name):
        if name == 'Circle':
            return Circle()
        if name == 'Rectangle':
            return Rectangle()


shape_interface = ShapeCircle()
obj = shape_interface.create()
obj.getShape()
obj.draw()
shape2 = Shape("Circle")
shape2.getShape()
shape2.draw()

