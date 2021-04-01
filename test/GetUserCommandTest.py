import unittest

from src.Display.ConsoleInputs import getUserCommand
from src.Display.IOTest import IOTest


class GetUserCommandTest(unittest.TestCase):
    def test_GetValidUserCommand(self):
        logger = IOTest()
        logger.setInputList(["close"])
        self.assertEqual("close", getUserCommand(logger))

    def test_GetValidUserCommandAlternateOption(self):
        logger = IOTest()
        logger.setInputList(["c"])
        self.assertEqual("close", getUserCommand(logger))

    def test_GetInvalidUserCommand(self):
        logger = IOTest()
        logger.setInputList(["1", "close"])
        self.assertEqual("close", getUserCommand(logger))

    def test_GetEmptyUserCommand(self):
        logger = IOTest()
        logger.setInputList(["", "close"])
        self.assertEqual("close", getUserCommand(logger))

    def test_GetMultipleUserCommands(self):
        logger = IOTest()
        logger.setInputList(["volume", "s", "close"])
        getUserCommand(logger)
        getUserCommand(logger)
        self.assertEqual("close", getUserCommand(logger))


if __name__ == '__main__':
    unittest.main()
