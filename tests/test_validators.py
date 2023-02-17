from typing import Any

import pytest

from sudoku_solver.exceptions import (
    InvalidInputGridException,
    InvalidInputValuesException,
)
from sudoku_solver.validators import validate_input


@pytest.mark.parametrize(
    ["input_grid"],
    [
        pytest.param("", id="not-a-list-of-rows"),
        pytest.param([], id="empty-list-of-rows"),
        pytest.param([0] * 8, id="not-enough-rows"),
        pytest.param([0] * 10, id="too-many-rows"),
        pytest.param([""] * 9, id="not-list-of-columns"),
        pytest.param([[]] * 9, id="empty-list-of-columns"),
        pytest.param([[0] * 8] * 9, id="not-enough-columns"),
        pytest.param([[0] * 10] * 9, id="too-many-columns"),
    ],
)
def test_validate_input_invalid_input_grid(input_grid: Any) -> None:
    with pytest.raises(InvalidInputGridException):
        validate_input(input_grid)


@pytest.mark.parametrize(
    ["input_grid"],
    [
        pytest.param([[""] * 9] * 9, id="not-integer-values"),
        pytest.param([[1] * 9] * 9, id="duplicate-values-in-row"),
        pytest.param(
            [[1, 0, 0, 0, 0, 0, 0, 0, 0]] * 9, id="duplicate-values-in-column"
        ),
        pytest.param(
            [
                [1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0, 0],
                [0] * 9,
                [0] * 9,
                [0] * 9,
                [0] * 9,
                [0] * 9,
                [0] * 9,
                [0] * 9,
            ],
            id="duplicate-values-in-box",
        ),
    ],
)
def test_validate_input_invalid_input_values(input_grid: Any) -> None:
    with pytest.raises(InvalidInputValuesException):
        validate_input(input_grid)


def test_validate_input_valid_input() -> None:
    validate_input(
        [
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 2, 0, 0, 0, 0, 0, 0, 0],
            [3, 0, 0, 4, 0, 0, 0, 0, 0],
            [2, 0, 0, 0, 3, 0, 0, 0, 0],
            [0] * 9,
            [0] * 9,
            [0] * 9,
            [0] * 9,
            [0] * 9,
        ]
    )
