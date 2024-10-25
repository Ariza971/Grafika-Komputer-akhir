import pygame
import cairo

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Testing")

def main():
    running = True
    clock = pygame.time.Clock()
 
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
     
        screen.fill((1, 1, 0))
     
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
