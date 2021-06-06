decimal = 0
expoente = 0

numero = int(input("Informe o numero binario: "))

while numero != 0:
    digito = numero % 10
    decimal = decimal + digito * 2 ** expoente
    numero = numero // 10
    expoente = expoente + 1

print(decimal)