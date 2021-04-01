import unittest
from src.Display.ConsoleInputs import getFileToPlay
from src.Display.IOTest import IOTest


class GetFileToPlayTest(unittest.TestCase):
    fileList = ["track_1.mp3", "track_2.mp3", "track_3.mp3"]

    def test_getValidFileToPlay(self):
        logger = IOTest()
        logger.setInputList(["1"])
        self.assertEqual("track_2.mp3", getFileToPlay(self.fileList, logger))

    def test_getValidFileToPlayWithSpaces(self):
        logger = IOTest()
        logger.setInputList(["  1  "])
        self.assertEqual("track_2.mp3", getFileToPlay(self.fileList, logger))

    def test_getValidFileToPlayFirstInList(self):
        logger = IOTest()
        logger.setInputList(["0"])
        self.assertEqual("track_1.mp3", getFileToPlay(self.fileList, logger))

    def test_getValidFileToPlayLastInList(self):
        logger = IOTest()
        logger.setInputList(["2"])
        self.assertEqual("track_3.mp3", getFileToPlay(self.fileList, logger))

    def test_getOutOfBoundsFileToPlay(self):
        logger = IOTest()
        logger.setInputList(["-1", "0"])
        getFileToPlay(self.fileList, logger)
        self.assertEqual("That is an invalid track number", logger.outputList[-1])

    def test_getInvalidTypeFileToPlay(self):
        logger = IOTest()
        logger.setInputList(["file", "0"])
        getFileToPlay(self.fileList, logger)
        self.assertEqual("That is an invalid track number", logger.outputList[-1])

    def test_getEmptyFileToPlay(self):
        logger = IOTest()
        logger.setInputList(["", "0"])
        getFileToPlay(self.fileList, logger)
        self.assertEqual("That is an invalid track number", logger.outputList[-1])

    def test_getMultipleFilesToPlay(self):
        logger = IOTest()
        logger.setInputList(["1", "0", "2"])
        getFileToPlay(self.fileList, logger)
        getFileToPlay(self.fileList, logger)
        self.assertEqual("track_3.mp3", getFileToPlay(self.fileList, logger))


if __name__ == '__main__':
    unittest.main()
