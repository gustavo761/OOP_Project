import pygame
import Colors


class Invader:
    """
    Descripcion de los Invader's del juego
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
    

    def get_x(self):
        return self.x
    

    def set_x(self, new_x):
        self.x = new_x


    def get_y(self):
        return self.y


    def set_y(self, new_y):
        self.y = new_y


    def draw(self, pygame_window):
        pygame.draw.rect(pygame_window, Colors.white, (self.x, self.y, self.width, self.height))


    def move_in_y(self, pygame_window, mov_y):
        self.y += mov_y

    
    def move_in_x(self, pygame_window, mov_x):
        self.x += mov_x
