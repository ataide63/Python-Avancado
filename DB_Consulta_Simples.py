
# import MySQLdb     ou      import pymysql



var_server = 'localhost'
var_user = 'root'
var_pwd = 'mypwd'
var_db = 'escola_curso'
var_port = 3306
import MySQLdb
    #    import pymysql

  # Comandos de leitura:
  # arq.read()  # Lê o arquivo inteiro$
  # arq.readline()  # Le uma linha do arquivo
  # arq.readlines()  # Le o arquivo e joga em uma lista

 # def __init__(self):

conn = MySQLdb.connect(var_server, var_user,var_pwd, var_db,var_port)
c = conn.cursor()   # definir como global nas funcoes que vão utilizá-la para acessar o BD

def Aplicacao_Consulta(fields, tables, where=None):

    global c  # indica que é uma variável é global

    myquery = " SELECT " + fields + " from " + tables
    if (where):
        myquery = myquery + "  where " + where
        c.execute(myquery)
        conn.close()
        return c.fetchall()


resultado = Aplicacao_Consulta("nome, cpf","alunos","id_aluno in(1,2,3)")
print(resultado) 







