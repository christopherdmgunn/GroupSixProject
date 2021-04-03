import unittest

from src.Display.ConsoleInputs import getUserCommand
from src.Display.IOTest import IOTest


class GetUserCommandTest(unittest.TestCase):
    message = "Enter a command"

    def test_getUserCommand(self):
        logger = IOTest()
        logger.setInputList(["close"])
        self.assertEqual("close", getUserCommand(self.message, logger))

    def test_getUserCommandWithSpaces(self):
        logger = IOTest()
        logger.setInputList(["      close       "])
        self.assertEqual("close", getUserCommand(self.message, logger))

    def test_getMultipleUserCommands(self):
        logger = IOTest()
        logger.setInputList(["volume", "s", "close"])
        getUserCommand(self.message, logger)
        getUserCommand(self.message, logger)
        self.assertEqual("close", getUserCommand(self.message, logger))


if __name__ == '__main__':
    unittest.main()
