def getFileToPlay(fileList, logger):
    fileRange = len(fileList)
    outputMessage = "Please select a track number"
    errorMessage = "That is an invalid track number"

    fileIdentifier = getValidNumericValue(outputMessage, errorMessage, fileRange, int, logger)
    fileName = fileList[fileIdentifier]
    return fileName


def getVolume(logger):
    volumeRange = 11
    outputMessage = "Enter a volume between 0 for mute and 10"
    errorMessage = "That is an invalid volume"

    volume = getValidNumericValue(outputMessage, errorMessage, volumeRange, float, logger)
    logger.showOutput("Volume changed to " + str(volume))
    volume = volume / 10
    return volume


def getValidNumericValue(outputMessage, errorMessage, validRange, valueType, logger):
    validValueCondition = False
    while not validValueCondition:
        try:
            userInput = valueType(getUserCommand(outputMessage, logger))

            if userInput not in range(validRange):
                raise ValueError
        except:
            logger.showOutput(errorMessage)
        else:
            validValueCondition = True
    return userInput


def getUserCommand(message, logger):
    userCommand = logger.takeInput(message)

    if len(userCommand) > 0:
        while userCommand[0] == " " or userCommand[-1] == " ":
            userCommand = userCommand.strip(" ")

    return userCommand