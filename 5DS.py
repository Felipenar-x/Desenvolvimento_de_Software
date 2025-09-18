class Transacao:
    def __init__(self):
        self.conta = None   
    
    def registrar_conta(self,conta:"Conta"):
        self.conta = conta  


class Saque(Transacao):
    def __init__(self,valor:float):
        super().__init__()
        self.valor = valor


class Deposito(Transacao):
    def __init__(self,valor:float):
        super().__init__()
        self.valor = valor


class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao: Transacao):
        self.transacoes.append(transacao)  
    

class Cliente:
    def __init__(self,endereco:str,contas:list):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self,transacao:Transacao,conta:"Conta"):
        transacao.registrar_conta(conta)

        
    def adicionar_conta(self,conta:"Conta"):
        self.contas.append(conta)
        conta.cliente = self
        

class PessoaFisica(Cliente):
    def __init__(self,endereco:str,conta:list,cpf:str,nome:str,data_nascimento:str):
        super().__init__(endereco,conta)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento


class Conta:
    def __init__(self,saldo:float,numero:int,agencia:str,cliente:Cliente,historico:Historico):
        self.saldo = saldo
        self.numero = numero    
        self.agencia = agencia
        self.cliente = cliente
        self.historico = historico

    def consultar_saldo(self):
        return self.saldo
    
    def nova_conta(self,cliente:Cliente,conta:"Conta"):
        self.conta = conta
        
        
    def sacar(self,valor:float):
        if valor > self.saldo:
            return False
        else:
            self.saldo -= valor
            return True

    def depositar(self,valor:float):
        if valor > 0:
            self.saldo += valor
            return True
        else:
            return False


class ContaCorrente(Conta):
    def __init__(self,saldo:float,numero:int,agencia:str,cliente:Cliente,historico:Historico,limite:float,limite_saques:int):
        super().__init__(saldo,numero,agencia,cliente,historico)
        self.limite = limite
        self.limite_saques = limite_saques


historico = Historico()

cliente1 = PessoaFisica("Rua A, 123", "111.222.333-44", "João","123123123","01/01/1990",)

conta1 = ContaCorrente(1000, 1, "0001", historico, limite=500, limite_saques=3,historico=historico)

cliente1.adicionar_conta(conta1)

cliente1.realizar_transacao(Deposito(200), conta1)

cliente1.realizar_transacao(Saque(300), conta1)

print("Saldo atual:", conta1.consultar_saldo())

