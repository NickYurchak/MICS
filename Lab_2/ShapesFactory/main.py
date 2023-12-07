from shape_factory import*

# Основний код
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

shapes = []

shape_n = random.randint(1, 10)
print("Було створено ", shape_n, " фігур:")
for _ in range(shape_n):
    shape = ShapeFactory.create_random_shape()
    shapes.append(shape)
    shape.create_shape()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()