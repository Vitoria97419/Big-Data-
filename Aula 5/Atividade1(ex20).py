#como fazer um programa com repetição

soma = 0
media =0
for i in range (5):
    nome = input ("Informe o nome: ")
    idade = int (input("Informe a idade: "))
    soma= soma+idade
    media =soma /(i+1)
    print(f"A soma é {soma}")
    print(f"A média é {media:.0f}")