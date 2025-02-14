produtos= ["tv","cell","mouse","teclado","tablet","geladeira","forno"]
item_usuario = input("qual item deseja remover?")
try:
    produtos.remove(item_usuario)
    print(produtos)
except:
    print("o produto {} nao existe na lista".format(item_usuario))