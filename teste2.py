class Funcionario:
    def __init__(self, matricula='', nome='', dataAdmissao='', valorHora=0, valorHoraExtra=0, cargo='', status=''):
        self.matricula = matricula
        self.nome = nome
        self.dataAdmissao = dataAdmissao
        self.valorHora = valorHora
        self.valorHoraExtra = valorHoraExtra
        self.cargo = cargo
        self.status = status

    def calcularSalario(self, qtdeHorasTrabalhadas):
        return self.valorHora * qtdeHorasTrabalhadas

    def calcularTotalHorasExtras(self, qtdeHorasExtrasTrabalhadas):
        return self.valorHoraExtra * qtdeHorasExtrasTrabalhadas

    def reajustarValorHora(self, percentual):
        self.valorHora *= (1 + percentual / 100)
        self.valorHoraExtra *= (1 + percentual / 100)

# Instanciando um objeto da classe Funcionario
funcionario = Funcionario()

# Obtendo valores de entrada para as propriedades
funcionario.matricula = input("Matrícula: ")
funcionario.nome = input("Nome: ")
funcionario.dataAdmissao = input("Data de Admissão: ")
funcionario.valorHora = float(input("Valor da Hora: "))
funcionario.valorHoraExtra = float(input("Valor da Hora Extra: "))
funcionario.cargo = input("Cargo: ")
funcionario.status = input("Status: ")

# Executando os métodos e exibindo os resultados
qtdeHorasTrabalhadas = float(input("Quantidade de Horas Trabalhadas: "))
qtdeHorasExtrasTrabalhadas = float(input("Quantidade de Horas Extras Trabalhadas: "))

salario = funcionario.calcularSalario(qtdeHorasTrabalhadas)
totalHorasExtras = funcionario.calcularTotalHorasExtras(qtdeHorasExtrasTrabalhadas)

print("\n=== Informações do Funcionário ===")
print("Matrícula:", funcionario.matricula)
print("Nome:", funcionario.nome)
print("Data de Admissão:", funcionario.dataAdmissao)
print("Valor da Hora:", funcionario.valorHora)
print("Valor da Hora Extra:", funcionario.valorHoraExtra)
print("Cargo:", funcionario.cargo)
print("Status:", funcionario.status)
print("\n=== Resultados ===")
print("Salário:", salario)
print("Total de Horas Extras:", totalHorasExtras)
