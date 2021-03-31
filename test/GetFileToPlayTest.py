import unittest
from src.Display.ConsoleInputs import getFileToPlay
from src.Display.IOTest import IOTest


class GetFileToPlayTest(unittest.TestCase):
    def test_getValidFileToPlay(self):
        fileList = ["track_1.mp3", "track_2.mp3", "track_3.mp3"]
        logger = IOTest()
        logger.setInputList([1])
        self.assertEqual("track_2.mp3", getFileToPlay(fileList, logger))

    def test_getValidFileToPlayFirstInList(self):
        fileList = ["track_1.mp3", "track_2.mp3", "track_3.mp3"]
        logger = IOTest()
        logger.setInputList([0])
        self.assertEqual("track_1.mp3", getFileToPlay(fileList, logger))

    def test_getValidFileToPlayLastInList(self):
        fileList = ["track_1.mp3", "track_2.mp3", "track_3.mp3"]
        logger = IOTest()
        logger.setInputList([2])
        self.assertEqual("track_3.mp3", getFileToPlay(fileList, logger))

    def test_getOutOfBoundsFileToPlay(self):
        fileList = ["track_1.mp3", "track_2.mp3", "track_3.mp3"]
        logger = IOTest()
        logger.setInputList([-1, 0])
        self.assertEqual("track_1.mp3", getFileToPlay(fileList, logger))

    def test_getInvalidTypeFileToPlay(self):
        fileList = ["track_1.mp3", "track_2.mp3", "track_3.mp3"]
        logger = IOTest()
        logger.setInputList(["file", 0])
        self.assertEqual("track_1.mp3", getFileToPlay(fileList, logger))

    def test_getNullFileToPlay(self):
        fileList = ["track_1.mp3", "track_2.mp3", "track_3.mp3"]
        logger = IOTest()
        logger.setInputList([None, 0])
        self.assertEqual("track_1.mp3", getFileToPlay(fileList, logger))

    def test_getMultipleFilesToPlay(self):
        fileList = ["track_1.mp3", "track_2.mp3", "track_3.mp3"]
        logger = IOTest()
        logger.setInputList([1, 0, 2])
        getFileToPlay(fileList, logger)
        getFileToPlay(fileList, logger)
        self.assertEqual("track_3.mp3", getFileToPlay(fileList, logger))


if __name__ == '__main__':
    unittest.main()
