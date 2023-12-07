from parameters import*

# Клас фігури: Прямокутник
class Rectangle(Shape):
    def create_shape(self):
        x = random.randint(0, WINDOW_WIDTH)
        y = random.randint(0, WINDOW_HEIGHT)
        width = random.randint(20, 100)
        height = random.randint(20, 100)
        color = random.choice(SHAPE_COLORS)
        print(f"Намалювано прямокутник з координатами ({x}, {y}), шириною {width}, висотою {height} кольором {color}")
        return pygame.draw.rect(window, color, (x, y, width, height))
