def readLogFile(filePath):
    with open(filePath, "r") as logFile:
        rawData = logFile.read().splitlines()
    return rawData
