class ContaCorrente:
  def __init__ (self, nome, agencia, conta, saldo):
    self.__nome = nome
    self.__agencia = agencia
    self.__conta = conta
    self.__saldo = saldo

  def getNome(self):
    return self.__nome
  def setNome(self, nome):
    self.__nome = nome

  def getAgencia(self):
    return self.__agencia
  def setAgencia(self, agencia):
    self.__agencia = agencia

  def getConta(self):
    return self.__conta
  def setConta(self, conta):
    self.__conta = conta


  def getSaldo(self):
    return self.__saldo
  def setSaldo(self, saldo):
    self.__saldo = saldo



  def __str__(self):
    return "Nome: "+ str(self.__nome) +"\n" + "Agencia: " + str(self.__agencia) + "\n" +"Conta: "+ str(self.__conta) + "\n" +"Saldo: "+ str(self.__saldo)

################
obj1 = ContaCorrente('guilherme', 123, 123, 150)
print(obj1)
inptConta = obj1.setConta(int(input('Qual a conta: ')))######################
print (obj1.getConta())
print(obj1)
################