import os
 
def limpar_console():
    os.system('cls')
 
def modificador_texto(texto):
 
    def metodo_dinamico(metodo):
        return print('Aqui está seu texto convertido: \n', getattr(texto, metodo)(), sep='')
 
    if metodo_input == '1':
        metodo = 'upper'
        metodo_dinamico(metodo)
    elif metodo_input == '2':
        metodo = 'lower'
        metodo_dinamico(metodo)
    elif metodo_input == '3':
        metodo = 'capitalize'
        metodo_dinamico(metodo)
    elif metodo_input == '4':
        return print(f'Aqui está seu texto convertido: \n',texto.strip().replace(' ', '-'), sep='')
    elif metodo_input == '5':
        return print('Aqui está seu texto convertido: \n',texto.strip().replace(' ', '_'), sep='')
 
def verificador_input(input, lista):
    if input not in lista or input == '' or input.isspace():
        try:
            int(input)
            limpar_console()
            print('Você digitou um número inválido, por favor tente novamente..\n')
        except:
            limpar_console()
            print('Por favor, digite apenas números!\n')
        
        return 'Reiniciar'
 
# Listas verificadoras
lista_metodos = '1 2 3 4 5'
lista_encerrar = '1 9'
 
while True:
    metodo_input = input('Digite o numero referente ao método que você deseja utilizar:\n'
    '1) MAIÚSCULA\n'
    '2) minúscula\n'
    '3) Capitalizar\n'
    '4) dash-case\n'
    '5) snake_case\n'
    '9) Fechar programa\n'
    )
 
    if metodo_input == '9':
        limpar_console()
        print('Certo, até breve!')
        break
 
    if verificador_input(metodo_input, lista_metodos) == 'Reiniciar':
        continue
 
    texto = input('\nDigite o texto que você deseja tranformar: ')
    
    limpar_console()
 
    modificador_texto(texto)
 
    print('')
 
    encerrar = False
 
    while True:
        deseja_encerrar = input('Digite 1 para continuar ou 9 para encerrar o programa: ')
        if deseja_encerrar == '9':
            encerrar = True
            break
 
        if verificador_input(deseja_encerrar, lista_encerrar) == 'Reiniciar':
            continue
 
        limpar_console()
        break
 
    if encerrar == True:
        limpar_console()
        print('Certo, até breve!')
        break