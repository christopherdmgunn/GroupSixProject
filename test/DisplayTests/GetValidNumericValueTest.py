import unittest

from src.Display.ConsoleInputs import getValidNumericValue
from src.Display.IOTest import IOTest


class GetValidNumericValueTest(unittest.TestCase):
    outputMessage = "Enter a value"
    errorMessage = "This is an invalid value"
    validRange = 11
    valueType = int

    def test_getValidNumericValue(self):
        logger = IOTest()
        logger.setInputList(["5"])
        result = getValidNumericValue(self.outputMessage, self.errorMessage, self.validRange, self.valueType, logger)
        self.assertEqual(5, result)

    def test_getValidNumericValueWithSpaces(self):
        logger = IOTest()
        logger.setInputList(["    5     "])
        result = getValidNumericValue(self.outputMessage, self.errorMessage, self.validRange, self.valueType, logger)
        self.assertEqual(5, result)

    def test_getValidMinNumericValue(self):
        logger = IOTest()
        logger.setInputList(["0"])
        result = getValidNumericValue(self.outputMessage, self.errorMessage, self.validRange, self.valueType, logger)
        self.assertEqual(0, result)

    def test_getValidMaxNumericValue(self):
        logger = IOTest()
        logger.setInputList(["10"])
        result = getValidNumericValue(self.outputMessage, self.errorMessage, self.validRange, self.valueType, logger)
        self.assertEqual(10, result)

    def test_getOutOfBoundsNumericValue(self):
        logger = IOTest()
        logger.setInputList(["-1", "0"])
        result = getValidNumericValue(self.outputMessage, self.errorMessage, self.validRange, self.valueType, logger)
        self.assertEqual("This is an invalid value", logger.outputList[-1])

    def test_getInvalidNumericValue(self):
        logger = IOTest()
        logger.setInputList(["invalid number", "0"])
        result = getValidNumericValue(self.outputMessage, self.errorMessage, self.validRange, self.valueType, logger)
        self.assertEqual("This is an invalid value", logger.outputList[-1])

    def test_getEmptyNumericValue(self):
        logger = IOTest()
        logger.setInputList(["", "0"])
        result = getValidNumericValue(self.outputMessage, self.errorMessage, self.validRange, self.valueType, logger)
        self.assertEqual("This is an invalid value", logger.outputList[-1])

    def test_getMultipleNumericValues(self):
        logger = IOTest()
        logger.setInputList(["1", "5", "0"])
        result = getValidNumericValue(self.outputMessage, self.errorMessage, self.validRange, self.valueType, logger)
        result = getValidNumericValue(self.outputMessage, self.errorMessage, self.validRange, self.valueType, logger)
        result = getValidNumericValue(self.outputMessage, self.errorMessage, self.validRange, self.valueType, logger)
        self.assertEqual(0, result)



if __name__ == '__main__':
    unittest.main()
