usu=["Mia","Dia","Pria","Nia","Kya"]
senha=["123","456","789","101112","131415"]
usu=input("Informe o nome de acesso:")
for i in range(len(usu)):
    if usu[i] == usu:
        resp="Usuario Encontrado"
        break
    else:
        resp="Usuario não encontrado"
    print(resp)

