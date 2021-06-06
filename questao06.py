primeiro_termo = 3

i = 0
sequencia = 2
termo = 0

print(primeiro_termo)

while i < 14:

    if i == 0:
        termo = primeiro_termo + 4 / (sequencia * (sequencia + 1) * (sequencia + 2))
        sequencia = sequencia + 2
        print(termo)
        i = i + 1

    termo = termo - 4 / (sequencia * (sequencia + 1) * (sequencia + 2))
    sequencia = sequencia + 2    
    print(termo)
    i = i + 1

    