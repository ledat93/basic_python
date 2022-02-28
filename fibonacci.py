def fib(n):
    l = [0,1]
    for i in range(2, n+1):
        item = l[i-1] + l[i-2]
        l.append(item)
    return l[n]
print(fib(90)) 

def recursion_fib(n):
    if lst[n] == None:
        if n <= 1:
            lst[n] = n
        else:
            lst[n] = recursion_fib(n-1) + recursion_fib(n-2)
    return lst[n]

inp = input('Enter n=', )
lst = [None for i in range(int(inp)+1)]
print(recursion_fib(int(inp)))
    
    
   