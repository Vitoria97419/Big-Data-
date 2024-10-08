nomes = []
medias = []
resp = "S"
while resp == "S" or resp=="s":
    nomes.append(input("Informe o nome do estudante:"))
    medias.append(float(input("Informe a média do estudante:")))
    resp=input("Deseja continuar(S/N)?")
print("Nome do estudante:",nomes)
print("Médias dos estudantes:",medias)
print(f"A soma das medias é:{sum(medias)} anos.")
print(f"A maior das medias é: {max(medias)}anos.")
print(f"A menor das medias é: {min(medias)}anos.")
print(f"A média da turma é: {(sum(medias)/len(medias)):.2f}.")
medias.sort(reverse = True)
print("Média na ordem Decrescente:", medias)

medias.sort()
print("Média na Ordem crescente:", medias)