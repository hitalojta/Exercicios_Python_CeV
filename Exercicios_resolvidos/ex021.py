'''import pygame

pygame.mixer.init() # dá inicio ao player

pygame.mixer.music.load('ex021.mp3') #carrega o arquivo
pygame.mixer.music.play() # toca o arquivo carregado
input('Insira qualquer tecla para encerrar.')'''
''''''
#NOVA FORMA DE UTILIZAR O PACOTE
import pygame

# Inicializando o mixer PyGame
pygame.mixer.init()

# Iniciando o Pygame
pygame.init()

pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait() #Tá com problema de que se mexer o mouse, para.
