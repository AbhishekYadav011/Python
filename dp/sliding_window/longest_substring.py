# Sliding window technique
# https://www.geeksforgeeks.org/window-sliding-technique/

def lengthOfLongestSubstring(s):
    str_list = []
    max_length = 0

    for x in s:
        if x in str_list:
            print(x, ":", str_list.index(x))
            str_list = str_list[str_list.index(x) + 1:]

        str_list.append(x)
        print(str_list)
        max_length = max(max_length, len(str_list))
    # print(str_list)

    return max_length


print(lengthOfLongestSubstring("ABDEFGABEF"))
