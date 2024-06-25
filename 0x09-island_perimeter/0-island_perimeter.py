#!/usr/bin/python3
def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the grid.
    
    :param grid: List of list of integers representing the grid
    :return: Integer representing the perimeter of the island
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Check all four sides
                if r == 0 or grid[r - 1][c] == 0:
                    perimeter += 1  # Top
                if r == rows - 1 or grid[r + 1][c] == 0:
                    perimeter += 1  # Bottom
                if c == 0 or grid[r][c - 1] == 0:
                    perimeter += 1  # Left
                if c == cols - 1 or grid[r][c + 1] == 0:
                    perimeter += 1  # Right
    
    return perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
