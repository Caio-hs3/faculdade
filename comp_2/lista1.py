class Conta:
    def __init__(self, numero, titular, saldo=0, limite=1):
        self.limite = limite
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def troca_nome(self,novo_nome):
        """Troca o nome do titular da conta.
        str -> str"""
        self.titular = novo_nome
        return self.titular
    def deposita(self, valor):
        """Deposita um valor em uma conta.
        float -> float"""
        if valor > 0:
            self.saldo += valor
            return True
        else:
            print('Valor inválido!')
            return False

    def saca(self, valor):
        """Saca um valor de uma conta.
        float -> bool"""
        if valor <= 0:
            print("Valor inválido")
            return False
        if self.saldo < valor:
            print("A operação não foi bem sucedida")
            return False
        else:
            self.saldo -= valor
            print(f"A operação foi bem sucedida. Novo saldo: R${self.saldo}")
            return True

    def extrato(self):
        """Exibe o saldo de uma conta e seu número.
        -> float"""
        print(f"""Saldo da conta: R${self.saldo}
Número da conta: {self.numero}.""")
        return self.saldo

    def transfere_para(self, destino, valor):
        """Transfere valores de uma conta para outra.
        (Conta, float) -> bool"""
        if valor <= 0:
            print("Valor inválido")
            return False
        if self.saldo < valor:
            print("A operação não foi bem sucedida")
            return False
        else:
            if self.saca(valor) and destino.deposita(valor):
                print("A operação foi bem sucedida")
                return True
        return False

class ContaInvestimento(Conta):
    def __init__(self, numero, titular,taxa_de_juros, saldo=0, limite=1):
        super().__init__(numero, titular, saldo, limite)
        self.taxa_de_juros = taxa_de_juros
    def aplica_juros(self):
        juros = self.saldo * self.taxa_de_juros / 100
        self.saldo += juros
        print(f"Juros de {self.taxa_de_juros}% aplicados. R${juros:.2f} adicionados. Novo saldo: R${self.saldo:.2f}")
        return self.saldo
class Pessoa:
    def __init__(self,nome_completo,CPF):
        self.nome_completo = str(nome_completo)
        self.CPF = str(CPF)
    def primeiro_nome(self):
        primeiro_nome = self.nome_completo[0:self.nome_completo.find(" ")]
        print(primeiro_nome)
        return primeiro_nome
class Cliente(Pessoa):
    def __init__(self,nome_completo,CPF,senha):
        super().__init__(nome_completo,CPF)
        self.senha = senha
    def validar_operacao(self,senha):
        if senha == self.senha:
            return True
        else:
            return False
class Funcionario(Pessoa):
    def __init__(self,nome_completo,CPF,salario):
        super.__init__(nome_completo,CPF)
        self.salario = float(salario)
    def receber_aumento(self,porcentagem_aumento):
        porcentagem_aumento = porcentagem_aumento/100
        self.salario = self.salario * porcentagem_aumento
        return self.salario
class Gerente(Funcionario):
    def __init__(self,nome_completo,CPF,salario,lista__gerenciados):
        super().__init__(nome_completo,CPF,salario)
        self.lista_gerenciados = []
conta = Conta(23, "Caio", 15, 10)
banco = Conta(32, "Pedro", 12, 15000)
conta1 = ContaInvestimento(25,"Caio",10,1500,3000)
conta1.aplica_juros()
Caio = Pessoa("Caio Wellington de Souza Laurentino",15149004758)
print(type(Caio.CPF))
Caio.primeiro_nome()