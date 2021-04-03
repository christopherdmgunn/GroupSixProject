import pygame


def setVolume(volume, soundPlayer):
    if soundPlayer != "":
        pygame.mixer.Sound.set_volume(soundPlayer, volume)