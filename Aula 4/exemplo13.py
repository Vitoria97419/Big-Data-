try:
   n1 = int(input("Informe o primeiro valor: "))
   n2= int (input("Informe o segundo valor: "))

except ValueError:
       print ("Verifique a entrda de dados")

else:
    try:
        result= n1/n2
    except ZeroDivisionError:
        print ("Não é possível dividir por zero")
    else:
         print (result)