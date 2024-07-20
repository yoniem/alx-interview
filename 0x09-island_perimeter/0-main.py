#!/usr/bin/python3
"""
0-main
"""

# Import the function to test
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    # Test Case 1
    grid1 = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print("Test Case 1:", island_perimeter(grid1))  # Expected output: 12

    # Test Case 2
    grid2 = [
        [1]
    ]
    print("Test Case 2:", island_perimeter(grid2))  # Expected output: 4

    # Test Case 3
    grid3 = [
        [0, 1],
        [1, 1]
    ]
    print("Test Case 3:", island_perimeter(grid3))  # Expected output: 8

    # Test Case 4
    grid4 = [
        [1, 0],
        [0, 1]
    ]
    print("Test Case 4:", island_perimeter(grid4))  # Expected output: 8

    # Test Case 5
    grid5 = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    print("Test Case 5:", island_perimeter(grid5))  # Expected output: 4

    # Additional Test Cases
    grid6 = [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1]
    ]
    print("Test Case 6:", island_perimeter(grid6))  # Expected output: 16

    grid7 = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 1, 1]
    ]
    print("Test Case 7:", island_perimeter(grid7))  # Expected output: 16

    grid8 = [
        [0, 1, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 1],
        [1, 1, 0, 1, 1, 1],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 0, 0]
    ]
    print("Test Case 8:", island_perimeter(grid8))  # Expected output: 20
