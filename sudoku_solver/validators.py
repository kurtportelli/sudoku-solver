from typing import Any

from sudoku_solver.exceptions import (
    GridNotResolvedException,
    InvalidInputGridException,
    InvalidInputValuesException,
    InvalidOutputValuesException,
)
from sudoku_solver.utils import get_box, get_column, get_row

POSSIBLE_VALUES = set(range(1, 10))


def validate_input(grid: Any) -> list[list[int]]:
    if not (isinstance(grid, list) and len(grid) == 9):
        raise InvalidInputGridException

    for row in grid:
        if not (isinstance(row, list) and len(row) == 9):
            raise InvalidInputGridException

        for value in row:
            if not isinstance(value, int):
                raise InvalidInputValuesException

    for row_index in range(9):
        for column_index in range(9):
            value = grid[row_index][column_index]

            if value == 0:
                continue

            row = get_row(grid, row_index)
            column = get_column(grid, column_index)
            box = get_box(grid, row_index, column_index)

            if (
                row.count(value) != 1
                or column.count(value) != 1
                or box.count(value) != 1
            ):
                raise InvalidInputValuesException

    return grid


def validate_output(grid: list[list[int | set[int]]]) -> list[list[int]]:
    for row in grid:
        for value in row:
            if not isinstance(value, int):
                raise GridNotResolvedException

    for row_index in range(9):
        for column_index in range(9):
            value = grid[row_index][column_index]

            if value not in POSSIBLE_VALUES:
                raise InvalidOutputValuesException

            row = get_row(grid, row_index)
            column = get_column(grid, column_index)
            box = get_box(grid, row_index, column_index)

            if (
                row.count(value) != 1
                or column.count(value) != 1
                or box.count(value) != 1
            ):
                raise InvalidOutputValuesException

    return grid  # type: ignore
