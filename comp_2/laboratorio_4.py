from abc import ABC, abstractmethod

class Pessoa(ABC):
    """
    Classe abstrata que representa uma pessoa com nome, endereço e idade.
    """

    def __init__(self, nome: str, endereco: str, idade: int):
        self.__nome = nome
        self.__endereco = endereco
        self.__idade = idade

    @abstractmethod
    def get_id(self) -> str:
        """
        Retorna o identificador da pessoa.
        () -> str
        """
        pass

    @abstractmethod
    def __eq__(self, objeto: object) -> bool:
        """
        Verifica igualdade entre duas pessoas.
        object -> bool
        """
        pass

    def set_endereco(self, novo_endereco: str) -> str:
        """
        Altera o endereço da pessoa.
        str -> str
        """
        self.__endereco = novo_endereco
        return self.__endereco

    def aniversario(self) -> int:
        """
        Incrementa a idade da pessoa.
        None -> int
        """
        self.__idade += 1
        return self.__idade

    def __str__(self) -> str:
        """
        Retorna string com os dados da pessoa.
        None -> str
        """
        return f"""Nome: {self.__nome}
Idade: {self.__idade}
Endereço: {self.__endereco}"""

class PessoaFisica(Pessoa):
    """
    Representa uma pessoa física com CPF e estado civil.
    """

    def __init__(self, nome: str, endereco: str, idade: int, CPF: str, estado_civil: str):
        super().__init__(nome, endereco, idade)
        self.__CPF = CPF
        self.__estado_civil = estado_civil

    def get_id(self) -> str:
        """
        Retorna o CPF da pessoa física.
        None -> str
        """
        return self.__CPF

    def __eq__(self, other: object) -> bool:
        """
        Verifica igualdade com base no CPF.
        object -> bool
        """
        if not isinstance(other, PessoaFisica):
            return False
        return self.__CPF == other.__CPF

    def set_estado_civil(self, novo_estado: str) -> str:
        """
        Altera o estado civil da pessoa.
        str -> str
        """
        self.__estado_civil = novo_estado
        return self.__estado_civil

    def __str__(self) -> str:
        """
        Retorna string com os dados da pessoa física.
        None -> str
        """
        dados_pessoa = super().__str__()
        return f"""{dados_pessoa}
CPF: {self.__CPF}
Estado Civil: {self.__estado_civil}"""

class PessoaJuridica(Pessoa):
    """
    Representa uma pessoa jurídica com CNPJ.
    """

    def __init__(self, nome: str, endereco: str, idade: int, CNPJ: str):
        super().__init__(nome, endereco, idade)
        self.__CNPJ = CNPJ

    def get_id(self) -> str:
        """
        Retorna o CNPJ da pessoa jurídica.
        None -> str
        """
        return self.__CNPJ

    def __eq__(self, other: object) -> bool:
        """
        Verifica igualdade com base no CNPJ.
        object -> bool
        """
        if not isinstance(other, PessoaJuridica):
            return False
        return self.__CNPJ == other.__CNPJ

    def __str__(self) -> str:
        """
        Retorna string com os dados da pessoa jurídica.
        None -> str
        """
        dados_pessoa = super().__str__()
        return f"""{dados_pessoa}
CNPJ: {self.__CNPJ}"""

class Empregado(PessoaFisica):
    """
    Representa um empregado que é uma pessoa física com salário.
    """

    def __init__(self, nome: str, endereco: str, idade: int, salario: float, estado_civil: str, CPF: str):
        super().__init__(nome, endereco, idade, CPF, estado_civil)
        self.__salario = salario

    def aumentar_salario(self, porcentagem_aumento: float) -> float:
        """
        Aumenta o salário do empregado com base em porcentagem.
        float -> float
        """
        aumento = self.__salario * porcentagem_aumento / 100
        self.__salario += aumento
        return self.__salario

    def total_anual(self) -> float:
        """
        Retorna o total anual recebido (13 salários).
        None -> float
        """
        return self.__salario * 13

    def __str__(self) -> str:
        """
        Retorna string com os dados do empregado.
        None -> str
        """
        dados_pessoa = super().__str__()
        return f"""{dados_pessoa}
CPF: {self._PessoaFisica__CPF}
Estado Civil: {self._PessoaFisica__estado_civil}
Salário: {self.__salario:.2f}"""

    def get_id(self) -> str:
        """
        Retorna o CPF do empregado.
        None -> str
        """
        return self._PessoaFisica__CPF

    def __eq__(self, other: object) -> bool:
        """
        Verifica igualdade entre empregados por CPF.
        object -> bool
        """
        if not isinstance(other, PessoaFisica):
            return False
        return self._PessoaFisica__CPF == other._PessoaFisica__CPF

