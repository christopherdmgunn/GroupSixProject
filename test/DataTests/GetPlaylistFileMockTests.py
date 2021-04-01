import unittest

from unittest.mock import MagicMock

from src.Data.InputDataFile import InputDataFile
from src.Display.IOTest import IOTest
from src.Engine.Main import getPlaylist


class GetPlayListFileMocksTest(unittest.TestCase):
    def test_getPlaylistFileNotFoundMock(self):
        inputType = InputDataFile()
        directoryPath = "missing file"
        logger = IOTest()
        InputDataFile.getRawData = MagicMock(side_effect=FileNotFoundError)
        playlist = getPlaylist(inputType, directoryPath, logger)
        self.assertEqual("stub_bensound-dubstep.wav", playlist[0])

    def test_getPlaylistFileNotFoundMockOutput(self):
        inputType = InputDataFile()
        directoryPath = "missing file"
        logger = IOTest()
        InputDataFile.getRawData = MagicMock(side_effect=FileNotFoundError)
        playlist = getPlaylist(inputType, directoryPath, logger)
        self.assertEqual("Error: Directory was not found. Switching to stub", logger.getOutputList()[-1])


if __name__ == '__main__':
    unittest.main()
