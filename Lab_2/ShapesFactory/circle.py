from parameters import*

# Клас фігури: Коло
class Circle(Shape):
    def create_shape(self):
        x = random.randint(0, WINDOW_WIDTH)
        y = random.randint(0, WINDOW_HEIGHT)
        radius = random.randint(10, 50)
        color = random.choice(SHAPE_COLORS)
        print(f"Намалювано коло з центром у точці ({x}, {y}), радіусом {radius} кольором {color}")
        return pygame.draw.circle(window, color, (x, y), radius)