class Empresa(PessoaJuridica):
    """
    Representa uma empresa com uma lista de empregados.
    """

    def __init__(self, nome: str, endereco: str, idade: int, CNPJ: str, empregados: list = None):
        super().__init__(nome, endereco, idade, CNPJ)
        if empregados is None:
            empregados = []
        self.__empregados = empregados

    def contratar(self, novo_empregado: object) -> list:
        """
        Adiciona novo empregado à empresa.
        object -> list
        """
        if novo_empregado not in self.__empregados:
            self.__empregados.append(novo_empregado)
        else:
            print("Empregado já contratado!")
        return self.__empregados

    def demitir(self, empregado: object) -> list:
        """
        Remove empregado da empresa.
        object -> list
        """
        if empregado in self.__empregados:
            self.__empregados.remove(empregado)
        else:
            print("Empregado não pertence à empresa!")
        return self.__empregados

    def __len__(self) -> int:
        """
        Retorna a quantidade de empregados.
        None -> int
        """
        return len(self.__empregados)

    def __str__(self) -> str:
        """
        Retorna string com dados da empresa e IDs dos empregados.
        None -> str
        """
        dados_pessoa = super().__str__()
        return f"""{dados_pessoa}
Empregados: {[emp.get_id() for emp in self.__empregados]}"""

    def get_id(self) -> str:
        """
        Retorna o CNPJ da empresa.
        None -> str
        """
        return self._PessoaJuridica__CNPJ

    def __eq__(self, other: object) -> bool:
        """
        Verifica igualdade entre empresas por CNPJ.
        object -> bool
        """
        if not isinstance(other, PessoaJuridica):
            return False
        return self._PessoaJuridica__CNPJ == other._PessoaJuridica__CNPJ

class EmpregadoPJ(Empregado):
    """
    Representa um prestador de serviços PJ que é um empregado com informações de PJ.
    """

    def __init__(self, nome: str, endereco: str, idade: int, salario: float, estado_civil: str, CPF: str, CNPJ: str, contrato: str):
        Empregado.__init__(self, nome, endereco, idade, salario, estado_civil, CPF)
        self.__CNPJ = CNPJ
        self.__empregados = [self]
        self.__contrato = contrato

    def get_id(self) -> str:
        """
        Retorna a concatenação do CPF e CNPJ.
        None -> str
        """
        return f"{self._PessoaFisica__CPF} {self.__CNPJ}"

    def __eq__(self, other: object) -> bool:
        """
        Verifica igualdade por CPF ou CNPJ.
        object -> bool
        """
        if isinstance(other, PessoaFisica):
            return self._PessoaFisica__CPF == other._PessoaFisica__CPF
        elif isinstance(other, PessoaJuridica):
            return self.__CNPJ == other.__CNPJ
        return False

    def __str__(self) -> str:
        """
        Retorna string com dados do EmpregadoPJ.
        None -> str
        """
        dados_empregado = Empregado.__str__(self)
        return f"""{dados_empregado}
CNPJ: {self.__CNPJ}
Contrato: {self.__contrato}"""

# Testes
empregado1 = Empregado("Mariana Silva", "Av. das Flores, 123", 25, 2800.0, "Solteira", "456.789.012-34")
empregado2 = Empregado("Ricardo Oliveira", "Rua dos Pinheiros, 456", 32, 4200.0, "Casado", "789.012.345-67")
empregado3 = Empregado("Mariana Silva", "Av. das Flores, 123", 25, 2800.0, "Solteira", "456.789.012-34")  # Mesmo CPF de empregado1
prestador1 = EmpregadoPJ("Fernanda Costa", "Travessa das Acácias, 789", 41, 6000.0, "Divorciada", "123.456.789-01", "23.456.789/0001-23", "ABC-543")

print(empregado1)
print(empregado2)
print(empregado3)
print(prestador1)

print(isinstance(empregado1, EmpregadoPJ))
print(isinstance(empregado1, Empregado))
print(isinstance(empregado1, PessoaFisica))
print(isinstance(empregado1, Empresa))
print(isinstance(empregado1, PessoaJuridica))
print(isinstance(empregado1, Pessoa))

print(Empregado.mro())

print(isinstance(prestador1, EmpregadoPJ))
print(isinstance(prestador1, Empregado))
print(isinstance(prestador1, PessoaFisica))
print(isinstance(prestador1, Empresa))
print(isinstance(prestador1, PessoaJuridica))
print(isinstance(prestador1, Pessoa))

print(EmpregadoPJ.mro())

print(empregado1 == empregado2)
print(empregado1 == empregado3)
print(empregado2 == prestador1)

empresa = Empresa("InovaTech Solutions", "Setor Comercial, 1000", 8, "01.234.567/0001-02", [])
print(len(empresa))
print(empresa)

empresa.contratar(empregado1)
empresa.contratar(empregado2)
print(len(empresa))
print(empresa)

empresa.demitir(empregado2)
print(len(empresa))
print(empresa)

empresa.demitir(empregado2)
empresa.contratar(empregado3)
empresa.contratar(prestador1)
print(len(empresa))
print(empresa)

prestador1.set_endereco("Alameda dos Ipês, 202")
prestador1.set_estado_civil("Viúva")
prestador1.aniversario()
prestador1.aumentar_salario(800.0 / prestador1._Empregado__salario * 100)

print(prestador1.total_anual())
print(empresa)