def checkAnagram(s1, s2):
    # """First Method"""
    # if len(s1) != len(s2):
    #     print('NO')
    # if sorted(s1) == sorted(s2):
    #     print('YES')
    # else:
    #     print('NO')
    """Second method"""
    if len(s1) != len(s2):
        return False

    count = [0] * 256
    for i in range(len(s1)):
        count[ord(s1[i])] += 1
        count[ord(s2[i])] -= 1
    for x in count:
        if x != 0:
            return False
    return True


if __name__ == '__main__':
    # checkAnagram('listen', 'silent')
    print(checkAnagram('listen', 'silent'))
    print(checkAnagram('b', 'd'))
