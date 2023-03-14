website = "http://google.com/"
slice = slice(7, -5)

# slicing example
website_name = website[slice].capitalize()
# queremos excluir http:// e as partes .com

# aqui usamos slice(start,top,step), observe que usaremos ',' ao invés de ':'
# você pode usar índice negativo, cada caractere em uma string tem um índice positivo e um negativo
# o índice negativo começa da direita para a esquerda, sendo o mais à direita -1

print(website_name)

website2 = "http://wikipedia.com/"
website2_name = website2[slice].upper()
print(website2_name)
