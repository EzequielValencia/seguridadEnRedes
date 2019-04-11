abecedario1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T',
              'U', 'V', 'W', 'X', 'Y', 'Z']
abecedario2 = ['T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                        'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S']


def cifrar(texto):
    textoSalida = ''
    print('Voy a cifrar {}'.format(texto))
    for j in range(len(texto)):
        for i in range(len(abecedario1)):
            if texto[j] == abecedario1[i]:
                textoSalida += abecedario2[i]

    return textoSalida


def descifrar(texto):
    textoSalida = ''

    for letraTexto in texto:

        for i in range(len(abecedario2)):

            if letraTexto == abecedario2[i]:
                textoSalida += abecedario1[i]

    return textoSalida



palabra = input('Dame una palabra: ').strip().upper()
print('Tu palabra es {}'.format(palabra))
opcion = int(input('1.- Cifrar \n2.- Descifrar \nOpcion: '))

if opcion == 1:
    cifrado = cifrar(palabra)
    print('Tu palabra cifrada es {}'.format(cifrado))
else:
    print('Tu palabra descifrada es {}'.format(descifrar(palabra)))
