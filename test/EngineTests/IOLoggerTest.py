import unittest

from src.Data.ReadLogFile import readLogFile
from src.Display.IOTest import IOTest
from src.Engine.Main import main


class IOLoggerTest(unittest.TestCase):

    def test_replayInputs(self):
        logInput = readLogFile("../../Logs/InputLog.txt")
        logOutput = readLogFile("../../Logs/OutputLog.txt")
        logger = IOTest()
        logger.setInputList(logInput)
        main("../../Music/", logger)
        testOutput = logger.getOutputList()

        self.assertEqual(testOutput, logOutput)


if __name__ == '__main__':
    unittest.main()
