entrada = ""
quantidade_funcionarios = 0
soma_salario = 0
salario_maior = 0
salario_menor = 0

while entrada != "fim":
    nome = input("Informe o nome do funcionario: ")
    if nome == "fim":
        break
    salario = float(input("Informe o salario do funcionario: "))

    if salario > salario_maior:
        salario_maior = salario
        if quantidade_funcionarios == 0:
            salario_menor = salario
    elif salario < salario_menor:
        salario_menor = salario
    
    soma_salario = soma_salario + salario
    quantidade_funcionarios = quantidade_funcionarios + 1

media = soma_salario / quantidade_funcionarios
print("A media salarial é: ", media)
print("O salário mais alto é: ", salario_maior)
print("O salário mais baixo é: ", salario_menor)