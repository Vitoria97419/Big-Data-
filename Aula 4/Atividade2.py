import datetime 
data_atual = datetime.date.today()
ano_atual= data_atual.year

try:
    nome = input ("Informe seu nome:")
    ano_nasc = int (input("Informe seu ano nascimento:"))
    ano_emp = int (input("Informe seu ano de entrada na empresa:"))
except ValueError:
    print("Verifique os dados informados")

idade= ano_nasc - ano_atual
contrib= ano_emp-ano_atual
if idade >65:
    print("Está qualificado a aposentadoria.")
elif contrib >30:
    print("Está qualificado a aposentadoria")
elif idade >60  and contrib >25:
    print("Está qualificado a aposentadoria ")
else:
    print("Não está qualificado")
     

