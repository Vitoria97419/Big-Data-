#Programa IMC
h = float (input("Digite a sua altura :"))
s= input ("Informe M - para Masculimo e F -para Feminino")
if s== "M" or s== "m":
    m = (72.7 * h) -58
    print(f"O seu peso ideal é {m:.2f}")
elif s =="F" or s=="f":
     f = (62.1 * h) -44.7
     print(f"O seu peso ideal é {f:.2f}")

else:
      print ("Verifique o sexo informado")


