def printing(n):
    if n>=10:
        return 
    print(n)
    printing(n+1)

printing(0)