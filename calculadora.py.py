# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zxtGgqUYBJO7b2TRS9CAe8UzfWdqQ3Fh
"""

def calcular():
    while True:
        # Receber os dois números do usuário
        num1 = input("Digite o primeiro número: ")
        num2 = input("Digite o segundo número: ")

        # Converter para número inteiro ou ponto flutuante
        try:
            num1 = float(num1) if '.' in num1 else int(num1)
            num2 = float(num2) if '.' in num2 else int(num2)
        except ValueError:
            print("Por favor, insira números válidos.")
            continue

        # Exibir opções de operações
        print("\nEscolha a operação:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        # Receber a escolha do usuário
        operacao = input("\nDigite o número da operação desejada: ")

        # Executar a operação escolhida
        if operacao == '1':
            print(f"\nResultado: {num1} + {num2} = {num1 + num2}\n")
        elif operacao == '2':
            print(f"\nResultado: {num1} - {num2} = {num1 - num2}\n")
        elif operacao == '3':
            print(f"\nResultado: {num1} * {num2} = {num1 * num2}\n")
        elif operacao == '4':
            if num2 != 0:
                print(f"\nResultado: {num1} / {num2} = {num1 / num2}\n")
            else:
                print("\nErro: Divisão por zero não é permitida.\n")
        elif operacao == '5':
            print("\nSaindo da calculadora. Até mais!")
            break
        else:
            print("\nOpção inválida. Tente novamente.\n")

# Executar a função da calculadora
calcular()

cd /caminho/para/seu/arquivo
from google.colab import userdata
userdata.get('secretName')