def Polycarp():
    t = int(input())

    while t > 0:
        u = set()

        n = int(input())
        numbers = input().split(" ")

        for i in range(n-1,-1,-1):
            if numbers[i] in u:
                print(n)
                break
            u.add(numbers[i])
            n = n - 1

        if(n==0):
            print(n)

        t = t - 1

        

if __name__ == '__main__':
    Polycarp()