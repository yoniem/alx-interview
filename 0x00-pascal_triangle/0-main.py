#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    print("n = 5:")
    print_triangle(pascal_triangle(5))
    print()  # For better separation

    print("n = 1:")
    print_triangle(pascal_triangle(1))
    print()  # For better separation

    print("n = 0:")
    print_triangle(pascal_triangle(0))
    print()  # For better separation

    print("n = 10:")
    print_triangle(pascal_triangle(10))
    print()  # For better separation

    # For large n, like 100, it's better to just check the last row
    print("n = 100 (last row):")
    triangle = pascal_triangle(100)
    print("[{}]".format(",".join([str(x) for x in triangle[-1]])))
