def printFunction(n):
    outList = [str(i) for i in range(1,n+1)]
    result = "".join(outList)
    return result

if __name__ == '__main__':
    n = int(input())
    print(printFunction(n))
    