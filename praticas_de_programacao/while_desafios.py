import random
import time

def contar_pares_impares():
    """
    Conta quantos números pares e ímpares o usuário digita até inserir o número 0.

    A função continua pedindo números até que o usuário digite o valor 0. Ao final, exibe a quantidade de números pares e ímpares inseridos. Durante a execução, o programa faz uma pausa de 2 segundos entre cada interação com o usuário para tornar o jogo mais interessante.

    Returns:
        None
    """
    par = 0
    impar = 0
    n = None
    while n != 0:
        n = int(input("Digite um número: "))
        time.sleep(2)
        if n != 0:
            if n % 2 == 0:
                par += 1
                print("Número par!")
            else:
                impar += 1
                print("Número ímpar!")
            time.sleep(2)
    print(f"Você digitou {par} números pares e {impar} números ímpares!")
    time.sleep(2)

sexo = str(input("Digite seu sexo: [M/F] ")).strip()
while sexo not in "MmFf":
    sexo = str(input("Dado inválido. Por favor, digite seu sexo: [M/F] ")).strip()
print(f"Sexo {sexo} registrado com sucesso!")
time.sleep(2)

def jogo_adivinha():
    """
    Jogo de adivinhação onde o computador "pensa" em um número aleatório entre 0 e 10,
    e o usuário tenta adivinhar qual é o número.

    Durante o jogo, o computador fornece feedback sobre o número errado e solicita novas tentativas até o acerto.
    Uma pausa de 2 segundos é feita entre cada interação para criar suspense.

    Returns:
        None
    """
    print("""Bem-vindo ao nosso jogo de adivinhação!
Aqui o computador irá "pensar" em um número de
0 a 10 e você precisa adivinhar qual é!""")
    time.sleep(2)
    p = str(input("Quer jogar? [S/N]: ")).upper().strip()
    time.sleep(2)
    if p == "S":    
        while True:
            erro = 1
            r = int(input("Digite um número: "))
            time.sleep(2)
            n = random.randrange(0, 11)
            while r != n:
                r = int(input("Número errado, tente novamente: "))
                time.sleep(2)
                if r != n:
                    erro += 1
            print("Parabéns, você acertou!")
            time.sleep(2)
            print(f"Você tentou {erro} vezes até acertar!")
            time.sleep(2)
            pergunta = str(input("Você quer jogar de novo? [S/N]: ")).upper().strip()
            if pergunta == "N":
                print("Obrigado por jogar!")
                time.sleep(2)
                break
    else: 
        print("Okay, até a próxima!")
        time.sleep(2)

def operador():
    """
    Função que permite ao usuário realizar várias operações matemáticas com dois números inteiros.
    As opções incluem somar, multiplicar e comparar os números, além de permitir a escolha de novos números ou sair do programa.

    Durante a interação, o programa faz pausas de 2 segundos entre as respostas para tornar o processo mais dinâmico.

    Returns:
        None
    """
    while True:
        print("\n" + "="*30)
        valor1 = int(input("Digite um número inteiro: "))
        valor2 = int(input("Digite outro número inteiro: "))
        time.sleep(2)
        
        while True:
            print("""\nOperações disponíveis:
[1] = somar
[2] = multiplicar
[3] = maior
[4] = novos números
[5] = sair""")
            time.sleep(2)
            
            escolha = input("Escolha uma operação (1-5): ")
            
            if escolha == '1':
                resultado = valor1 + valor2
                print(f"\nResultado: {valor1} + {valor2} = {resultado}")
            elif escolha == '2':
                resultado = valor1 * valor2
                print(f"\nResultado: {valor1} × {valor2} = {resultado}")
            elif escolha == '3':
                resultado = max(valor1, valor2)
                print(f"\nO maior entre {valor1} e {valor2} é: {resultado}")
            elif escolha == '4':
                print("\nVocê escolheu digitar novos números.")
                time.sleep(2)
                break  
            elif escolha == '5':
                print("\nEncerrando o programa...")
                time.sleep(2)
                return 
            else:
                print("\nOpção inválida! Digite um número entre 1 e 5.")
            continuar = input("\nDeseja fazer outra operação com estes números? (S/N): ").upper()
            time.sleep(2)
            if continuar != 'S':
                break
