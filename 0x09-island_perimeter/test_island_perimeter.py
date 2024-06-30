#!/usr/bin/python3
from island_perimeter import island_perimeter

def run_tests():
    test_cases = [
        ([[0, 0, 0, 0, 0, 0],
          [0, 1, 0, 0, 0, 0],
          [0, 1, 0, 0, 0, 0],
          [0, 1, 1, 1, 0, 0],
          [0, 0, 0, 0, 0, 0]], 12),

        ([[0, 0, 0, 0, 0, 0],
          [0, 1, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0]], 4),

        ([[0, 0, 0, 0, 0, 0],
          [0, 1, 1, 1, 0, 0],
          [0, 1, 1, 1, 0, 0],
          [0, 1, 1, 1, 0, 0]], 14),

        ([[0], [0], [0]], 0),

        ([[1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1]], 14),

        ([[0, 0, 0, 0, 0, 0],
          [0, 1, 1, 0, 0, 0],
          [1, 1, 1, 0, 0, 0],
          [0, 1, 1, 1, 0, 0],
          [0, 0, 0, 1, 1, 1]], 16),

        ([[0, 1, 0, 0, 0, 1],
          [1, 1, 0, 0, 0, 1],
          [1, 1, 0, 1, 1, 1],
          [0, 1, 1, 1, 0, 0],
          [0, 0, 1, 1, 0, 0]], 20),
    ]

    for i, (grid, expected) in enumerate(test_cases):
        result = island_perimeter(grid)
        print(f"Test case {i+1}: {'Passed' if result == expected else 'Failed'} - Expected: {expected}, Got: {result}")

if __name__ == "__main__":
    run_tests()
