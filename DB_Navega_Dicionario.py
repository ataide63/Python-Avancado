
import SQL_Conexao_db as conn_db
         
Myclass = conn_db.Conexao_db
result = Myclass.Aplicacao_Consulta("nome, cpf","alunos")


"""   ###   Com o retorno em dicionário "result" posso navegar no set   ###  """

print(result[4])    ## retono o 5ºregistro inteiro
print(result[0]["cpf"])    ## retono só o campo cpf do 1ºregistro

for i in result:  ## Cada elemento do dicionario
    print (i["nome"],  i["cpf"] )
    if (i["cpf"] == "07347812111"):
        print ("é igual")
    else:
        print("não é igual")

print("Fim da navegação no dicionario")
 ###   Fim do teste da chamada da Aplicacao_Consulta

