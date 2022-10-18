def chessboard(n):
    for i in range(n):
        for i in range(1,2):
            print((" "+"##")*4)
        for i in range(3,4):
            print(("##"+" ")*4)

chessboard(8)
