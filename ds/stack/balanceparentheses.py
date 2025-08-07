"""Given an expression string exp, write a program to examine whether the pairs and the orders of “{“, “}”, “(“, “)”,
“[“, “]” are correct in exp."""


def inputstring(str):
    stack = []
    for i in str:
        if i == '[' or i == '(' or i == '{':
            stack.append(i)
        else:
            # for use case )((()))
            if not stack:
                return False
            elif not matchcloseparentheses(stack[-1], i):
                return False
            else:
                stack.pop()
    # for use case (())(
    if stack:
        return False
    else:
        return True


def matchcloseparentheses(str1, str2):
    if (str1 == '[' and str2 == ']') or (str1 == '(' and str2 == ')') or (str1 == '{' and str2 == '}'):
        return True
    return False


if __name__ == '__main__':
    print("Provide string is balnaced:", inputstring('({})[]'))
