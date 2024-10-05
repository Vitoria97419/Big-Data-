import datetime
data_atual = datetime.date.today()
ano_atual= data_atual.year
nome= str(input('Qual é o seu nome?'))
ano_nasc = int (input ("Informe o Ano de Nascimento: "))
idade = ano_atual - ano_nasc
print ("Sr(a)",nome, "a sua idade é: ",idade," anos.") 