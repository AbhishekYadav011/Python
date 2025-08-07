def tower_of_hanoi(n, from_rod, to_rod, aux_rod):
    if n == 0:
        return
    tower_of_hanoi(n - 1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    tower_of_hanoi(n - 1, aux_rod, to_rod, from_rod)


if __name__ == '__main__':
    n = 4
    tower_of_hanoi(n, 'A', 'C', 'B')
