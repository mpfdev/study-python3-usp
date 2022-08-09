import math

number = int(input("Int: "))

size = len(str(number))

soma = 0

if(size == 1):
    print(number)
else:
    while size > 0:
        unidade = number // math.pow(10, size - 1)
        soma += unidade
        number -= unidade * math.pow(10, size - 1)
        size -= 1

    print(int(soma))
