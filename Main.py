

from tkinter import *
import pandas as pd 
from pandastable import Table, TableModel

# Mensagens
from tkinter import messagebox

# Cnexão ao SQL 
import SQL_Conexao_db as Con_Sql

#calculo
import calsal

#VAlidar os dados de entrada numéricos
import Validacao_Dados 

global ws, mainframe, mainframe


ws = Tk()
ws.geometry('500x350+500+200')
ws.title("Dados de Funcionarios")
f = ('sans-serif 12')

class MyApp():
    ### docstring for Monta_Tela
    par_ws = None
    

    def __init__(self, par_ws ):  # objeto protegido inicia com
        self.par_ws = par_ws

            
    # functions

    def Calcular(emp_name, rph , duty, s3_contrib, phealth, hloan):
        ## Se tiver erro nos dados numéricos
        Tratamento = Validacao_Dados.Trata_Dados
        if not(Tratamento.valida_entrada( emp_name, rph , duty, s3_contrib, phealth, hloan)): 
            return

        ename = emp_name.get()
        r =  str(rph.get()).replace(",", ".")
        d = str(duty.get()).replace(",", ".")
        contri = str(s3_contrib.get()).replace(",", ".")
        ph = str(phealth.get()).replace(",", ".")
        hl = str(hloan.get()).replace(",", ".")

        r = float(r)
        d = float(d) 
        contri = float(contri)
        ph = float(ph)
        hl = float(hl)

        gross_sal = 0.00
        tax = 0.00
        total_deduction = 0.00
        net_sal = 0.00
        
        # calling function
        calsal.payslip(ename, d, r, gross_sal, contri, ph, hl, tax, total_deduction, net_sal, ws, f)

    def Gravar(Cod_Alteracao, emp_name, rph , duty, s3_contrib, phealth, hloan):
        ## Se tiver erro nos dados numéricos
        ## Se tiver erro nos dados numéricos
        Tratamento = Validacao_Dados.Trata_Dados
        if not(Tratamento.valida_entrada( emp_name, rph , duty, s3_contrib, phealth, hloan)): 
            return

        ename = emp_name.get()
        r = rph.get()
        d = duty.get()
        contri = s3_contrib.get()
        ph = phealth.get()
        hl = hloan.get()
        Cod_Alt = str(Cod_Alteracao.get())

        if len(Cod_Alt) > 0:
            Tipo=2
        else:
            Tipo=1
            Cod_Alteracao.delete(0, 'end')

        Mysql = Con_Sql.Conexao_db
        Mysql.Dados(Tipo, Cod_Alt, ename, r , d, contri, ph, hl)


    def clearbtn( Cod_Alteracao, emp_name, rph , duty, s3_contrib, phealth, hloan):
        emp_name.delete(0, 'end')
        rph.delete(0, 'end')
        duty.delete(0, 'end')
        s3_contrib.delete(0, 'end')
        phealth.delete(0, 'end')
        hloan.delete(0, 'end')
        Cod_Alteracao.delete(0, 'end')


    def Consulta(Cod_Alteracao, emp_name, rph , duty, s3_contrib, phealth, hloan):
        #Carrega a base de dados
        Cod_Alt = Cod_Alteracao.get()
        Mysql = Con_Sql.Conexao_db 
        if Cod_Alt.isdigit():  # Se consulta de um funcionário é aqui
            Cod_Alt = int(Cod_Alt)
            emp_name.delete(0, 'end')
            rph.delete(0, 'end')
            duty.delete(0, 'end')
            s3_contrib.delete(0, 'end')
            phealth.delete(0, 'end')
            hloan.delete(0, 'end')
            # Consulta o MySQL Para o funcionanrio selecionado
            result = Mysql.Consulta(Cod_Alt)
 

            for row in result:
                # Default values in the entry widget
                Cod_Alteracao.delete(0, 'end')
                Cod_Alteracao.insert('0', row[0])
                emp_name.insert('0', row[1])
                rph.insert('0', row[2])
                duty.insert('0',row[3])
                s3_contrib.insert('0',row[4])
                phealth.insert('0', row[5])
                hloan.insert('0', row[6])
            return

        else:   # Se consulta geral  é aqui
            Cod_Alteracao.delete(0, 'end')
            df = Mysql.Consulta(None)

        # Configura e Mostra o DataFrame
        ws_Cons =  Toplevel(ws)
        ws_Cons.title("Consulta Dados de Funcionarios")
        ws_Cons.geometry ('800x450+350+200')       
        fr = Frame(ws_Cons)
        mainfr = Frame(ws_Cons, padx=5, pady=5,  bg="lightsteelblue")
        mainfr.pack(expand=True)
        fr.pack(fill=BOTH,expand=1)
        Table(fr, dataframe=df, showtoolbar=True, showstatusbar=True).show()
        ws_Cons.mainloop()


    def Excluir(Cod_Alteracao):
        var_alt = str(Cod_Alteracao.get())
        if  len(var_alt) > 0:
            if (messagebox.askyesno("Confirma a exclusãp do Funcionário?", "Confirma?"))==1:
                Mysql = Con_Sql.Conexao_db
                Mysql.Dados(3,var_alt,None, None, None, None, None, None)
                return
        else:
            messagebox.showinfo("Dados Incorretos", "Informe um código de funcionário para excluir, ou consulte")


    def Monta_EMPLOYEE_PAYSLIP(): 
        Label(
            ws,
            text=" Controle de Colaboradores e Folha",
            font=('sans-serif, 14'),
            relief=SOLID,
            padx=10,
            pady=5
        ).pack()

        # frame widget
        mainframe = Frame(ws, padx=0, pady=5,  bg="lightsteelblue")
        mainframe.configure(  width=300, height = 500, bd = 5)
        mainframe.pack(expand=True)
    

        # label widget
        Label(
            mainframe,
            text='Funcionário:',
            font=f, bg="lightsteelblue"
            ).grid(row=0, column=0, sticky='e')

        Label(
            mainframe,
            text=' $ por Hora',
            font=f,  bg="lightsteelblue"
            ).grid(row=1, column=0, sticky='e')

        Label(
            mainframe,
            text=' Impostos(Horas)',
            font=f ,  bg="lightsteelblue"
            ).grid(row=2, column=0, sticky='e')

        Label(
            mainframe,
            text='INSS: ',
            font=f ,  bg="lightsteelblue"
            ).grid(row=3, column=0, sticky='e')

        Label(
            mainframe,
            text='Plano dd Saúde: ',
            font=f ,  bg="lightsteelblue"
            ).grid(row=4, column=0, sticky='e')

        Label(
            mainframe,
            text=' Moradia: ',
            font=f ,  bg="lightsteelblue"
            ).grid(row=5, column=0, sticky='e')

        Label( mainframe,
            text='Consultar Código:',
            font=f ,  bg="lightsteelblue"
            ).grid(row=6, column=0, sticky='e')


        # Entry widgets
        emp_name = Entry(mainframe, font=f)
        rph = Entry(mainframe, font=f)
        duty = Entry(mainframe, font=f)
        s3_contrib = Entry(mainframe, font=f)
        phealth = Entry(mainframe, font=f)
        hloan = Entry(mainframe, font=f)
        Cod_Alteracao = Entry(mainframe, font=f)

        # geometry method - Grid
        emp_name.grid(row=0, column=1, padx=5, sticky='w')
        rph.grid(row=1, column=1, padx=5, sticky='w')
        duty.grid(row=2, column=1, padx=5, sticky='w')
        s3_contrib.grid(row=3, column=1, padx=5, sticky='w')
        phealth.grid(row=4, column=1, padx=5, sticky='w')
        hloan.grid(row=5, column=1, padx=5, sticky='w')
        Cod_Alteracao.grid(row=6, column=1, padx=5, sticky='w')

        # # default values in the entry widget
        # emp_name.insert('0', 'Noel B. Atazar')
        # rph.insert('0', 150)
        # duty.insert('0', 9)
        # s3_contrib.insert('0', 200)
        # phealth.insert('0', 150)
        # hloan.insert('0', 100)
        Cod_Alteracao.insert('0', '')

        # frame for buttons
        frame = Frame(mainframe,  bg="blue")  #  bg="lightsteelblue"
        frame.grid(row=7, columnspan=3, pady=(30, 0))

    #limpar = Monta_Tela.clearbtn()
        Button(
            frame,
            text='Novo',
            width=5,
            font=f,
            bg='#91BF2C', 
            command= lambda:MyApp.clearbtn(Cod_Alteracao, emp_name, rph , duty, s3_contrib, phealth, hloan) 
        ).pack(side=LEFT, expand=True, padx=(0, 5))

        Button(
            frame,
            text='Calcular',
            width=8,
            font=f,
            bg='#E6D92A',
            command=lambda:MyApp.Calcular(emp_name, rph , duty, s3_contrib, phealth, hloan ) 
        ).pack(side=LEFT, expand=True, padx=(0, 5))

        # 
        Button(
            frame,
            text='Gravar',
            width=5,
            font=f,
            bg='#E6D92A',
            command= lambda:MyApp.Gravar( Cod_Alteracao, emp_name, rph , duty, s3_contrib, phealth, hloan) 
        ).pack(side=LEFT, expand=True, padx=(0, 5))

        # = t
        Button(
            frame,
            text='Consultar',
            width=8,
            font=f,
            bg='#E6D92A',
            command= lambda:MyApp.Consulta(Cod_Alteracao,emp_name, rph , duty, s3_contrib, phealth, hloan)
        ).pack(side=LEFT, expand=True, padx=(0, 5))

    

        #limpar = Monta_Tela.clearbtn()
        Button(
            frame,
            text='Excluir',
            width=5,
            font=f,
            bg='#E6D92A',
            command= lambda:MyApp.Excluir(Cod_Alteracao) 
        ).pack(side=LEFT, expand=True, padx=(0, 5))

        Button(
            frame,
            text='Sair',
            width=4, 
            font=f,
            bg='#FF614F',
            command=lambda:ws.destroy()
        ).pack(side=LEFT, expand=True, padx=(0, 5))

        # infinite loop
        emp_name.focus_set()
        ws.mainloop()
        return


x=MyApp
x.Monta_EMPLOYEE_PAYSLIP()