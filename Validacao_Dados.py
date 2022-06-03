
import os
import sys

# Mensagens
from tkinter import messagebox



class Trata_Dados:


	def valida_entrada( emp_name, rph , duty, s3_contrib, phealth, hloan):

		emp_n = str(emp_name.get())
		rp = str(rph.get())
		dt = str(duty.get())
		s3 = str(s3_contrib.get())
		ph = str(phealth.get())
		hl = str(hloan.get())
		_msg=True

		if len(emp_n) < 5: # Pode ser nome Chines ou Koreano
			messagebox.showinfo("Erro no Nome", "Nome inválido, Corrija.")
			_msg=False

		## Continua validação dos valores 
		Var_checagem=(rp,dt,s3,ph,hl)
		for var_checa in Var_checagem:
			for var in var_checa:
				if var.upper() in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ!?/@#$%¨&*()_+=-[´{`]~}^;:><'):
					messagebox.showinfo("Erro de Dados", "Dados Numéricos inválidos, corrija.")
					_msg=False

		return _msg
