from enum import Enum


# 59132587963756471
class BoardPosition(Enum):
    BOARD = '48021476852645360'


class BoardGrid(Enum):
    GRID = ' %s | %s | %s '
    SEPARATOR = '---+---+---'


class BoardDisplay(Enum):
    RST = '\033[00m'
    GRAY = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    VIOLET = '\033[35m'
    VERDAO = '\033[36m'
    WHITE = '\033[37m'


class InfoParameters(Enum):
    PARAMS = '%s%s%s'
    PARAMS_SHOW_RESULT = '%s%s%i%s'

