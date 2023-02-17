from copy import deepcopy
from typing import Any

from sudoku_solver.utils import get_box, get_column, get_row
from sudoku_solver.validators import POSSIBLE_VALUES, validate_input, validate_output


def replace_zeros(grid: list[list[int]]) -> list[list[int | set[int]]]:
    """
    Replace any zeros (0) in the input grid with a set of all possible_values.
    """
    new_grid: list[list[int | set[int]]] = deepcopy(grid)  # type: ignore

    for row_index in range(9):
        for column_index in range(9):
            if new_grid[row_index][column_index] == 0:
                new_grid[row_index][column_index] = POSSIBLE_VALUES

    return new_grid


def calculate_certainties(
    grid: list[list[int | set[int]]],
) -> tuple[list[list[int | set[int]]], bool]:
    """
    Calculate all values that are certain and do not require guessing.
    Returns the new_grid and along with a boolean indicating if any changes were made.
    """
    new_grid: list[list[int | set[int]]] = deepcopy(grid)
    modified = False

    for row_index in range(9):
        for column_index in range(9):
            cell = new_grid[row_index][column_index]

            if isinstance(cell, set):
                row_values = {
                    cell
                    for cell in get_row(new_grid, row_index)
                    if isinstance(cell, int)
                }
                column_values = {
                    cell
                    for cell in get_column(new_grid, column_index)
                    if isinstance(cell, int)
                }
                box_values = {
                    cell
                    for cell in get_box(new_grid, row_index, column_index)
                    if isinstance(cell, int)
                }

                used_values = row_values | column_values | box_values

                possible_values = cell - used_values

                if possible_values != cell:
                    if len(possible_values) == 1:
                        new_grid[row_index][column_index] = possible_values.pop()
                    else:
                        new_grid[row_index][column_index] = possible_values
                    modified = True

    return new_grid, modified


def solve(input_grid: Any) -> list[list[int]]:
    validated_input_grid: list[list[int]] = validate_input(input_grid)

    grid: list[list[int | set[int]]] = replace_zeros(validated_input_grid)

    while True:
        grid, modified = calculate_certainties(grid)

        if not modified:
            break

    return validate_output(grid)
