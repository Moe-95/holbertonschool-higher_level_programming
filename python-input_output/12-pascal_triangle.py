#!/usr/bin/python3

def pascal_triangle(n):
    """Generate Pascal's triangle up to the specified number of rows."""
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle

if __name__ == "__main__":
    triangle = pascal_triangle(5)
    for row in triangle:
        print(row)
