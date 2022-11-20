def cross(n):
    for i in range(n):
        print(" " * n + "*" * n + " " * n)
    for i in range(n):
        print((" " * 3) * n)
    for i in range(n):
        print(" " * n + "*" * n + " " * n)

n = 4
cross(n)
