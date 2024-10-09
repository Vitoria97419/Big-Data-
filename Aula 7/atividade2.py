temp = []
resp= "S"
while resp == "S" or resp=="s":
  temp.append(float(input("Informe a temperatura:")))
  resp=input("Deseja continuar (S/N)?")
print(f"A maior temperatura é: {max(temp)} °C.")
print(f"A menor temperatura é: {min(temp)} °C.")
print(f"A média das temperaturas é: {sum(temp)/len (temp)} °C.")