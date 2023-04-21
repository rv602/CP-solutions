def main():
    t = int(input())
    body = []
    x=0
    y=0
    z=0

    for i in range(t):
        vector = list(map(int, input().split(' ')))
        body.append(vector)

    for i in range(len(body)):
        x = x + body[i][0]
        y = y + body[i][1]
        z = z + body[i][2]

    if x == y == z == 0:
        print('YES')
    else:
        print('NO')
        
        
if __name__ == '__main__':
    main()