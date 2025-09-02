import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class Gestao:
    def __init__(self, empresa):
        self.empresa = empresa
        self.funcs = []

    def adicionar_func(self, Funcionario):
        self.funcs.append(Funcionario)

    def show_funcs(self):
        return [str(i) for i in self.funcs]

class Funcionario:
    cont = 1
    def __init__(self, nome, salario):
        self.id = Funcionario.cont
        self.nome = nome
        self.salario = salario
        Funcionario.cont += 1

    def __str__(self):
        return f"ID:{self.id}, Nome:{self.nome} Salario: R${self.salario:.2f}"

class Funcionario_adm(Funcionario):
    def __init__(self, nome, salario, CRA):
        super().__init__(nome, salario)
        self.CRA = CRA

    def __str__(self):
        return f"{super().__str__()}, CRA:{self.CRA}, Tipo: Administrador"
        
class Funcionario_prof(Funcionario):
    def __init__(self, nome, salario, materia):
        super().__init__(nome, salario)
        self.materia = materia

    def __str__(self):

        return f"{super().__str__()}, Materia:{self.materia}, Tipo: Professor"

class Funcionario_tec(Funcionario):
    def __init__(self, nome, salario, area):
        super().__init__(nome, salario)
        self.area = area

    def __str__(self):
        return f"{super().__str__()}, Area:{self.area}, Tipo: Tecnico"

class GestaoApp(tk.Tk):
    def __init__(self, gestao):
        super().__init__()
        self.title("Sistema de Gestão de Funcionários")
        self.geometry("350x250")
        self.gestao = gestao

        self.frame_menu = tk.Frame(self)
        self.frame_menu.pack(pady=20)

        tk.Label(self.frame_menu, text=self.gestao.empresa, font=("Helvetica", 16)).pack(pady=10)

        self.btn_add = tk.Button(self.frame_menu, text="  Adicionar Funcionário", command=self.adicionar_funcionario_gui, width=30)
        self.btn_add.pack(pady=5)
        
        self.btn_show = tk.Button(self.frame_menu, text="  Mostrar Funcionários", command=self.mostrar_funcionarios_gui, width=30)
        self.btn_show.pack(pady=5)
        
        self.btn_exit = tk.Button(self.frame_menu, text="  Sair", command=self.destroy, width=30)
        self.btn_exit.pack(pady=5)

    def adicionar_funcionario_gui(self):
        add_window = tk.Toplevel(self)
        add_window.title("Adicionar Funcionário")

        self.tipo_var = tk.StringVar(add_window)
        self.tipo_var.set("adm") 

        tk.Label(add_window, text="Nome:").grid(row=0, column=0, padx=10, pady=5)
        entry_nome = tk.Entry(add_window)
        entry_nome.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(add_window, text="Salário:").grid(row=1, column=0, padx=10, pady=5)
        entry_salario = tk.Entry(add_window)
        entry_salario.grid(row=1, column=1, padx=10, pady=5)
        
        tk.Label(add_window, text="Tipo:").grid(row=2, column=0, padx=10, pady=5)
        tk.OptionMenu(add_window, self.tipo_var, "adm", "prof", "tec").grid(row=2, column=1, padx=10, pady=5)
        
        def on_add():
            nome = entry_nome.get()
            salario_str = entry_salario.get()
            tipo = self.tipo_var.get()

            try:
                salario = float(salario_str)
            except ValueError:
                messagebox.showerror("Erro de Salário", "Salário inválido. Digite um número.")
                return

            if tipo == "adm":
                cra = simpledialog.askstring("CRA", "Digite o CRA:", parent=add_window)
                if cra:
                    self.gestao.adicionar_func(Funcionario_adm(nome, salario, cra))
                    messagebox.showinfo("Sucesso", "Funcionário adicionado!")
                    add_window.destroy()
            elif tipo == "prof":
                materia = simpledialog.askstring("Matéria", "Digite a Matéria:", parent=add_window)
                if materia:
                    self.gestao.adicionar_func(Funcionario_prof(nome, salario, materia))
                    messagebox.showinfo("Sucesso", "Funcionário adicionado!")
                    add_window.destroy()
            elif tipo == "tec":
                area = simpledialog.askstring("Área", "Digite a Área:", parent=add_window)
                if area:
                    self.gestao.adicionar_func(Funcionario_tec(nome, salario, area))
                    messagebox.showinfo("Sucesso", "Funcionário adicionado!")
                    add_window.destroy()
            
        tk.Button(add_window, text="Adicionar", command=on_add).grid(row=3, column=0, columnspan=2, pady=10)

    def mostrar_funcionarios_gui(self):
        show_window = tk.Toplevel(self)
        show_window.title("Lista de Funcionários")
        
        texto_funcionarios = tk.Text(show_window, wrap="word", width=100, height=20)
        texto_funcionarios.pack(padx=10, pady=10)
        
        # Corrigido: Chamando o show_funcs correto que retorna uma lista de strings
        lista_str = self.gestao.show_funcs()
        if not lista_str:
            texto_funcionarios.insert(tk.END, "Nenhum funcionário cadastrado.")
        else:
            for func_str in lista_str:
                texto_funcionarios.insert(tk.END, func_str + "\n\n")

        texto_funcionarios.config(state=tk.DISABLED)

if __name__ == "__main__":
    Gestao1 = Gestao("Empresa X")
    app = GestaoApp(Gestao1)
    app.mainloop()
