nome_01="Alessandro,Maria,Pedro,Duda,Eduardo"
nomes_02=["Alessandro","Maria","Pedro", "Duda", "Eduardo","Manoel"]
print(nome_01)
print(nomes_02)
print(nomes_02[0])
print(len(nomes_02))
n=1
for i in range(len(nomes_02)):
    print(f"{n}-{nomes_02[i]}")
    n+=1

