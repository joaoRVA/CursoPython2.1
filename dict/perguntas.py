# Sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta 1': 'Quanto é 2 + 2?',
        'Opções': ['22', '2', '4', '0'],
        'Resposta': '4',
    },
    {
        'Pergunta 2': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta 3': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]


question1 = list(perguntas[0])
opcoes1 = perguntas[0]['Opções']
resposta = perguntas[0]['Resposta']
x = 0
print(question1[0], ":", perguntas[0]['Pergunta 1'], "\n")

for i in opcoes1:
    print(f"{x}) {i}")
    x = x + 1

res = str(input('Digite a opção correta: '))
print(res)

if res == '2':
    print("\nParabéns!! Você acertou 👍\n")
else:
    print("\nVocê errou... ❌")
    print("A resposta era: ",resposta,"\n")

    

question2 = list(perguntas[1])
opcoes2 = perguntas[1]['Opções']
resposta2 = perguntas[1]['Resposta']
x = 0
print(question2[0], ":", perguntas[1]['Pergunta 2'], "\n")

for i in opcoes2:
    print(f"{x}) {i}")
    x = x + 1

res = str(input('Digite a opção correta: '))
print(res)

if res == '0':
    print("\nParabéns!! Você acertou 👍\n")
else:
    print("\nVocê errou... ❌")
    print("A resposta era: ",resposta2,"\n")



question3 = list(perguntas[2])
opcoes3 = perguntas[2]['Opções']
resposta3 = perguntas[2]['Resposta']
x = 0
print(question2[0], ":", perguntas[2]['Pergunta 3'], "\n")

for i in opcoes3:
    print(f"{x}) {i}")
    x = x + 1

res = str(input('Digite a opção correta: '))
print(res)

if res == '1':
    print("\nParabéns!! Você acertou 👍\n")
else:
    print("\nVocê errou... ❌")
    print("A resposta era: ",resposta3,"\n")

