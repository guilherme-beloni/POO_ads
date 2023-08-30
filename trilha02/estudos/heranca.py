class Funcionario:
  def __init__(self, matricula, nome, dataAdmissao, valorHora, valorHoraExtra, cargo, status):
    self.__matricula = matricula
    self.__nome = nome
    self.__dataAdmissao = dataAdmissao
    self.__valorHora = valorHora
    self.__valorHoraExtra = valorHoraExtra
    self.__cargo = cargo
    self.__status = status


  def getMatricula(self):
    return self.__matricula
  def setmatricula(self, matricula):
    self.__matricula = matricula


  def getNome(self):
    return self.__nome
  def setNome(self, nome):
    self.__nome = nome


  def getdataAdmissao(self):
    return self.__dataAdmissao
  def setdataAdmissao(self, dataAdmissao):
    self.__dataAdmissao = dataAdmissao


  def getvalorHora(self):
    return self.__valorHora
  def setvalorHora(self, valorHora):
    self.__valorHora = valorHora


  def getvalorHoraExtra(self):
    return self.__valorHoraExtra
  def setvalorHoraExtra(self, valorHoraExtra):
    self.__valorHoraExtra = valorHoraExtra


  def getcargo(self):
    return self.__cargo
  def setcargo(self, cargo):
    self.__cargo = cargo


  def getstatus(self):
    return self.__status
  def setstatus(self, status):
    self.__status = status


  def calculaSalario(self, qtdHoras):
    return self.__valorHora * qtdHoras

  def calculaHExtra(self, qtdHoras):
    return self.__valorHoraExtra * qtdHoras

  def calculaReajuste(self, porcento):
    return self.__valorHora + self.__valorHora * porcento/100

  def calculaReajusteExtra(self, porcento):
    return self.__valorHoraExtra + self.__valorHoraExtra * porcento/100


  def __str__(self):
    return "\n \n \n" +"Matrícula: " + str(self.__matricula) + "\n" + "Nome: " + self.__nome + "\n"  + "Data de Admissão:  "+ self.__dataAdmissao + "\n" +"Valor Horas normais: " + str(self.__valorHora) + "\n" +"Valor Horas Extras: "+ str(self.__valorHoraExtra) + "\n" +"Cargo: "+ self.__cargo + "\n" +"Status: "+ self.__status


#inputs
#iptM = int(input('Matriucula: '))
#iptNome = input('Digite seu nome: ')
#iptDataAdmissao = input('informe a data de admissão: ')
#iptCargo = input('Qual o seu cargo na empresa: ')
#iptStatus = input('Qual o status: ')
#iptValorH = float(input('Qual o valor da hora trabalhada: '))
#iptValorHX = float(input('Qual o valor da hora extra trabalhada: '))
iptQtdH = float(input('Quantas horas você trabalhou: '))
iptQtdHX = float(input('Quantas horas extras você trabalhou: '))


func1 = Funcionario(123, 'iptNome', 'iptCargo', 25, 30, 'iptCargo', 'iptStatus')

print("Salário: R$ " + str(func1.calculaSalario(iptQtdH)))
print("Horas Extras: R$ " + str(func1.calculaHExtra(iptQtdHX)))

iptReajuste = input('\n\nDeseja reajustar as horas Extras? ( S / N) ')
if iptReajuste == "S" or iptReajuste == "s":
  
  reajuste = int(input('Reajuste hora normal (%): '))
  reajusteExtra = int(input('Reajuste hora extra (%): '))
  
  print('------- Informações -------')
  print("\nReajuste realizado com sucesso! \n\n")
  print(f'{func1}' + "\n\n\n" + "Reajuste de Horas Normais: R$ " + str(func1.calculaReajuste(reajuste)) + "\n" + "Reajuste de Horas Extras: R$ " + str(func1.calculaReajusteExtra(reajusteExtra)) + '\n\n' )

else:
  print(func1)  