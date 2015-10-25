import pygame
import pprint

pygame.init()


if __name__ == '__main__':
    print("Starting Pumpkin Hero...")
    screen = pygame.display.set_mode((400, 300))

    black = (0,0,0)

    witch = pygame.image.load("witch.jpg")
    witch = pygame.transform.scale(witch, (50,100))
    witchrect = witch.get_rect()
    witchrect = (25,0,50,100)
    pprint.pprint(witchrect)

    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    done = True

        screen.fill(black)
        screen.blit(witch, witchrect)

        pygame.display.flip()
