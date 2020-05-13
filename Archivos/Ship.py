import pygame
import Colors

class Ship:
    """
    Descripción del comportamiento de la nave manipulada por el usuario
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
        pygame.draw.rect(pygame_window, Colors.blue, (self.x, self.y, self.width, self.height))
    
    def move_up(self, pygame_window):
        self.y -= 8
        #self.draw(pygame_window)

    def move_down(self, pygame_window):
        self.y += 8
        #self.draw(pygame_window)
    
    def move_right(self, pygame_window):
        self.x += 8
        #self.draw(pygame_window)
    
    def move_left(self, pygame_window):
        self.x -= 8
        #self.draw(pygame_window)
    
    def shot(self, pygame_window):
        pass