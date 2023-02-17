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

    for row_index in range(9):
        for column_index in range(9):
            value = input_grid[row_index][column_index]

            if value == 0:
                continue

            row = input_grid[row_index]
            if row.count(value) != 1:
                raise InvalidInputValuesException

            column = [row[column_index] for row in input_grid]
            if column.count(value) != 1:
                raise InvalidInputValuesException

            box_row_start = (row_index // 3) * 3
            box_column_start = (column_index // 3) * 3

            box = []
            for box_row_index in range(box_row_start, box_row_start + 3):
                box.extend(
                    input_grid[box_row_index][box_column_start : box_column_start + 3]
                )

            if box.count(value) != 1:
                raise InvalidInputValuesException

    return input_grid
