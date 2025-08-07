"""You are given a string s.
You need to find the missing characters in the string to make a panagram
( a sentence using every letter of english alphabet at least once ).
Note: The output characters will be lowercase and lexicographically sorted."""


def missingPanagram(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    test = []
    for i in alphabet:
        print(i)
        if i not in set(s.lower()):
            test.append(i)
    print(test)
    return ("").join(sorted(test))


if __name__ == '__main__':
    print(missingPanagram('Abcdefghijklmnopqrstuvwxy'))
