recebe= int (input("Quanto você recebe por hora?"))
horas = int (input("Quantas horas vc trabalha mensalmente?"))
bruto = recebe *horas
inss= bruto * 0.08
sind = bruto *0.05
irrf=(bruto-inss-sind) * 0.11
liquido=bruto -(inss+irrf+sind)
print("Salário Bruto = (bruto)")
print("Desconto INSS=", (inss))
print("Desconto Sindicato=",(sind))
print(f"Desconto IRRF ={(irrf):.2f} ")
print(f"Salário Líquido={(bruto-inss-sind-irrf):.2f}")