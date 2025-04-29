class Produto:
    def __init__(self, codigo, nome, descricao, preco):
        self.codigo = codigo
        self.nome = str(nome)
        self.descricao = str(descricao)
        self.preco = preco

    def calcula_desconto(self, desconto):
        preco_final = self.preco * desconto / 100
        return preco_final


class Eletronicos(Produto):
    def __init__(self, codigo, nome, descricao, preco, garantia):
        super().__init__(codigo, nome, descricao, preco)
        self.garantia = garantia


class Roupas(Produto):
    def __init__(self, codigo, nome, descricao, preco, tamanho, cor):
        super().__init__(codigo, nome, descricao, preco)
        self.tamanho = tamanho
        self.cor = cor


class Pessoa:
    def __init__(self, nome_completo, idade, estado_civil, nome_social=None):
        self.nome_completo = str(nome_completo)
        self.nome_social = str(nome_social)
        self.idade = int(idade)
        self.estado_civil = str(estado_civil)

    def mudar_estado_civil(self):
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
    def mudar_nome_social(self,novo_nome):
        self.nome_social = novo_nome
        return self.nome_social
    def registrar_aniversario(self):
        self.idade += 1
        return self.idade
class PessoaFisica(Pessoa):
    def __init__(self,nome_completo, idade, estado_civil, CPF,RG,nome_social=None):
        super().__init__(nome_completo, idade, estado_civil, nome_social)
        self.CPF = str(CPF)
        self.RG = str(RG)
class PessoaJuridica(Pessoa):
    def __init__(self,nome_completo, idade, estado_civil,CNPJ, nome_social=None):
        super().__init__(nome_completo, idade, estado_civil, nome_social)
        self.CNPJ = str(CNPJ)
class Empregado(PessoaFisica):
    def __init__(self,nome_completo, idade, estado_civil, CPF,RG,salario,nome_social=None):
        super().__init__(nome_completo, idade, estado_civil, CPF,RG,nome_social)
        self.salario = salario
    def salario_anual(self):
        salario_anual = self.salario*12
        return salario_anual
class Empresa(PessoaJuridica):
    def __init__(self,nome_completo, idade, estado_civil,CNPJ,nome_fantasia,funcionarios, nome_social=None):
        super().__init__(self,nome_completo, idade, estado_civil,CNPJ, nome_social)
        self.nome_fantasia = str(nome_fantasia)
        self.funcionarios = []
    def contrata_funcionario(self,funcionario_novo):
        funcionario_novo = str(input("Digite o nome do novo funcionário: "))
        self.funcionarios.append(funcionario_novo)
        return self.funcionarios
    def demite_funcionario(self,funcionario):
        self.funcionarios.remove(funcionario)
        return self.funcionarios
class Personagem:
    def __init__(self,nome,classe,vida=100):
        self.nome = nome 
        self.classe = classe
        self.vida = vida
    def atacar(self,inimigo,dano):
        """Aplica dano ao inimigo.
        float -> float"""
        if inimigo.vida > 0:
            inimigo.vida -= dano
            return inimigo.vida
    def defender(self,dano):
        """Defende-se de um ataque inimigo.
        float -> float"""
        self.vida -= (dano/2)
        return self.vida    
    def descansar(self):
        self.vida = 100
        return self.vida
class Barbaro(Personagem):
    def __init__(self, nome, vida=100):
        super().__init__(nome, "Barbaro", vida)
        self.em_furia = False
        self.furias_restantes = 2
    def ativar_furias(self):
        if self.furias_restantes > 0:
            self.furias_restantes -= 1
            self.em_furia = True
            return self.furias_restantes, self.em_furia
        else:
            print("Você não tem furias disponíveis!")
            return self.furias_restantes
    def atacar(self, inimigo, dano):
        if self.em_furia:
            dano *= 2
            self.em_furia = False  
        return super().atacar(inimigo, dano)
    def descansar(self):
        self.furias_restantes = 2
        self.em_furia = False
        return super().descansar()
class Clerigo(Personagem):
    def __init__(self, nome, vida=100):
        super().__init__(nome, "Clerigo", vida)
    def cura(self,alvo,valor_cura):
        alvo.vida += valor_cura
        return alvo.vida
    def defender(self, dano):
        dano_reduzido = dano * 0.75
        return super().defender(dano_reduzido)
class Guerreiro(Personagem):
    def __init__(self, nome, nivel_de_combate, nivel_de_armadura, vida=100):
        super().__init__(nome, "Guerreiro", vida)
        self.nivel_de_combate = nivel_de_combate
        self.nivel_de_armadura = nivel_de_armadura
    def atacar(self,inimigo,dano):
        return super().atacar(inimigo, dano + self.nivel_de_combate)
    def defender(self,dano):
        dano_reduzido = max(0, dano - self.nivel_de_armadura)  
        return super().defender(dano_reduzido)
Caio = Pessoa("Caio Wellington de Souza Laurentino", 19,"Casado")
print(Caio.estado_civil)
Caio.mudar_estado_civil()
print(Caio.estado_civil)