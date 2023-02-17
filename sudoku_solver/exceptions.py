class InvalidInputException(Exception):
    ...


class InvalidInputGridException(InvalidInputException):
    def __str__(self) -> str:
        return "Input must be a 9x9 grid"


class InvalidInputValuesException(InvalidInputException):
    def __str__(self) -> str:
        return "Input values are invalid"
