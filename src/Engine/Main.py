from src.Data.InputDataFile import InputDataFile
from src.Data.InputDataStub import InputDataStub
from src.Display.ConsoleInputs import *
from src.Display.ConsoleOutputs import *
from src.Display.IOLogger import IOLogger
from src.Engine.Commands import Commands
from src.Engine.TrackControls import *
from src.Engine.VolumeControls import *

pygame.mixer.init()

def getPlaylist(inputType, directoryPath, logger):
    try:
        playlist = inputType.getRawData(directoryPath)
    except FileNotFoundError:
        logger.showOutput("Error: Directory was not found. Switching to stub")
        inputSource = InputDataStub()
        playlist = inputSource.getRawData(directoryPath)
    return playlist


def main(directoryPath="Music/", logger=IOLogger(True)):

    soundPlayer = ""
    volume = 1.0
    close = False
    musicFiles = getPlaylist(InputDataFile(), directoryPath, logger)

    if type(logger) == IOLogger:
        logger.initialiseLogs()

    while not close:
        print()
        displayCommands(logger)
        command = getUserCommand("Please enter a command", logger)

        # handle command

        # stop
        if command in Commands.STOP.value:
            stopSound(soundPlayer, logger)

        # play
        elif command in Commands.PLAY.value:
            displayFiles(musicFiles, logger)
            songName = getFileToPlay(musicFiles, logger)
            filePath = directoryPath + songName
            soundPlayer = playSound(filePath, volume, logger)

        # volume control
        elif command in Commands.VOLUME.value:
            volume = getVolume(logger)
            setVolume(volume, soundPlayer)

        # pause
        elif command in Commands.PAUSE.value:
            playPause(logger)

        # unpause
        elif command in Commands.UNPAUSE.value:
            unPause(logger)

        # close program
        elif command in Commands.CLOSE.value:
            close = True

        else:
            logger.showOutput("That is not a valid user command")

    logger.showOutput("Closing program")

if __name__ == '__main__':
    main()
