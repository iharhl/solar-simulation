from planet import Planet
from glob_param import *


def create_solar():

    sun = Planet(0, 0, 30, 1.98892*10**30, 0, 0, YELLOW) # mass in [kg]
    sun.sun = True
    sun.name = "Sun"

    earth = Planet(-1*AU, 0, 16, 5.9742*10**24, 0, 29.783 * 1000, BLUE)    
    earth.name = "Earth"

    mars = Planet(-1.524*AU, 0, 12, 6.39*10**23, 0, 24.077 * 1000, RED)
    mars.name = "Mars" 

    mercury = Planet(0.387*AU, 0, 8, 3.3*10**23, 0, -47.4 * 1000, DARK_GREY)
    mercury.name = "Mercury"

    venus = Planet(0.723*AU, 0, 14, 4.8685*10**24, 0, -35.02 * 1000, WHITE)
    venus.name = "Venus"
    
    planets = [sun, mercury, venus, earth, mars]

    return planets