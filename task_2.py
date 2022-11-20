def chessboard(n, k):

    for i in range(n):
        for _ in range(k):
            print((k * " " + k * "#") * n)
        for _ in range(k):
            print((k * "#" + k * " ") * n)

