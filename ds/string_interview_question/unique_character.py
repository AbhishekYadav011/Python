# to check all characters are unique in string
def make_link(arr):
    G = []
    for i in arr:
        if i not in G:
            G.append(i)
    if len(G) != len(arr):
        print("not unique")
    else:
        print("Unique")

make_link("moon")