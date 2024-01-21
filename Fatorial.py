numero = int(input("Qual número deseja calcular o fatorial?: "))
fatorial = 1
if numero < 0:
    print("Não existe fatorial de um número negativo")
elif numero == 0:
    print("O fatorial de 0 é sempre 1")
else:
    for x in range(1, numero + 1):
        fatorial *= x
    print(f'O fatorial de {numero} é {fatorial}')