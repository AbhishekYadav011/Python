def isInterleave(str1, str2, str3) -> bool:
    N = len(str3)
    A, B = len(str1), len(str2)
    if A + B != N:
        return False

    def rec(i, j, k):
        # base condition
        if i == A and j == B and k == N:
            return True
        b1, b2 = False, False
        if i < A and str1[i] == str3[k]:
            b1 = rec(i + 1, j, k + 1)
            print("Iteration number i:", i)
            print("b1:", b1)
        if j < B and str2[j] == str3[k]:
            b2 = rec(i, j + 1, k + 1)
            print("Iteration number j:", j)
            print("b2:", b2)
        return b1 or b2

    return rec(0, 0, 0)


def test(A, B, C):
    if (isInterleave(A, B, C)):
        print(C, "is interleaved of", A, "and", B)
    else:
        print(C, "is not interleaved of", A, "and", B)


if __name__ == '__main__':
    # test("XXY", "XXZ", "XXZXXXY")
    # test("XY", "WZ", "WZXY")
    test("XY", "X", "XXY")
    # test("YX", "X", "XXY")
    # test("XXY", "XXZ", "XXXXZY")
