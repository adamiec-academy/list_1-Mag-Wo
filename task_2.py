def chessboard(n,k):
    for i in range(n):
        for i in range(k):
            print((k * " " + k * "#") * n)
        for i in range(k):
            print((k * "#" + k * " ") * n)
          
chessboard(4,5)
