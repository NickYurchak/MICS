from parameters import*

# Клас фігури: Лінія
class Line(Shape):
    def create_shape(self):
        x1 = random.randint(0, WINDOW_WIDTH)
        y1 = random.randint(0, WINDOW_HEIGHT)
        x2 = random.randint(0, WINDOW_WIDTH)
        y2 = random.randint(0, WINDOW_HEIGHT)
        color = random.choice(SHAPE_COLORS)
        print(f"Намалювано лінію від ({x1}, {y1}) до ({x2}, {y2}) кольором {color}")
        return pygame.draw.line(window, color, (x1, y1), (x2, y2), 3)
