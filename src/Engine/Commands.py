from enum import Enum


class Commands(Enum):
    PLAY = ["play", "p"]
    STOP = ["stop", "s"]
    VOLUME = ["volume", "v"]
    CLOSE = ["close", "c"]
    PAUSE = ["pause"]
    UNPAUSE = ["unpause", "u"]
