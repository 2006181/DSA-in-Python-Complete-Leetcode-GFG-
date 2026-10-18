n = int(input())

def printGfg(n):
    if n == 0:
        return
    print("GFG", end=" ")
    printGfg(n - 1)

printGfg(n)