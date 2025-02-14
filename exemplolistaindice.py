produtos= ["tv","cell","mouse","teclado","tablet","geladeira","forno"]
print(produtos[1])
estoque  = [100,150,100,120,70,180,80]
print("as vendas de {}" "foram de {}".format(produtos[1],estoque[1]))

i=produtos.index("mouse")
print("o valor de i e " + str(i))
print("o prduto da posicao i e" + str(produtos[i]))

produto = input ("insira o nome do produtoe letra minuscula ")
i = produtos.index(produto)
print(i)
if produto in produtos:
    i = produtos.index(produto)
    qtde_estoque = estoque[i]
    print ("temos {} unidades de {} no estoque ".format(qtde_estoque,produto))
else:
    print("erro!nao temos este produto no estoque".format(produto))
    
