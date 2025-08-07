"""Repeated Character Whose First Appearance is Leftmost
Input: geeksforgeeks
Output: g
"""
char = 256

def leftmostrepeatingchar(s):
    
    visited = [False] * char
    res = -1

    for i in range(len(s)-1,-1,-1):
        if visited[ord(s[i])] == True:
            res = i
        else:
            visited[ord(s[i])] = True
    return res

if __name__ == '__main__':
    s = "geeksforgeeks"
    index = leftmostrepeatingchar(s)     
    print("left most repeated character is:",s[index])   

