def loop(n):
    nNegative = [i*i for i in range(n)]
    output = '\n'.join(map(str, nNegative))
    print(output)

if __name__ == '__main__':
    n = int(input())
    loop(n)