from typing import Any

from sudoku_solver.exceptions import (
    InvalidInputGridException,
    InvalidInputValuesException,
)


def validate_input(input_grid: Any) -> list[list[int]]:
    if not (isinstance(input_grid, list) and len(input_grid) == 9):
        raise InvalidInputGridException

    for row in input_grid:
        if not (isinstance(row, list) and len(row) == 9):
            raise InvalidInputGridException

        for value in row:
            if not isinstance(value, int):
                raise InvalidInputValuesException

    return [[0] * 9] * 9
