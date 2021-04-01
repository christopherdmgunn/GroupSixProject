import unittest

from src.Data.InputDataFile import InputDataFile
from src.Data.InputDataStub import InputDataStub
from src.Display.IOTest import IOTest
from src.Engine.Main import getPlaylist


class InputTest(unittest.TestCase):
    def test_inputDataFile(self):
        inputType = InputDataFile()
        logger = IOTest()
        directoryPath = "../../Music/"

        playlist = getPlaylist(inputType, directoryPath, logger)
        self.assertEqual("Beat Of Success.mp3", playlist[0])

    def test_inputDataStub(self):
        inputType = InputDataStub()
        logger = IOTest()
        playlist = getPlaylist(inputType, "stubMusic", logger)
        self.assertEqual("stub_bensound-dubstep.wav", playlist[0])


if __name__ == '__main__':
    unittest.main()
