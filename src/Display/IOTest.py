from src.Data.readLogFile import readLogFile
from src.Display.IO import IO

class IOTest(IO):

    inputList = []
    outputList = []

    def SetInputList(self, inputList):
        self.inputList = inputList
        print(self.inputList)

    def TakeInput(self, message):
        if len(self.inputList) > 0:
            command = self.inputList.pop(0)
            return command
        return ""

    def ShowOutput(self, message):
        self.outputList.append(message)

    def GetInputList(self):
        return self.inputList

    def GetOutputList(self):
        return self.outputList