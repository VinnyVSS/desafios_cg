class Funcionario:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def calcular_salario(self):
        pass  

class FuncionarioPJ(Funcionario):
    def __init__(self, nome, idade, horas_trabalhadas, valor_hora):
        super().__init__(nome, idade)
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def calcular_salario(self):
        return self.horas_trabalhadas * self.valor_hora

class FuncionarioPF(Funcionario):
    def __init__(self, nome, idade, salario_fixo):
        super().__init__(nome, idade)
        self.salario_fixo = salario_fixo

    def calcular_salario(self):
        return self.salario_fixo


pj = FuncionarioPJ("Vinicius", 21, 12,80)
pf = FuncionarioPF("Michelle", 42, 4500)

print(f"{pj.nome} - Salário PJ: R${pj.calcular_salario():.2f}")
print(f"{pf.nome} - Salário PF: R${pf.calcular_salario():.2f}")
