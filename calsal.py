


from tkinter import *

# function
def payslip(ename, d, r, gross_sal, contri, ph, hl, tax, total_deduction, net_sal, ws, f):
    cf = ('sans-serif 12 bold')
    win = Toplevel(ws)
    win.geometry ('500x450+500+200')      


    Label( 
        win, 
        text='EMPLOYEES INFORMATION', 
        font='sans-serif 14', 
        relief=SOLID, padx=5, 
        pady=10
        ).place(x=110 , y=10)

    Label(
        win, 
        text='Name: ', 
        font=cf
        ).place(x=10, y=70)

    Label(
        win, 
        text=f'{ename}', 
        font=f
        ).place(x=65, y=70)

    Label(
        win, 
        text='Rendered Hours: ', 
        font=cf
        ).place(x=250, y=70)

    Label(
        win, 
        text=f'{d}', 
        font=f
        ).place(x=390, y=70)

    Label(
        win, 
        text='Rate per hour: ', 
        font=cf
        ).place(x=10, y=110)

    Label(
        win, 
        text=f'{r}', 
        font=f
        ).place(x=125, y=110)

    Label(
        win, 
        text='Gross Salary: ',
        font=cf
        ).place(x=250, y=110)

    Label(
        win, 
        text=f'{gross_sal}', 
        font=f
        ).place(x=390, y=110)


    Label(
        win, 
        text='DEDUCTIONS',
        font='sans-serif 14', relief=SOLID, 
        pady=5, padx=10
        ).place(x=170, y=180)


    Label(
        win, 
        text='SSS: ', 
        font=cf
        ).place(x=10, y=240)

    Label(
        win, 
        text=f'{contri}', 
        font=f
        ).place(x=65, y=240)

    Label(
        win, 
        text='PhilHealth: ', 
        font=cf
        ).place(x=250, y=240)

    Label(
        win, 
        text=f'{ph}', 
        font=f
        ).place(x=390, y=240)

    Label(
        win, 
        text='Other Loan:', 
        font=cf
        ).place(x=10, y=280)
    
    Label(
        win,
        text=f'{hl}', 
        font=f
        ).place(x=105, y=280)

    Label(
        win, 
        text='Tax: ', 
        font=cf
        ).place(x=250, y=280)

    Label(
        win, 
        text=f'{tax}', 
        font=f
        ).place(x=390, y=280)

    Label(
        win, 
        text='Total Deductions: ', 
        font=cf
        ).place(x=10, y=320)

    Label(
        win, 
        text=f'{total_deduction}',
        font=f
        ).place(x=150, y=320)

    Label(
        win, 
        text='Net Salary:', 
        font=cf
        ).place(x=250, y=320)

    Label(
        win, 
        text=f'{net_sal}', 
        font=f
        ).place(x=390, y=320)

    Button(
        win, 
        text='Close', 
        padx=10, 
        pady=5, 
        font=f, 
        bg='#FF614F', 
        command=lambda:win.destroy()
        ).place(x=220, y=390)
