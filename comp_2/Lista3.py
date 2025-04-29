class Produto:
    def __init__(self, codigo, nome, descricao, preco):
        """Inicializa um produto com código, nome, descrição e preço.
        int, str, str, float -> None"""
        self.codigo = codigo
        self.nome = str(nome)
        self.descricao = str(descricao)
        self.preco = preco

    def calcula_desconto(self, desconto):
        """Calcula o valor de desconto sobre o preço e retorna o preço final com desconto.
        float -> float"""
        valor_desconto = self.preco * desconto / 100
        preco_final = self.preco - valor_desconto
        return preco_final
class Eletronicos(Produto):
    def __init__(self, codigo, nome, descricao, preco, garantia):
        """Inicializa um eletrônico com garantia.
        int, str, str, float, int -> None"""
        super().__init__(codigo, nome, descricao, preco)
        self.garantia = garantia


class Roupas(Produto):
    def __init__(self, codigo, nome, descricao, preco, tamanho, cor):
        """Inicializa uma roupa com tamanho e cor.
        int, str, str, float, str, str -> None"""
        super().__init__(codigo, nome, descricao, preco)
        self.tamanho = tamanho
        self.cor = cor


class Pessoa:
    def __init__(self, nome_completo, idade, estado_civil, nome_social=None):
        """Inicializa uma pessoa com nome completo, idade, estado civil e nome social opcional.
        str, int, str, str -> None"""
        self.nome_completo = str(nome_completo)
        self.nome_social = str(nome_social)
        self.idade = int(idade)
        self.estado_civil = str(estado_civil)

    def mudar_estado_civil(self):
        """Interage com o usuário para mudar o estado civil.
        None -> str | None"""
        while True:
            print("""Para qual estado civil você gostaria de mudar?
            Solteiro = 1
            Casado = 2
            Divorciado = 3
            Viúvo = 4
            União Estável = 5""")
            try:
                escolha = int(input("Digite o número correspondente ao de sua escolha: "))
                opcoes = {
                    1: "Solteiro",
                    2: "Casado",
                    3: "Divorciado",
                    4: "Viúvo",
                    5: "União Estável"
                }
                if escolha == 0:
                    print("Operação cancelada.")
                    return None
                if escolha in opcoes:
                    novo_estado = opcoes[escolha]
                    if hasattr(self, 'estado_civil') and novo_estado == self.estado_civil:
                        print(f"Você já possui este estado civil ({self.estado_civil}).")
                        continue
                    self.estado_civil = novo_estado
                    print(f"Estado civil alterado para: {self.estado_civil}")
                    return self.estado_civil
                else:
                    print("Opção inválida. Digite um número entre 1 e 5.")
            except ValueError:
                print("Erro: Digite apenas números inteiros!")

    def mudar_nome_social(self, novo_nome):
        """Altera o nome social.
        str -> str"""
        self.nome_social = novo_nome
        return self.nome_social

    def registrar_aniversario(self):
        """Incrementa a idade em 1 ano.
        None -> int"""
        self.idade += 1
        return self.idade


class PessoaFisica(Pessoa):
    def __init__(self, nome_completo, idade, estado_civil, CPF, RG, nome_social=None):
        """Inicializa uma pessoa física com CPF e RG.
        str, int, str, str, str, str -> None"""
        super().__init__(nome_completo, idade, estado_civil, nome_social)
        self.CPF = str(CPF)
        self.RG = str(RG)


class PessoaJuridica(Pessoa):
    def __init__(self, nome_completo, idade, estado_civil, CNPJ, nome_social=None):
        """Inicializa uma pessoa jurídica com CNPJ.
        str, int, str, str, str -> None"""
        super().__init__(nome_completo, idade, estado_civil, nome_social)
        self.CNPJ = str(CNPJ)


class Empregado(PessoaFisica):
    def __init__(self, nome_completo, idade, estado_civil, CPF, RG, salario, nome_social=None):
        """Inicializa um empregado com salário.
        str, int, str, str, str, float, str -> None"""
        super().__init__(nome_completo, idade, estado_civil, CPF, RG, nome_social)
        self.salario = salario

    def salario_anual(self):
        """Calcula o salário anual.
        None -> float"""
        salario_anual = self.salario * 12
        return salario_anual


