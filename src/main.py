import pygame
import Colors
from Invader import Invader
from Ship import Ship
import easygui as eg


# Proyecto // Hacer un space invader

pygame.init()
main_window = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Project")
running_game = True

inv = []  #  Lista de Invaders
pos_x = 100
pos_y = 30


#  Instanciacion de Invaders con sus respectivas coordenadas en x e y
for i in range(5):
    pos_x = 100
    for j in range(10):
        invad = Invader(pos_x, pos_y)
        inv.append(invad)
        pos_x += 50
    pos_y += 50


#  Instanciación de la nave
ship = Ship(400, 550)


#  control_x y control_y definen la velocidad de movimiento de los invaders
control_x = 1
control_y = 0

while running_game:
    pygame.time.delay(10)
    main_window.fill(Colors.black) #  Refresca la pantalla
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_game = False
            break
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and (ship.get_x() > 100):
        ship.move_left(main_window)

    if keys[pygame.K_RIGHT] and (ship.get_x() < 700):    
        ship.move_right(main_window)

    if keys[pygame.K_UP] and (ship.get_y() > 500):
        ship.move_up(main_window)

    if keys[pygame.K_DOWN] and (ship.get_y() < 570):
        ship.move_down(main_window)
    
    for i in range(50):
        inv[i].draw(main_window)
        inv[i].move_in_x(main_window, control_x)
        inv[i].move_in_y(main_window, control_y)

    if inv[0].get_x() < 100:
        control_x *= -1
        control_y = 40
    elif inv[49].get_x() > 700:
        control_x *= -1
        control_y = 40
    else:
        control_y = 0

    if inv[49].get_y() > 500:
        eg.msgbox(msg="Game Over", title="Game Over", ok_button="Aceptar")
        running_game = False

    ship.draw(main_window)
    pygame.display.update()
    
pygame.quit()