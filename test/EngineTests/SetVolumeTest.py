import unittest

import pygame

from src.Display.IOTest import IOTest
from src.Engine.VolumeControls import setVolume
from src.Engine.TrackControls import playSound
from src.Display.ConsoleInputs import getVolume
from unittest.mock import MagicMock


class SetVolumeTest(unittest.TestCase):
    filePath = "../../src/Data/stubMusic/stub_bensound-dubstep.wav"
    initialVolume = 1

    def test_setVolumeToValidValueNoPlayback(self):
        pygame.mixer.init()
        newVolume = 0.5
        logger = IOTest()
        soundPlayer = playSound(self.filePath, self.initialVolume, logger)
        pygame.mixer.stop()
        setVolume(newVolume, soundPlayer)
        self.assertEqual(0.5, pygame.mixer.Sound.get_volume(soundPlayer))

        pygame.mixer.quit()

    def test_setVolumeToValidValueDuringPlayback(self):
        pygame.mixer.init()
        newVolume = 0.5
        logger = IOTest()
        soundPlayer = playSound(self.filePath, self.initialVolume, logger)
        setVolume(newVolume, soundPlayer)
        self.assertEqual(0.5, pygame.mixer.Sound.get_volume(soundPlayer))

        pygame.mixer.quit()

    def test_setVolumeToValidValueNoSoundPlayer(self):
        pygame.mixer.init()
        newVolume = 0.5
        soundPlayer = ""
        setVolume(newVolume, soundPlayer)
        self.assertRaises(TypeError, pygame.mixer.Sound.get_volume, soundPlayer)

        pygame.mixer.quit()

    def test_setVolumeToMute(self):
        pygame.mixer.init()
        newVolume = 0
        logger = IOTest()
        soundPlayer = playSound(self.filePath, self.initialVolume, logger)
        setVolume(newVolume, soundPlayer)
        self.assertEqual(0, pygame.mixer.Sound.get_volume(soundPlayer))

        pygame.mixer.quit()

    def test_setVolumeToMax(self):
        pygame.mixer.init()
        initialVolume = 0.5
        newVolume = 1
        logger = IOTest()
        soundPlayer = playSound(self.filePath, initialVolume, logger)
        setVolume(newVolume, soundPlayer)
        self.assertEqual(1, pygame.mixer.Sound.get_volume(soundPlayer))

        pygame.mixer.quit()

    def test_setOutOfBoundsVolume(self):
        pygame.mixer.init()
        newVolume = -0.5
        logger = IOTest()
        soundPlayer = playSound(self.filePath, self.initialVolume, logger)
        setVolume(newVolume, soundPlayer)
        self.assertNotEqual(-0.5, pygame.mixer.Sound.get_volume(soundPlayer))

        pygame.mixer.quit()

    def test_setInvalidVolume(self):
        pygame.mixer.init()
        newVolume = ""
        logger = IOTest()
        soundPlayer = playSound(self.filePath, self.initialVolume, logger)
        self.assertRaises(TypeError, setVolume, newVolume, soundPlayer)

        pygame.mixer.quit()

    def test_setNullVolume(self):
        pygame.mixer.init()
        initialVolume = 0.5
        newVolume = None
        logger = IOTest()
        soundPlayer = playSound(self.filePath, initialVolume, logger)
        self.assertRaises(TypeError, setVolume, newVolume, soundPlayer)

        pygame.mixer.quit()

    def test_setMultipleVolumesWithMock(self):
        pygame.mixer.init()
        filePath = "../../src/Data/stubMusic/stub_bensound-dubstep.wav"
        initialVolume = 1
        logger = IOTest()
        soundPlayer = playSound(filePath, initialVolume, logger)
        getVolume = MagicMock(side_effect=[0.5, 1, 0])
        setVolume(getVolume(), soundPlayer)
        setVolume(getVolume(), soundPlayer)
        setVolume(getVolume(), soundPlayer)
        self.assertEqual(0, pygame.mixer.Sound.get_volume(soundPlayer))

        pygame.mixer.quit()



if __name__ == '__main__':
    unittest.main()
