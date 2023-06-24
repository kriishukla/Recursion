def ToH(n, A, B, C):
    if n == 1:
        print(f"Move 1 from {A} to {C}")
        return
    ToH(n - 1, A, C, B)
    print(f"Move {n} from {A} to {C}")
    ToH(n - 1, B, A, C)


ToH(4, 'A', 'B', 'C')
