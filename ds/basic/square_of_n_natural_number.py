# Time complexity is O(1)
def squareofnaturalnumbers(n):
    return (n * (n + 1) * (2 * n + 1)) // 6


if __name__ == "__main__":
    print(squareofnaturalnumbers(5))
