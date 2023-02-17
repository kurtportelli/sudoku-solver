def get_row(grid: list[list[int | set[int]]], row_index: int) -> list[int | set[int]]:
    return grid[row_index]


def get_column(
    grid: list[list[int | set[int]]], column_index: int
) -> list[int | set[int]]:
    return [row[column_index] for row in grid]


def get_box(
    grid: list[list[int | set[int]]], row_index: int, column_index: int
) -> list[int | set[int]]:
    box_row_start = (row_index // 3) * 3
    box_column_start = (column_index // 3) * 3

    box = []
    for box_row_index in range(box_row_start, box_row_start + 3):
        box.extend(grid[box_row_index][box_column_start : box_column_start + 3])

    return box
