import pygame
from sys import exit

#Iniciar pygame
pygame.init()

#Crear la ventana del juego (ancho,alto)
screen = pygame.display.set_mode((800,400))

#Titulo de la ventana
pygame.display.set_caption("Space wars")

#Instanciar el reloj que va a limitar los frames por segundo
clock = pygame.time.Clock()

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
    #Actualiza la ventana con lo que hayamos hecho
    pygame.display.update()
    #Definir el clock en 60 frames por segundo
    clock.tick(60)
