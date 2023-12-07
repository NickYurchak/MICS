from line import Line
from rectangle import Rectangle
from circle import Circle
from parameters import*

class ShapeFactory:
    @staticmethod
    def create_random_shape():
        choice = random.choice(['Line', 'Rectangle', 'Circle'])
        if choice == 'Line':
            return Line()
        elif choice == 'Rectangle':
            return Rectangle()
        elif choice == 'Circle':
            return Circle()