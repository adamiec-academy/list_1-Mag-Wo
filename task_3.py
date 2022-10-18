def envelope(n,x):
    print("*"*n)
    for i in range(x):
        print("*"+(i*" ")+"*"+(n//2 + 1 - 2*i) * " " + "*" + i * " " + "*")
    print("*"+(" "*x)+"*"+(" "*x)+"*")
    for i in range(x):
        print("*"+((x-i-1)*" ")+"*"+(2*i+1)*" "+"*"+((x-i-1)*" ")+"*")
    print("*"*n)

envelope(9,3)
