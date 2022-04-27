

a = "Diego"
b = "Mariano" 
concatenar = a + " " + b
print (concatenar)

print (concatenar[0:4])

print (concatenar.lower())
print (concatenar.upper())

var1 = " texto com caracter especial\n"
print(var1)  # mostra o texto sem alteração
print(var1.strip())   # mostra o texto removendo carcteres especiais e espaços.

# Convertendo uma string em lista:
var1 = "O rato roeu a roupa do rei de Roma"
print ("tamanho da variavel: " + str(len(var1)))
var1 = var1.split()  # cada palavra se torna elemento da lista
print ("tamanho da variavel: %s" %  len(var1))


### Quebra os elementos a partir de um determinado caracter:
var2 = "O rato roeu a roupa do rei de Roma"
var2 = var2.split("r")  # cada palavra com "r' se torna elemento da lista  sem a letra 'r'
print(var2)

## Pesquisando dentro de uma string
var1 = "O rato roeu a roupa do rei de Roma"
pesquisa = var1.find("roupa")  # retorna a posição da palavra dentro da string
print(pesquisa)


## Substituindo parte da  string
var1 = "O rato roeu a roupa do rei de Roma"
pesquisa = var1.replace("roupa", "sandalia")  # substitui "roupa" por "sandalia" 
print(pesquisa)


## pegando parte  uma string
var1 = "O rato roeu a roupa do rei de Roma"
pesquisa = var1[3:12] 
print(pesquisa)





