# Pascal's Triangle Generator

This Python script generates Pascal's Triangle up to the nth row.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Pascal's Triangle is a triangular array of binomial coefficients. Each number in the triangle is the sum of the two directly above it. The first row is 1, the second row is 1,1, and each subsequent row is constructed by adding the numbers above and to the left and right.

This script provides a function `pascal_triangle(n)` that generates Pascal's Triangle up to the nth row and returns it as a list of lists.

## Installation

No installation is required. Simply download or clone the `0-pascal_triangle.py` file to your local environment.

## Usage

To use the script, import the `pascal_triangle` function from the `0-pascal_triangle.py` file and call it with the desired value of `n` to generate Pascal's Triangle.

```python
from 0-pascal_triangle import pascal_triangle

# Generate Pascal's Triangle up to the 5th row
triangle = pascal_triangle(5)
print(triangle)
