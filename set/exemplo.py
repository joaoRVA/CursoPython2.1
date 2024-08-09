# exemplo de utilização de sets

letras = set()

while True:
    letra = input("Digite uma letra: ")
    letras.add(letra.lower())

    if 'l' in letras:
        print("Parabéns, você encontrou a letra certa! 'l' ")
        break
    print(letras)
