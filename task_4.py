def snowball(n,k):

    for i in range(2,8,2):
        print(k*" "+(n-i-1)//2 * " " +(i+1)*"#")
    print(k*" "+ "#"*n)
    for i in range(2,8,2):
        print(k*" "+((2*(i+n)//(n//2))-6) * " "+ (n-i+2)*"#")

snowball(7,10)

def snowman(n):
    pass
