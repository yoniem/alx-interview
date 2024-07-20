#!/usr/bin/python3
"""
0-island_perimeter
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the grid.
    
    :param grid: List of list of integers representing the grid
    :return: Integer representing the perimeter of the island
    """
    if not grid or not grid[0]:
        return 0

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Check all four sides
                if r == 0 or grid[r - 1][c] == 0:  # Top
                    perimeter += 1
                if r == rows - 1 or grid[r + 1][c] == 0:  # Bottom
                    perimeter += 1
                if c == 0 or grid[r][c - 1] == 0:  # Left
                    perimeter += 1
                if c == cols - 1 or grid[r][c + 1] == 0:  # Right
                    perimeter += 1

    return perimeter
