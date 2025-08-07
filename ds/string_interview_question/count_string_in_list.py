l1 = ["abhi", "tinku", "abhi"]


def count_string(l1):
    count = 0
    for i in l1:
        if i == "abhi":
            count += 1
    return count


totalcount = count_string(l1)
print(totalcount)
