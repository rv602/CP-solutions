def main():
    t = int(input())

    while t>0:
        num = int(input())

        try:
            result = mult2_div6(num)
            print(result)
        except:
            print(-1)
        
        t = t - 1

def mult2_div6(num):

    if num == 1:
        return 0
    
    if num%6==0:
        return 1 + mult2_div6(num/6)
    
    if num%6!=0:
        num = num * 2
        if num%6==0:
            return 2 + mult2_div6(num/6)
        else:
            return -1 + 'nai hoga bhai'
        
        
if __name__ == '__main__':
    main()