class ContaBancaria:
    def __init__(self, numero: str, titular: str, saldo: float = 0) -> None:
        """Cria uma conta com número, titular e saldo inicial.
        str, str, float -> None"""

        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def troca_nome(self, novo_nome: str) -> str:
        """Troca o nome do titular.
        str -> str"""
        self.titular = novo_nome
        return self.titular

    def deposita(self, valor: float) -> bool:
        """Adiciona valor ao saldo, se for positivo.
        float -> bool"""
        if valor > 0:
            self.saldo += valor
            return True
        print('Valor inválido!')
        return False

    def saca(self, valor: float) -> bool:
        """Retira valor do saldo, se houver saldo suficiente.
        float -> bool"""
        if valor <= 0:
            print("Valor inválido")
            return False
        if self.saldo < valor:
            print("Saldo insuficiente")
            return False
        self.saldo -= valor
        print(f"Saque realizado. Saldo: R${self.saldo}")
        return True

class ContaInvestimento(ContaBancaria):
    def __init__(self, numero: str, titular: str, taxa_de_juros: float, saldo: float = 0) -> None:
        """Cria conta com taxa de juros.
        str, str, float, float -> None"""
        super().__init__(numero, titular, saldo)
        self.taxa_de_juros = taxa_de_juros

    def aplica_juros(self) -> float:
        """Aplica juros ao saldo da conta.
        None -> float"""
        juros = self.saldo * self.taxa_de_juros / 100
        self.saldo += juros
        print(f"Juros: R${juros:.2f}. Novo saldo: R${self.saldo:.2f}")
        return self.saldo

class Pessoa:
    def __init__(self, nome_completo: str, CPF: str) -> None:
        """Cria pessoa com nome e CPF.
        str, str -> None"""
        self.nome_completo = nome_completo
        self.CPF = CPF

    def primeiro_nome(self) -> str:
        """Retorna o primeiro nome da pessoa.
        None -> str"""
        return self.nome_completo.split()[0]

class Cliente(Pessoa):
    def __init__(self, nome_completo: str, CPF: str, senha: str) -> None:
        """Cria cliente com senha.
        str, str, str -> None"""
        super().__init__(nome_completo, CPF)
        self.senha = senha

    def validar_operacao(self, senha: str) -> bool:
        """Verifica se a senha está correta.
        str -> bool"""
        return senha == self.senha

class Funcionario(Pessoa):
    def __init__(self, nome_completo: str, CPF: str, salario: float) -> None:
        """Cria funcionário com salário.
        str, str, float -> None"""
        super().__init__(nome_completo, CPF)
        self.salario = salario

    def receber_aumento(self, porcentagem: float) -> float:
        """Aplica aumento percentual no salário.
        float -> float"""
        self.salario += self.salario * porcentagem / 100
        return self.salario

class Gerente(Funcionario):
    def __init__(self, nome_completo: str, CPF: str, salario: float) -> None:
        """Cria gerente com lista de gerenciados.
        str, str, float -> None"""
        super().__init__(nome_completo, CPF, salario)
        self.lista_gerenciados = []

    def receber_aumento(self, porcentagem: float, extra: float = 500) -> float:
        """Aumento com valor extra para gerentes.
        float, float -> float"""
        super().receber_aumento(porcentagem)
        self.salario += extra
        return self.salario

class SistemaBancario:
    def __init__(self) -> None:
        """Cria sistema com listas de clientes, contas e funcionários.
        None -> None"""
        self.lista_clientes = []
        self.lista_contas = []
        self.lista_funcionarios = []

    def adiciona_clientes(self, novo_cliente: 'Cliente') -> list:
        """Adiciona cliente à lista.
        Cliente -> list"""
        self.lista_clientes.append(novo_cliente)
        return self.lista_clientes

    def adiciona_contas(self, nova_conta: 'ContaBancaria') -> list:
        """Adiciona conta à lista.
        ContaBancaria -> list"""
        self.lista_contas.append(nova_conta)
        return self.lista_contas

    def adiciona_funcionarios(self, novo_funcionario: 'Funcionario') -> list:
        """Adiciona funcionário à lista.
        Funcionario -> list"""
        self.lista_funcionarios.append(novo_funcionario)
        return self.lista_funcionarios

    def dar_aumento(self, porcentagem: float) -> None:
        """Dá aumento a todos os funcionários.
        float -> None"""
        for funcionario in self.lista_funcionarios:
            funcionario.receber_aumento(porcentagem)