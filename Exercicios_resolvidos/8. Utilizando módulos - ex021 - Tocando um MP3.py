"""
Faça um programa em python que abra e reproduza o áudio de um
arquivo mp3.
"""

'''import pygame

pygame.mixer.init() # dá inicio ao player

pygame.mixer.music.load('8. Utilizando módulos - 8. Utilizando módulos - ex021.mp3') #carrega o arquivo
pygame.mixer.music.play() # toca o arquivo carregado
input('Insira qualquer tecla para encerrar.')'''
''''''
# NOVA FORMA DE UTILIZAR O PACOTE
import pygame

# Inicializando o mixer PyGame
pygame.mixer.init()

# Iniciando o Pygame
pygame.init()

pygame.mixer.music.load('8. Utilizando módulos - 8. Utilizando módulos - ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()  # Tá com problema de que se mexer o mouse, para.
