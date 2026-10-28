produtos = {}  


def cadastrar():
    nome = input("Nome do produto: ").strip()
    if nome == "":
        print("Nome nao pode ficar vazio.")
        return
    try:
        preco = float(input("Preco do produto: ").replace(",", "."))
    except ValueError:
        print("Preco invalido. Digite so numeros.")
        return
    if preco < 0:
        print("Preco nao pode ser negativo.")
        return
    produtos[nome] = preco
    print("Produto cadastrado!")

#Server para listar os produtos cadastrados
def listar():
    if not produtos:
        print("Nenhum produto cadastrado ainda.")
        return
    print("\n--- Lista de produtos ---")
    for nome, preco in produtos.items():
        print(f"{nome}: R$ {preco:.2f}")


while True:
    print("\n1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Sair")
    opcao = input("Escolha: ")
    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        print("Saindo...")
        break
    else:
        print("Opcao invalida.")
