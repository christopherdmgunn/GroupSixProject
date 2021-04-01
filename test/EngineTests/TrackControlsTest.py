import unittest

import pygame

from src.Display.IOLogger import IOLogger
from src.Display.IOTest import IOTest
from src.Engine.TrackControls import playSound, stopSound


class TrackControlsTest(unittest.TestCase):
    filePath = "../../src/Data/stubMusic/stub_bensound-dubstep.wav"

    def test_playSoundWithNoSongPlaying(self):
        pygame.mixer.init()
        logger = IOTest()
        soundPlayer = playSound(self.filePath, 1, logger)
        self.assertTrue(pygame.mixer.get_busy())

        pygame.mixer.quit()

    def test_playSoundWithSongPlaying(self):
        pygame.mixer.init()
        logger = IOTest()
        soundPlayer = playSound(self.filePath, 1, logger)
        newsoundPlayer = playSound(self.filePath, 1, logger)
        self.assertTrue(pygame.mixer.get_busy())

        pygame.mixer.quit()

    def test_stopSoundWithSongPlaying(self):
        pygame.mixer.init()
        logger = IOTest()
        soundPlayer = playSound(self.filePath, 1, logger)
        stopSound(soundPlayer, logger)
        self.assertFalse(pygame.mixer.get_busy())

        pygame.mixer.quit()

    def test_stopSoundWithNoSongPlaying(self):
        pygame.mixer.init()
        logger = IOTest()
        soundPlayer = playSound(self.filePath, 1, logger)
        soundPlayer.stop()
        stopSound(soundPlayer, logger)
        self.assertFalse(pygame.mixer.get_busy())

        pygame.mixer.quit()



if __name__ == '__main__':
    unittest.main()
