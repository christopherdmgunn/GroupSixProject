from src.Engine.Commands import Commands


def displayFiles(fileList, logger):
    for entryNumber, entry in enumerate(fileList):
        logger.showOutput(str(entryNumber) + ":" + entry)


def displayCommands(logger):
    commandList = []
    for command in Commands:
        commandList.append(command.value[0])
    logger.showOutput(str(commandList))