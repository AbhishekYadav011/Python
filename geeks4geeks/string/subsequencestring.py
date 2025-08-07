"""A subsequence is a sequence that 
can be derived from another sequence by removing zero or more elements, 
without changing the order of the remaining elements."""

def subsequence(s1,s2):
    if len(s2) > len(s1):
        return False
    i , j =0 ,0
    while (i < len(s1) and j < len(s2)):
        if s1[i] == s2[j]:
            j +=1
        i +=1

    if j == len(s2):
        return True
    else:
        return False
    
if __name__ == '__main__':
    s1 = 'ABCDE'
    s2 = 'AE'
    result = subsequence(s1,s2)
    print(result)