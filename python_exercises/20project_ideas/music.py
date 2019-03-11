import pygame
from pygame import mixer
mixer.init()
mixer.music.load("mp3/i.mp3")
mixer.music.play()
mixer.music.queue("mp3/A.mp3")
while pygame.mixer.music.get_busy() == True:
    continue

