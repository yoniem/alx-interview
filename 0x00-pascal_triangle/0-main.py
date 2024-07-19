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
    print_triangle(pascal_triangle(5))
    print()  # For better separation
    print_triangle(pascal_triangle(1))
    print()  # For better separation
    print_triangle(pascal_triangle(0))
    print()  # For better separation
    print_triangle(pascal_triangle(10))
