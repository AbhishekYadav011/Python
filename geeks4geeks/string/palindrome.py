def palindromeCheck(s1):
    # """first method"""
    # if s1 == s1[::-1]:
    #     print('YES')
    # else:
    #     print('NO')

    """Second Method"""
    start = 0
    end = len(s1) - 1
    while start < end:
        if s1[start] != s1[end]:
            print('NO')
            break
        start += 1
        end -= 1

    else:
        print('YES')


if __name__ == '__main__':
    palindromeCheck('MOM')
