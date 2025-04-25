import random

def jogo_adivinha():
    print("""Bem vindo ao nosso jogo de adivinha!
Aqui o computador irá "pensar" em um número de
0 a 10 e você precisa adivinhar qual é!""")
    p = str(input("Quer jogar? [S/N]: ")).upper().strip()
    if p == "S":    
        while True:
            erro = 1
            r = int(input("Digite um número: "))
            n = random.randrange(0,11)
            while r != n:
                r = int(input("Número errado, tente novamente: "))
                if r != n:
                    erro += 1
            print("Parabéns, você acertou!")
            print(f"Você tentou {erro} vezes até acertar!")
            pergunta = str(input("Você quer jogar de novo? [S/N]: ")).upper().strip()
            if pergunta == "N":
                print("Obrigado por jogar!")
                break
    else: 
        print("Okay, até a próxima!")
#jogo_adivinha()
def operador():
    while True:
        print("\n" + "="*30)
        valor1 = int(input("Digite um número inteiro: "))
        valor2 = int(input("Digite outro número inteiro: "))
        
        while True:
            print("""\nOperações disponíveis:
[1] = somar
[2] = multiplicar
[3] = maior
[4] = novos números
[5] = sair""")
            
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
                break  
            elif escolha == '5':
                print("\nEncerrando o programa...")
                return 
            else:
                print("\nOpção inválida! Digite um número entre 1 e 5.")
            continuar = input("\nDeseja fazer outra operação com estes números? (S/N): ").upper()
            if continuar != 'S':
                break
operador()
