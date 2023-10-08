import pygame

# pygame setup
pygame.init()
info = pygame.display.Info()
info = pygame.display.Info()
w = info.current_w
h = (info.current_h)-60 
screen = pygame.display.set_mode((w,h), pygame.RESIZABLE|pygame.SCALED)
clock = pygame.time.Clock()
running = True
dt = 0

# pygame title
pygame.display.set_caption("ShareSquare - Friendly way to split bills")

while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
        screen.fill("#e78492")
        pygame.draw.rect(screen, "#f01616", pygame.Rect(w-70,h-(h-15),60, 30), border_radius=20)
       
        

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    dt = clock.tick(60) / 1000

pygame.quit()