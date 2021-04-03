import pygame

from src.Engine.VolumeControls import setVolume
musicPlaying = True


def playSound(filePath, volume, logger):
    pygame.mixer.stop()
    soundPlayer = pygame.mixer.Sound(filePath)
    setVolume(volume, soundPlayer)
    soundPlayer.play()

    filePathComponents = filePath.split("/")
    logger.showOutput("Now playing: " + filePathComponents[-1])

    return soundPlayer


def stopSound(soundPlayer, logger):
    if pygame.mixer.get_busy():
        soundPlayer.stop()
        logger.showOutput("Song stopped")
    else:
        logger.showOutput("No song playing")


def playPause(logger):
    global musicPlaying

    if pygame.mixer.get_busy():

        if musicPlaying:
            musicPlaying = False
            pygame.mixer.pause()
            logger.showOutput("Pausing song")
        else:
            musicPlaying = True
            pygame.mixer.unpause()
            logger.showOutput("Resuming song")

    else:
        logger.showOutput("No song playing")

def unPause(logger):
    global musicPlaying

    if pygame.mixer.get_busy():

        if musicPlaying:
            logger.showOutput("Song is not paused")
        else:
            musicPlaying = True
            pygame.mixer.unpause()
            logger.showOutput("Resuming song")

    else:
        logger.showOutput("No song Playing")

