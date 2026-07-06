import random
numero = random.randint(1,10)
cont = 0

while True:
    tentativa = int(input("digite um número inteiro de 1 a 10: "))

    if tentativa < numero:
        cont += 1
        print("tente um número maior")
    elif tentativa > numero:
        cont += 1
        print("tente um número menor")
    elif tentativa == numero:
        print("você acertou!")
        cont += 1
        print(f"você tentou {cont} vezes")
        break
    else:
        print("tentativa invalida, tente novamente")