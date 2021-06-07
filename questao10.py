i = 0
soma_nota = 0
media = ""

while i < 5:
  quantidade_alunos = int(input("Informe a quantidade de alunos na {}° turma: ".format(i + 1)))
  j = 0
  while j < quantidade_alunos:
    nota = float(input("Informe a nota do {}° alunos ".format(j + 1)))
    soma_nota = soma_nota + nota
    j = j + 1
  media = media + "Media turma {}° ".format(i + 1) + str(soma_nota / quantidade_alunos) + "\n"
  soma_nota = 0
  i = i + 1

print(media) 
