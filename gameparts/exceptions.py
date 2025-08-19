class BoardIndexError(IndexError):
    def __str__(self):
        return 'A value was entered outside the playing field'


class CellOccupiedError(Exception):
    def __str__(self):
        return 'Attempt to change occupied cell'
