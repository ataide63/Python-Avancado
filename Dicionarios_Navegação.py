dicionario1 = { }

dicionario1['item'] = 'Conteúdo'
dicionario1[0] = 'Novo Conteúdo'
print ( dicionario1)  ## Resultado: {'item': 'Conteúdo', 0: 'Novo Conteúdo'}

print ( dicionario1[0])  #  Resultado: "Novo Conteúdo" que é lista o elemento zero

print ( dicionario1['item'])   #  Resultado: "Conteúdo" que é lista o elemento item

# qtde de elementos no dicionario len()
print ( len(dicionario1))   # Resultado: 2

# Listar as chaves do dicionario
print ( dicionario1.keys())   # resultado: dict_keys(['item', 0]) que são as chaves do dicionário

dicionario2 = {"A": "Ameixa","B": "Bola",  "C": "Cachorro"}
print (dicionario2) # Resultado:  {'A': 'Ameixa', 'B': 'Bola', 'C': 'Cachorro'}
print (dicionario2["B"])  # Resultado:  Bola

print (dicionario2["B"], dicionario2["A"])  # Resultado: Bola Ameixa

# NAvegar no dicionário:
for chave in dicionario2:
	print ( chave, dicionario2[chave])
	#Resultado:
	# A Ameixa
    # B Bola
    # C Cachorro


# Bavegsndo entre os ítens  do dicionário:
for item in dicionario2.items():
	print ( item)
	# Resultado:
	# ('A', 'Ameixa')
    # ('B', 'Bola')
    # ('C', 'Cachorro')


# navegando entre os valores  do dicionário:
for valor in dicionario2.values():
	print ( valor)
	# Resultado:
	# Ameixa
    # Bola
    # Cachorro


# navegando entre as chaves  do dicionário:
for chave in dicionario2.keys():
	print ( chave)
	# Resultado:
	# A
    # B
    # C

