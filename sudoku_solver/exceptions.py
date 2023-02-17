class InvalidInputException(Exception):
    ...


class InvalidOutputException(Exception):
    ...


class InvalidInputGridException(InvalidInputException):
    def __str__(self) -> str:
        return "Input must be a 9x9 grid"


class InvalidInputValuesException(InvalidInputException):
    def __str__(self) -> str:
        return "Input values are invalid"


class GridNotResolvedException(InvalidOutputException):
    def __str__(self) -> str:
        return "Grid could not be fully resolved"


class InvalidOutputValuesException(InvalidOutputException):
    def __str__(self) -> str:
        return "Output values are invalid"
