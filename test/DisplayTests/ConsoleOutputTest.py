import unittest

from src.Display.ConsoleOutputs import displayFiles, displayCommands
from src.Display.IOTest import IOTest


class ConsoleOutputTest(unittest.TestCase):
    def test_displayFiles(self):
        fileList = ["track_1.mp3", "track_2.mp3", "track_3.mp3"]
        logger = IOTest()
        displayFiles(fileList, logger)
        expectedOutput = "0:track_1.mp3"
        self.assertEqual(expectedOutput, logger.getOutputList()[0])

    def test_displayCommands(self):
        logger = IOTest()
        displayCommands(logger)
        expectedOutput = "['play', 'stop', 'volume', 'close', 'pause', 'unpause']"
        self.assertEqual(expectedOutput, logger.getOutputList()[0])


if __name__ == '__main__':
    unittest.main()
