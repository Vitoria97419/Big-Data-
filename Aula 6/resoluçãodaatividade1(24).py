nomes = []
medias = []
resp = "S"
while resp == "S" or resp=="s":
    nomes.append(input("Informe o nome do estudante:"))
    medias.append(float(input("Informe a média do estudante:")))
    resp=input("Deseja continuar(S/N)?")
for i in range (len(medias)):
          print(i,"- ",nomes[i], "-", medias[i])
maior_media=max(medias)
pos=medias.index(maior_media)
print(f"{nomes[pos]},você possui a maior media")
print(f"A média da turma é: {(sum(medias)/len(medias)):.1f}.")
print(f"A maior das medias é: {max(medias)}")
print(f"A menor das medias é: {min(medias)}")
print(f"Amplitude da média da turma é {max(medias)-min(medias)}")
medias.sort()
print(medias)