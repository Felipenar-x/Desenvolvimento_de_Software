#PACIENTE Felipe Naraki - 10443778
from typing import override


class Paciente:
    numero = 0
    def __init__(self, nome, idade, cpf, plano_de_saude):
        Paciente.numero += 1
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf
        self.__plano_de_saude = plano_de_saude
        self.numero = Paciente.numero

    def exibir_informacoes(self):
        print(f"Paciente Nº{self.numero}, :nome: {self.nome}, idade: {self.idade},anos cpf: {self.__cpf}, plano de saude: {self.__plano_de_saude}")

    @override
    def __str__(self):
        return f"Paciente Nº{self.numero}, :nome: {self.nome}, idade: {self.idade},anos cpf: {self.__cpf}, plano de saude: {self.__plano_de_saude}"


paciente1 = Paciente("Joao","25","123456789","itau")
paciente2 = Paciente("tonykill","39","4122069","bradesco")

print(paciente1)
print(paciente2)

