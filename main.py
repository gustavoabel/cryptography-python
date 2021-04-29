from random import randint
import os

'''Esta função gera uma chave aleatória de inteiros de acordo com o comprimento especificado
   Se nenhum argumento for passado, o tamanho será de 10 dígitos'''


def key_generator(lenght=10):
    key = []

    for i in range(lenght):
        key.append(randint(1, 9))

    return key


'''Esta função testa se o arquivo key existe e:
   Captura a chave se ele existir, ou
   gera uma chave e salva em um novo arquivo key se ele não existir'''


def key_validate(path='key.txt'):
    if os.path.isfile(path):
        arch = open(path, 'r')
        key = arch.read()
        arch.close()
        key_list = []

        for i in key:
            key_list.append(int(i))

        return key_list
    else:
        arch = open(path, 'w')
        key = key_generator()
        key_str = ''

        for i in key:
            key_str += str(i)

        arch.write(key_str)
        arch.close()

        return key


def open_txt(path):
    if os.path.isfile(path):
        arch = open(path, 'r', encoding='utf-8')
        text = arch.readlines()
        arch.close()
        return decript(text, key_validate())
    else:
        return write_text(path)


def write_text(path):
    number_lines = abs(int(input('Entre com o número de linhas desejadas: ')))
    text = []

    for i in range(number_lines):
        text.append(input())

    text_cripto = cript(text, key_validate())

    arch = open(path, 'w', encoding='utf-8')

    for line in text_cripto:
        arch.write(line + '\n')

    arch.close()

    return 'Processo terminado.', ''


def cript(text, key):
    text_cript = []

    for linha in text:
        aux = ''
        for i in range(len(linha)):
            aux += chr(ord(linha[i]) + key[i % len(key)])
        text_cript.append(aux)

    return text_cript


def decript(text, key):
    text_decript = []

    for linha in text:
        aux = ''
        for i in range(len(linha)):
            if linha[i] != '\n':
                aux += chr(ord(linha[i]) - key[i % len(key)])
        text_decript.append(aux)

    return text_decript


def menu():
    print('=' * 41)
    print(' CRIPTOGRAFIA DE CÉSAR DE CHAVE MÚLTIPLA')
    print('=' * 41)
    print('Ao escolher um arquivo existente, ele será automaticamente descriptografado.')
    print('Ao escolher um arquivo não existente, ele será criado criptografado.')
    print('Para sair, digite [sair].')
    path = input('\nEntre com o caminho do arquivo: ')
    if path != 'SAIR' and path != 'sair' and path != 'Sair':
        print(*open_txt(path), sep='\n')
        input('\nTecle ENTER para continuar... ')
        print()
    else:
        exit()


while True:
    menu()
