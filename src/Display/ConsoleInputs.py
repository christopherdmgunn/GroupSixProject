from src.Engine.Commands import Commands

def getFileToPlay(fileList, logger):
    validFileIdentifier = False
    while not validFileIdentifier:
        fileIdentifier = logger.takeInput("Please enter the track number:")
        try:
            fileIdentifier = int(fileIdentifier)

            if fileIdentifier not in range(len(fileList)):
                raise ValueError

            fileName = fileList[fileIdentifier]
            validFileIdentifier = True
        except:
            logger.showOutput("That is an invalid track number")
    return fileName

def getUserCommand(logger):
    validUserCommand = False
    while not validUserCommand:
        userCommand = logger.takeInput("Please enter a command")

        for commandOptions in Commands:
            if userCommand in commandOptions.value:
                    userCommand = commandOptions.value[0]
                    validUserCommand = True

            if not validUserCommand:
                logger.showOutput("That is an invalid user command")
    return userCommand