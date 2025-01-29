# Primeira situação: calcular o dígito das dezenas quando dividido por 70000
numeroInteiro = int(input("Digite um número inteiro: "))

# Dividindo o número por 70000 e obtendo o dígito das dezenas
totalDezenas = (numeroInteiro // 70000) % 10
print(f"O dígito das dezenas é {totalDezenas}")

# Segunda situação: calcular o dígito das dezenas de um número comum
numeroInteiro = int(input("Digite um número inteiro: "))

# Obtendo o dígito das dezenas
totalDezenas = (numeroInteiro // 10) % 10
print(f"O dígito das dezenas é {totalDezenas}")