usuarios=["Mia","Dia","Pria","Nia","Kya"]
senhas=["123","456","789","101112","131415"]
usuario=input("Informe o nome de acesso:")
for i in range(len(usuarios)):
    if usuarios[i] == usuario:
       senha = input("Informe a senha de acesso:")
       if senhas [i] ==senha:
          resp="Acesso Liberado"
       else:
          resp="Senha não confere"
       break

    else:
        resp="Usuario não encontrado"
        print(resp)

