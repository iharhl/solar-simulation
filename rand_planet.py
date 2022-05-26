import random
from glob_param import *
from planet import Planet


def generate(num):

    radius = []
    r_min = 4
    r_max = 15

    mass = []
    m_min = 10
    m_max = 15

    x_pos = []
    y_pos = []
    pos_min = -800
    pos_max = 800

    x_vel = []
    y_vel = []
    vel_min = -0
    vel_max = 0

    color = []
    color_min = 5
    color_max = 250   

    for i in range(num):
        radius.append(random.randint(r_min, r_max))
        mass.append(random.randint(m_min, m_max))
        x_pos.append(random.randint(pos_min, pos_max))
        y_pos.append(random.randint(pos_min, pos_max))
        x_vel.append(random.randint(vel_min, vel_max))
        y_vel.append(random.randint(vel_min, vel_max))
        color.append((random.randint(color_min, color_max), random.randint(color_min, color_max), random.randint(color_min, color_max)))

    planets = []
    for i in range(num):
        planets.append(Planet(x_pos[i], y_pos[i], radius[i], mass[i], x_vel[i], y_vel[i], color[i]))

    planets.append(Planet(0,0,10,10000,1,1,YELLOW))

    return planets
