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
    # Test cases
    print("n = 5")
    print_triangle(pascal_triangle(5))
    
    print("\nn = 1")
    print_triangle(pascal_triangle(1))
    
    print("\nn = 0")
    print(pascal_triangle(0))  # Should return an empty list
    
    print("\nn = 10")
    print_triangle(pascal_triangle(10))
    
    print("\nn = 100")
    # For large n, we won't print the entire triangle, just the length
    large_triangle = pascal_triangle(100)
    print("Length of Pascal's Triangle with n=100:", len(large_triangle))