class Empresa(PessoaJuridica):
    def __init__(self, nome_completo, idade, estado_civil, CNPJ, nome_fantasia, nome_social=None):
        """Inicializa uma empresa com nome fantasia e lista de funcionários.
        str, int, str, str, str, list, str -> None"""
        super().__init__(nome_completo, idade, estado_civil, CNPJ, nome_social)
        self.nome_fantasia = str(nome_fantasia)
        self.funcionarios = []

    def contrata_funcionario(self, funcionario_novo):
        """Adiciona um novo funcionário à lista.
        str -> list"""
        funcionario_novo = str(input("Digite o nome do novo funcionário: "))
        self.funcionarios.append(funcionario_novo)
        return self.funcionarios

    def demite_funcionario(self, funcionario):
        """Remove um funcionário da lista.
        str -> list"""
        self.funcionarios.remove(funcionario)
        return self.funcionarios


class Personagem:
    def __init__(self, nome, classe, vida=100):
        """Inicializa um personagem com nome, classe e vida.
        str, str, int -> None"""
        self.nome = nome
        self.classe = classe
        self.vida = vida

    def atacar(self, inimigo, dano):
        """Aplica dano ao inimigo.
        float -> float"""
        if inimigo.vida > 0:
            inimigo.vida -= dano
            return inimigo.vida

    def defender(self, dano):
        """Defende-se de um ataque inimigo.
        float -> float"""
        self.vida -= (dano / 2)
        return self.vida

    def descansar(self):
        """Restaura a vida do personagem para 100.
        None -> int"""
        self.vida = 100
        return self.vida


class Barbaro(Personagem):
    def __init__(self, nome, vida=100):
        """Inicializa um bárbaro com furias disponíveis e sem estar em fúria.
        str, int -> None"""
        super().__init__(nome, "Barbaro", vida)
        self.em_furia = False
        self.furias_restantes = 2

    def ativar_furias(self):
        """Ativa a fúria se houver fúrias restantes.
        None -> tuple | int"""
        if self.furias_restantes > 0:
            self.furias_restantes -= 1
            self.em_furia = True
            return self.furias_restantes, self.em_furia
        else:
            print("Você não tem furias disponíveis!")
            return self.furias_restantes

    def atacar(self, inimigo, dano):
        """Ataca com o dobro do dano se estiver em fúria.
        Personagem, float -> float"""
        if self.em_furia:
            dano *= 2
            self.em_furia = False
        return super().atacar(inimigo, dano)

    def descansar(self):
        """Restaura vida e fúrias do bárbaro.
        None -> int"""
        self.furias_restantes = 2
        self.em_furia = False
        return super().descansar()


class Clerigo(Personagem):
    def __init__(self, nome, vida=100):
        """Inicializa um clérigo.
        str, int -> None"""
        super().__init__(nome, "Clerigo", vida)

    def cura(self, alvo, valor_cura):
        """Cura outro personagem.
        Personagem, float -> float"""
        alvo.vida += valor_cura
        return alvo.vida

    def defender(self, dano):
        """Defende recebendo apenas 75% do dano.
        float -> float"""
        dano_reduzido = dano * 0.75
        return super().defender(dano_reduzido)


class Guerreiro(Personagem):
    def __init__(self, nome, nivel_de_combate, nivel_de_armadura, vida=100):
        """Inicializa um guerreiro com níveis de combate e armadura.
        str, int, int, int -> None"""
        super().__init__(nome, "Guerreiro", vida)
        self.nivel_de_combate = nivel_de_combate
        self.nivel_de_armadura = nivel_de_armadura

    def atacar(self, inimigo, dano):
        """Ataca com bônus do nível de combate.
        Personagem, float -> float"""
        return super().atacar(inimigo, dano + self.nivel_de_combate)

    def defender(self, dano):
        """Defende reduzindo o dano com base na armadura.
        float -> float"""
        dano_reduzido = max(0, dano - self.nivel_de_armadura)
        return super().defender(dano_reduzido)