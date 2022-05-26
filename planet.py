import pygame
import math
from glob_param import *


class Planet:

    def __init__(self, x, y, radius, mass, x_vel, y_vel, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.mass = mass
        self.color = color

        self.orbit = (0,0)
        self.sun = False
        self.distance_to_sun = 0

        self.x_vel = x_vel
        self.y_vel = y_vel

        self.updated_points = []
        self.name = " "

    def draw(self, win, font):
        x = self.x * SCALE + WIDTH/2
        y = self.y * SCALE + HEIGHT/2

        x, y = self.orbit
        x = x * SCALE + WIDTH/2
        y = y * SCALE + HEIGHT/2

        if len(self.updated_points) > ORBIT_LENGTH:
            self.updated_points.pop(0)

        self.updated_points.append((x,y))

        if len(self.updated_points) > 2:
            pygame.draw.lines(win, self.color, False, self.updated_points, 2)

        pygame.draw.circle(win, self.color, (x, y), self.radius)

        name = font.render(self.name, False, WHITE)
        # win.blit(name, (x - name.get_width()/2 ,y - name.get_height()/2))
        win.blit(name, (x,y))

    def attraction(self, other):
        other_x, other_y = other.x, other.y
        dist_x = other_x - self.x
        dist_y = other_y - self.y
        dist = math.sqrt(dist_x**2 + dist_y**2)

        if other.sun:
            self.distance_to_sun = dist

        force = G * self.mass * other.mass / dist**2
        theta = math.atan2(dist_y, dist_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force

        return force_x, force_y

    def update_pos(self, planets):

        total_force_x = total_force_y = 0

        for planet in planets:
            if self == planet:
                continue
            fx, fy = self.attraction(planet)
            total_force_x += fx
            total_force_y += fy
        
        self.x_vel += total_force_x / self.mass * TIMESTEP
        self.y_vel += total_force_y / self.mass * TIMESTEP

        self.x += self.x_vel * TIMESTEP
        self.y += self.y_vel * TIMESTEP

        self.orbit = (self.x, self.y) 



         