n = int(input("Integer:"))

contador = 1
n_impar = 0

while n_impar < n:
    if(contador % 2 != 0):
        print(contador)
        n_impar += 1
    contador += 1