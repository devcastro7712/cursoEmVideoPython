import pygame

pygame.init()

pygame.mixer.init()

caminho_musica = "/Users/erisonlucasdejesuscastro/Documents/cursoEmVideoPython/flowers.mp3"

pygame.mixer.music.load(caminho_musica)
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)