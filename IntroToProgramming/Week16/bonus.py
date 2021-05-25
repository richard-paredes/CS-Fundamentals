import sys
sys.setrecursionlimit(3500)
def g(x, y):
    if (x == 0):
        return (y+1)
    if (y == 0):
        return g(x-1, 1)
    return g(x-1,g(x,y-1))

def main():
    output = g(3,8)
    print(output)
main()