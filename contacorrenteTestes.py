from time import sleep

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



  def deposito(self, valor):
    return self.__saldo + valor


  def saque(self, valor):
    return self.__saldo - valor

  def __str__(self):
    return "Nome: "+ self.__nome +"\n" + "Agencia: " + str(self.__agencia) + "\n" +"Conta: "+ str(self.__conta) + "\n" +"Saldo: "+ str(self.__saldo)

obj1 = ContaCorrente('Guilherme', 4568, 123987654, 0)
print("===== Informações =====\n")
print(obj1)
#sleep(2)



ipt = int(input('\n\nDigite 1 para SAQUE e 2 para DEPOSITO: '))
if ipt == 1:
  while True:
    iptSaque = float(input('\nDigite o valor do saque: '))
    print(f"\nSaldo atual: {obj1.saque(iptSaque)}")
    atualizaSaque = obj1.setSaldo(obj1.saque(iptSaque))
    aux = input('\n\n\nDeseja continuar sacando? (S / N) ')
    if aux.lower() != "s":
      break
elif ipt == 2:
  while True:
    iptDeposito = int(input("\nDigite o valor do depósito: "))
    print(f"\nSaldo atual: {obj1.deposito(iptDeposito)}")
    atualizaDep = obj1.setSaldo(obj1.deposito(iptDeposito))

    #sleep(0.5)
    aux = input('\n\n\nDeseja continuar depositando? (S / N) ')
    if aux.lower() != "s":
      break
    #aux = input('Deseja continuar depositando? (S / N) ')
    #if aux == "s" or aux == "S":
     # iptDeposito = int(input("\nDigite o valor do depósito: "))
      #print(f"\nSaldo atual: {obj1.deposito(iptDeposito)}")
      #atualizaDep = obj1.setSaldo(obj1.deposito(iptDeposito))     
   # elif aux == "N" or aux == 'n':  
     # print(obj1.getSaldo())
     # break
else:
  print("\nErro! Digite novamente a opção!")





