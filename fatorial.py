n = int(input("Integer:"))

fatorial = 1;

if n == 0:
    print(fatorial)
else:
    while(n != 1):
        fatorial *= n
        n -= 1
    print(fatorial)