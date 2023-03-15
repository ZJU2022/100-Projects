def fib(num):
    n,a,b = 0,0,1
    while n < num:
        yield b
        a,b = b,a+b
        n += 1
    
for x in fib(20):
    print(x)
print("=================")
f = fib(6)
print(f)