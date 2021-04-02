import unittest

from src.Display.IOTest import IOTest
from src.Engine.Main import main
from unittest.mock import MagicMock
import pygame


class MainTest(unittest.TestCase):
    directoryPath = "../../src/Data/stubMusic/"

    def test_validCloseCommandMock(self):
        pygame.mixer.init()
        logger = IOTest()
        logger.takeInput = MagicMock(return_value="close")
        main(self.directoryPath, logger)
        self.assertEqual("Closing program", logger.outputList[-1])

        pygame.mixer.quit()

    def test_validPlayCommandWithNoSoundPlayingMock(self):
        pygame.mixer.init()
        logger = IOTest()
        expectedOutput = "Now playing: stub_bensound-dubstep.wav"
        logger.takeInput = MagicMock(side_effect=["play", "0", "close"])
        main(self.directoryPath, logger)
        self.assertEqual(expectedOutput, logger.outputList[-3])

        pygame.mixer.quit()

    def test_validPlayCommandWithSoundPlayingMock(self):
        pygame.mixer.init()
        logger = IOTest()
        expectedOutput = "Now playing: stub_bensound-dubstep.wav"
        logger.takeInput = MagicMock(side_effect=["play", "0", "play", "0", "close"])
        main(self.directoryPath, logger)
        self.assertEqual(expectedOutput, logger.outputList[-3])

        pygame.mixer.quit()

    def test_validPlayCommandWithInvalidSongMock(self):
        pygame.mixer.init()
        logger = IOTest()
        logger.takeInput = MagicMock(side_effect=["play", "5", "0", "close"])
        main(self.directoryPath, logger)
        self.assertEqual("That is an invalid track number", logger.outputList[-4])

    def test_validStopCommandWithNoSoundPlayingMock(self):
        pygame.mixer.init()
        logger = IOTest()
        logger.takeInput = MagicMock(side_effect=["stop", "close"])
        main(self.directoryPath, logger)
        self.assertEqual("No song playing", logger.outputList[-3])

        pygame.mixer.quit()

    def test_validStopCommandWithSoundPlayingMock(self):
        pygame.mixer.init()
        logger = IOTest()
        logger.takeInput = MagicMock(side_effect=["play", "0", "stop", "close"])
        main(self.directoryPath, logger)
        self.assertEqual("Song stopped", logger.outputList[-3])

        pygame.mixer.quit()

    def test_validVolumeCommandWithNoSoundPlayingMock(self):
        pygame.mixer.init()
        logger = IOTest()
        logger.takeInput = MagicMock(side_effect=["volume", "5", "close"])
        main(self.directoryPath, logger)
        self.assertEqual("Volume changed to 5.0", logger.outputList[-3])

        pygame.mixer.quit()

    def test_validMuteCommandMock(self):
        pygame.mixer.init()
        logger = IOTest()
        logger.takeInput = MagicMock(side_effect=["volume", "0", "close"])
        main(self.directoryPath, logger)
        self.assertEqual("Volume changed to 0.0", logger.outputList[-3])

        pygame.mixer.quit()

    def test_validMaxVolumeCommandMock(self):
        pygame.mixer.init()
        logger = IOTest()
        logger.takeInput = MagicMock(side_effect=["volume", "1", "close"])
        main(self.directoryPath, logger)
        self.assertEqual("Volume changed to 1.0", logger.outputList[-3])

        pygame.mixer.quit()

    def test_validVolumeCommandWithSoundPlayingMock(self):
        pygame.mixer.init()
        logger = IOTest()
        logger.takeInput = MagicMock(side_effect=["play", "0", "volume", "1", "close"])
        main(self.directoryPath, logger)
        self.assertEqual("Volume changed to 1.0", logger.outputList[-3])

        pygame.mixer.quit()

    def test_validVolumeCommandWithInvalidValueMock(self):
        pygame.mixer.init()
        logger = IOTest()
        logger.takeInput = MagicMock(side_effect=["play", "0", "volume", "-5", "5", "close"])
        main(self.directoryPath, logger)
        self.assertEqual("That is an invalid volume", logger.outputList[-4])

        pygame.mixer.quit()

    def test_validPauseUnpauseCommandWithNoSoundPlayingMock(self):
        pygame.mixer.init()
        logger = IOTest()
        logger.takeInput = MagicMock(side_effect=["pause", "close"])
        main(self.directoryPath, logger)
        self.assertEqual("No song playing", logger.outputList[-3])

        pygame.mixer.quit()

    def test_validPauseUnpauseCommandWithSoundPlayingMock(self):
        pygame.mixer.init()
        logger = IOTest()
        logger.takeInput = MagicMock(side_effect=["play", "0", "pause", "close"])
        main(self.directoryPath, logger)
        self.assertEqual("Pausing song", logger.outputList[-3])

        pygame.mixer.quit()

    def test_invalidUnPauseCommandWithSoundPlayingMock(self):
        pygame.mixer.init()
        logger = IOTest()
        logger.takeInput = MagicMock(side_effect=["play", "0", "unpause", "close"])
        main(self.directoryPath, logger)
        self.assertEqual("Song is not paused", logger.outputList[-3])

        pygame.mixer.quit()

    def test_validCloseCommandWithSongPlayingMock(self):
        pygame.mixer.init()
        logger = IOTest()
        logger.takeInput = MagicMock(side_effect=["play", "0", "close"])
        main(self.directoryPath, logger)
        self.assertEqual("Closing program", logger.outputList[-1])

        pygame.mixer.quit()

    def test_validCommandWithSpacesMock(self):
        pygame.mixer.init()
        logger = IOTest()
        logger.takeInput = MagicMock(return_value="   close    ")
        main(self.directoryPath, logger)
        self.assertEqual("Closing program", logger.outputList[-1])

        pygame.mixer.quit()

    def test_invalidCommandMock(self):
        pygame.mixer.init()
        logger = IOTest()
        logger.takeInput = MagicMock(side_effect=["invalid command", "close"])
        main(self.directoryPath, logger)
        self.assertEqual("That is not a valid user command", logger.outputList[-3])

        pygame.mixer.quit()

    def test_multipleCommandsMock(self):
        pygame.mixer.init()
        logger = IOTest()
        logger.takeInput = MagicMock(side_effect=["volume", "2", "play", "4", "0", "stop", "close"])
        main(self.directoryPath, logger)
        self.assertEqual("Closing program", logger.outputList[-1])

        pygame.mixer.quit()


if __name__ == '__main__':
    unittest.main()
