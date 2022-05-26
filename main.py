import pygame
pygame.init()

from glob_param import *
import solar
# import rand_planet


## Game Screen 
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
FONT = pygame.font.SysFont("Arial", 18)
pygame.display.set_caption("Planet Simulation")
clock = pygame.time.Clock()
timecount = 0


def update_fps():
    fps = "FPS: "+ str(int(clock.get_fps()))
    fps_show = FONT.render(fps, False, WHITE)
    return fps_show

def update_year(count):
    year = "YEAR: "+ str(int(count/365))
    year_show = FONT.render(year, False, WHITE)
    return year_show        


def main():

    run = True
    planets = solar.create_solar()
    # planets = rand_planet.generate(100)

    while run:
        clock.tick(FPS)
        WIN.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Update fps
        WIN.blit(update_fps(), (10,10))

        # Update year number
        global timecount
        timecount += 1
        WIN.blit(update_year(timecount), (10,30))

        # Calculate and draw
        for planet in planets:
            planet.update_pos(planets)
            planet.draw(WIN, FONT)

        # Update screen
        pygame.display.update()
        
    pygame.quit()


if __name__ == "__main__":
    main()