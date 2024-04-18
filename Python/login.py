def autenticador():
    usuario=input().split()
    usuarios_senhas = {"usuario1":"senha123","usuario2":"abc456","usuario3":"123456"}
    login=usuario[0]
    senha=usuario[1]

    key= usuarios_senhas.get(login)
    if senha == key:
        print(f"Login bem-sucedido! Bem-vindo, {login}.")
    else:
        print("Acesso negado. Credenciais inválidas.")
if __name__=="__main__":
    autenticador()    
'''
usuarios_senhas = {
    "usuario1": "senha123",
    "usuario2": "abc456",
    "usuario3": "123456"
}

usuario = input("Digite seu nome de usuário: ")
senha = input("Digite sua senha: ")
if usuario in usuarios_senhas and usuarios_senhas[usuario] == senha:
    print(f"Login bem-sucedido! Bem-vindo, {usuario}.")
else:
    print("Acesso negado. Credenciais inválidas.")

'''

