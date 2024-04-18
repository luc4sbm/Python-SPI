usuarios_senhas = {
    "usuario1": "senha123",
    "usuario2": "abc456",
    "usuario3": "123456"
}

login = input().split


if login in usuarios_senhas and usuarios_senhas[login] == login:
    print(f"Login bem-sucedido! Bem-vindo, {login}.")
else:
    print("Acesso negado. Credenciais inválidas.")