


from tkinter import *

# function
def payslip(ename, d, r, gross_sal, contri, ph, hl, tax, total_deduction, net_sal, ws, f):
    cf = ('sans-serif 12 bold')
    win = Toplevel(ws)
    win.geometry ('500x450+500+200')      

    r = float(r)
    d = float(d) 
    contri = float(contri)
    ph = float(ph)
    hl = float(hl)

    gross_sal = r * d
    tax = gross_sal * 0.1
    total_deduction = contri + ph + hl + tax
    net_sal = gross_sal - total_deduction

    Label( 
        win, 
        text='Informações do Colaborador', 
        font='sans-serif 14', 
        relief=SOLID, padx=5, 
        pady=10
        ).place(x=110 , y=10)

    Label(
        win, 
        text='Colaborador: ', 
        font=cf
        ).place(x=10, y=70)

    Label(
        win, 
        text=f'{ename}', 
        font=f
        ).place(x=65, y=70)

    Label(
        win, 
        text='Horas Renderizadas: ', 
        font=cf
        ).place(x=250, y=70)

    Label(
        win, 
        text=f'{d}', 
        font=f
        ).place(x=390, y=70)

    Label(
        win, 
        text='Valor Hora: ', 
        font=cf
        ).place(x=10, y=110)

    Label(
        win, 
        text=f'{r}', 
        font=f
        ).place(x=125, y=110)

    Label(
        win, 
        text='Salário Bruto: ',
        font=cf
        ).place(x=250, y=110)

    Label(
        win, 
        text=f'{gross_sal}', 
        font=f
        ).place(x=390, y=110)


    Label(
        win, 
        text='Deduções',
        font='sans-serif 14', relief=SOLID, 
        pady=5, padx=10
        ).place(x=170, y=180)


    Label(
        win, 
        text='INSS: ', 
        font=cf
        ).place(x=10, y=240)

    Label(
        win, 
        text=f'{contri}', 
        font=f
        ).place(x=65, y=240)

    Label(
        win, 
        text='Plano de Saúde: ', 
        font=cf
        ).place(x=250, y=240)

    Label(
        win, 
        text=f'{ph}', 
        font=f
        ).place(x=390, y=240)

    Label(
        win, 
        text='Empr.Consignado:', 
        font=cf
        ).place(x=10, y=280)
    
    Label(
        win,
        text=f'{hl}', 
        font=f
        ).place(x=105, y=280)

    Label(
        win, 
        text='Impostos: ', 
        font=cf
        ).place(x=250, y=280)

    Label(
        win, 
        text=f'{tax}', 
        font=f
        ).place(x=390, y=280)

    Label(
        win, 
        text='Deduções Totais: ', 
        font=cf
        ).place(x=10, y=320)

    Label(
        win, 
        text=f'{total_deduction}',
        font=f
        ).place(x=150, y=320)

    Label(
        win, 
        text='Líquido:', 
        font=cf
        ).place(x=250, y=320)

    Label(
        win, 
        text=f'{net_sal}', 
        font=f
        ).place(x=390, y=320)

    Button(
        win, 
        text='Sair', 
        padx=10, 
        pady=5, 
        font=f, 
        bg='#FF614F', 
        command=lambda:win.destroy()
        ).place(x=220, y=390)
