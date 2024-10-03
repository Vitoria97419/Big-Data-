nome = input ("Informe o nome do estudante: ")
n1 = float (input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota: "))
media= (n1 + n2) / 2
print(media)
if media >=70:
    print(f"{nome}, você está Aprovado, pois sua média foi {media:.2f}")
elif media >=30 and media<70:
    print (f"{nome}, você está em Recuperação, pois sua média foi {media:.2f}")
else :
    print (f"{nome}, você está Reprovado, pois sua média foi {media:.2f}")