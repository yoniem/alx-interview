0x08. Making Change

# Coin Change Problem

This module provides a solution to the classic coin change problem using a dynamic programming approach.

## Usage

To use the `makeChange` function, import it and provide a list of coin denominations and a total amount:

```python
from 0-making_change import makeChange

print(makeChange([1, 2, 25], 37))  # Output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
