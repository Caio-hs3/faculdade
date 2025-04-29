class Usuario:
    def __init__(self,nome,matricula):
        self.nome = nome
        self.matricula = matricula
class Aluno(Usuario):
    def __init__(self,nome,matricula):
        super().__init__(nome,matricula)
        self.materias = []
    def inscricao_materais(self,materia):
        if materia not in materias:
            self.materias.append(materia)
            print(f"A matéria {materia} foi adicionada as matérias ativas!")
            return self.materias
        else:
            print(f"A matéria {materia} já está sendo cursada!")
            return self.materias
    def informacoes_aluno(self):
        print(f"""Nome do aluno: {self.nome}
        Matrícula do aluno: {self.matricula}
        Matérias inscritas:""")
        for materia in self.materias:
            print('\t', materia)
class PosGraduando(Aluno):
    def __init__(self,nome,matricula,area_pesquisa):
        super().__init__(nome,matricula)
        self.area_pesquisa = area_pesquisa
    def troca_area(self,nova_area):
        if self.area_pesquisa != nova_area:
            self.area_pesquisa = nova_area
            print(f"O aluno {self.nome} mudou sua área de pesquisa para: {nova_area}")
            return self.area_pesquisa
        else:
            print(f'O aluno {self.nome} já está nessa área de pesquisa!')
            return self.area_pesquisa
class Professor(Usuario):
    def __init__(self,nome,matricula,departamento):
        super().__init__(nome,matricula)
        self.departamento = departamento
aluno1 = Aluno("Caio","20240318")
aluno1.materias.append("Computação 2")
aluno1.materias.append("Álgebra Linear")
aluno1.informacoes_aluno()
aluno2 = PosGraduando("Pedro","20240312","Curvas algébricas")
aluno2.troca_area("Análise")
aluno2.troca_area("Análise")