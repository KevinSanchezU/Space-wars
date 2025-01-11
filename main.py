import pygame #pygame
from sys import exit #Nos permite exit() y salir de la ventana

#Iniciar pygame
pygame.init()

#Crear la ventana del juego (ancho,alto)
screen = pygame.display.set_mode((1280,500))

#Titulo de la ventana
pygame.display.set_caption("Space wars")

#Instanciar el reloj que va a limitar los frames por segundo
clock = pygame.time.Clock()
#Crear la fuente para el texto
font_game_start = pygame.font.Font(None,100)
#Instanciar superficie que vamos a mostrar
background_surface = pygame.image.load("recursos/fondo/frame_0_delay-0.03s.jpg").convert()
#Instanciar superficie con texto
text_start_game = font_game_start.render("GAME START", True, 'White')
text_start_x_coord = 400
text_start_y_coord = 100

#Bucle infinito donde corre el juego
while True:
    #Obtencion constante de eventos
    for event in pygame.event.get():
        #Comparacion con evento SALIR
        if event.type == pygame.QUIT:
            #Termina Pygamme
            pygame.quit()
            #Salimos de la ventana y cierra el programa
            exit()
    #Cargar superficie
    screen.blit(background_surface,(0,0))
    screen.blit(background_surface,(420,0))
    screen.blit(background_surface,(840,0))
    if text_start_x_coord > -600:
        screen.blit(text_start_game,(text_start_x_coord,text_start_y_coord))
        text_start_x_coord -= 4

    #Actualiza la ventana con lo que hayamos hecho
    pygame.display.update()
    #Definir el clock en 60 frames por segundo
    clock.tick(60)
