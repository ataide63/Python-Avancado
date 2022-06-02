
# Para conectar o BD, vamos precisar de uma biblioteca(Móduilo) MySQLdb  ou  pymysql

# import MySQLdb     ou      import pymysql
import pandas as pd 
from pandastable import Table, TableModel

# Mensagens
from tkinter import messagebox

class Conexao_db:

    var_server = 'localhost'
    var_user = 'root'
    var_pwd = 'mypwd'
    var_db = 'escola_curso'
    var_port = 3306
    import MySQLdb

    ## Faço a conexão no bancoô&
    global conn  # global em toda classe
    conn = MySQLdb.connect(var_server, var_user,var_pwd, var_db,var_port)
    global c   ## Defino como global em toda classe antes de usar
    c = conn.cursor()     ## defino que o retorno será um cursor(set nornmal)

    ###  Ou Defino que o retorno será um cursor tipo dicionário
    c = conn.cursor(MySQLdb.cursors.DictCursor)
    myquery = ''

    def Dados ( 
        tipo,    # 1= insert   2 = update 3 = delete
        emp_name,
        rph,
        duty,
        s3_contrib,
        phealth,
        hloan
        ):
        try:

            if tipo == 1:   # Insert
                myquery = "INSERT INTO func_escola "
                myquery = myquery + " (cpemp_name, cprph, cpduty, cps3_contrib, cpphealth, cphloan, dtAtu ) " 
                myquery = myquery + " values ( '" 
                myquery = myquery +  emp_name   + "' ,"  
                myquery = myquery +  str(rph )  + "," 
                myquery = myquery +  str(duty ) + ","  
                myquery = myquery +  str(s3_contrib)  + ","
                myquery = myquery +  str(phealth) + ","   
                myquery = myquery +  str(hloan) + ", "
                myquery = myquery + " now() ) "
     
            elif tipo == 2:   # Update
         
                #global c, conn  # indica que é uma variável é global lá na classe
                myquery = "UPDATE func_escola set " 
                myquery = myquery + "cpemp_name = '" + emp_name 
                myquery = myquery + "' , cprph = " + str(rph )
                myquery = myquery + " , cpduty = " + str(duty )
                myquery = myquery + ", cps3_contrib = " + str(s3_contrib )
                myquery = myquery + ", cpphealth = " + str(s3_contrib )
                myquery = myquery + ", cphloan = " + str(hloan )
                myquery = myquery + ",dtAtu = now() "
                myquery = myquery + " where cpcod_emp = " + str(cod_emp )

            else:  # tipo ==3 delete
                myquery = "DELETE FROM func_escola where   cpcod_emp = " + str(cod_emp)
            ##  Executa a query e commit
            c.execute(myquery)
            conn.commit()
            messagebox.showinfo("Sucesso"," Funcionário(a) atualizado com sucesso")
        except Exception as e:
            messagebox.showinfo("Erro!!", "Erro Update. Detalhes=> " + str(e))
        finally:
            return

    def Consulta(Cod_Empr=None):

        myquery = " SELECT * from func_escola "
        if (Cod_Empr==None):
            myquery = " SELECT * from func_escola "
            df = pd.read_sql_query(myquery, conn)  # Retorna um dataframe pandas (pd)
            return df
        else:
            # Retorna cursor para captura em variaveis
            c = conn.cursor()
            myquery = "  SELECT * from func_escola where cpcod_emp = " + str(Cod_Empr) 
            c.execute(myquery)
            return c.fetchall()  ## Para retornar um cursor com linhas e colunas
            #for row in result:
            #    return( (row[0], row[1], row[2], row[3], row[4], row[5] row[6])

        # print(myquery)
        # # df = c.execute(myquery)
        # df = pd.read_sql_query(myquery, conn)

        # # Só para a consulta de um copdigo específico
        # for coluna in df.axes:
        #     print( coluna["cpemp_name"])
        #     print (  df["cpemp_name"], axis=1)
        
        # # return c.fetchall()
        # return df

    def Aplicacao_Consulta(where):

        global c  # indica que é uma variável é global

        myquery = "SELECT * from func_escola where cpcod_emp = " + str(where) 
        c.execute(myquery)
        return c.fetchall()