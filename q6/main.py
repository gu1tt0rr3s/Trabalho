# Q6 - Conversor de Moedas
# Crie a função que converte reais para dólares e dólares para reais (arquivo conversor.py)
# real_para_dolar e dolar_para_real. Caso o usuário não passe o tipo (real_para_dolar ou dolar_para_real) o default deve ser real_para_dolar <- padrão
from conversor import dolar, real

while True:
    escolha = int(input("MENU\n1. Real para Dólar\n2. Dólar para Real\n3. Sair\nEscolha uma opção: "))
    if escolha == 3:
        print("Até mais!")
        break
    valor = float(input("Digite o valor: "))
    cotacao = float(input("Digite a cotação do dólar: "))

    if escolha == 1:
        real_para_dolar = dolar(valor, cotacao)
        print(f"\n{valor:.2f} reais equivalem a {real_para_dolar:.2f} dólares.")
        break
    elif escolha == 2:
        dolar_para_real = real(valor, cotacao)
        print(f"{valor:.2f} dólares equivalem a {dolar_para_real:.2f} reais.")
        break
    else:
        real_para_dolar = dolar(valor, cotacao)
        print(f"\n{valor:.2f} reais equivalem a {real_para_dolar:.2f} dólares.")
        break