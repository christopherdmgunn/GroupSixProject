from abc import ABC as abstractBaseClass, abstractmethod

class IO(abstractBaseClass):
    @abstractmethod
    def takeInput(self, message):
        pass

    @abstractmethod
    def showOutput(self, message):
        pass