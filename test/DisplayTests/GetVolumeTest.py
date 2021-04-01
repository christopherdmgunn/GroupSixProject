import unittest

from src.Display.IOTest import IOTest
from src.Display.ConsoleInputs import getVolume
from unittest.mock import MagicMock


class GetVolumeTest(unittest.TestCase):
    def test_getValidVolume(self):
        logger = IOTest()
        logger.setInputList(["5"])
        self.assertEqual(0.5, getVolume(logger))

    def test_getValidVolumeWithSpaces(self):
        logger = IOTest()
        logger.setInputList(["     5     "])
        self.assertEqual(0.5, getVolume(logger))

    def test_getMinVolume(self):
        logger = IOTest()
        logger.setInputList(["0"])
        self.assertEqual(0, getVolume(logger))

    def test_getMaxVolume(self):
        logger = IOTest()
        logger.setInputList(["10"])
        self.assertEqual(1, getVolume(logger))

    def test_getOutOfBoundsVolume(self):
        logger = IOTest()
        logger.setInputList(["-1", "5"])
        self.assertEqual(0.5, getVolume(logger))

    def test_getInvalidVolume(self):
        logger = IOTest()
        logger.setInputList(["", "5"])
        self.assertEqual(0.5, getVolume(logger))

    def test_getMultipleVolumesMock(self):
        logger = IOTest()
        logger.takeInput = MagicMock(side_effect=["5", "10", "0"])
        self.assertEqual(0.5, getVolume(logger))
        self.assertEqual(1, getVolume(logger))
        self.assertEqual(0, getVolume(logger))

    def test_getMultipleVolumesMockThirdOutput(self):
        logger = IOTest()
        logger.takeInput = MagicMock(side_effect=["5", "10", "0"])
        getVolume(logger)
        getVolume(logger)
        self.assertEqual(0, getVolume(logger))



if __name__ == '__main__':
    unittest.main()
