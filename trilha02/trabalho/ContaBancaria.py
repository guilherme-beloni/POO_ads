class ContaBancaria:
    def __init__(self, nomeCliente, numConta, numAgencia, saldo):
        self.__nomeCliente = nomeCliente
        self.__numConta = numConta
        self.__numAgencia = numAgencia
        self.__saldo = saldo

    def getNomeCliente(self):
        return self.__nomeCliente
    def setNomeCliente(self, nomeCliente):
        self.__nomeCliente = nomeCliente

    def getNumConta(self):
        return self.__numConta
    def setNumConta(self, numConta):
        self.__numConta = numConta

    def getNumAgencia(self):
        return self.__numAgencia
    def setNumAgencia(self, numAgencia):
        self.__numAgencia = numAgencia

    def getSaldo(self):
        return self.__saldo
    def setSaldo(self, saldo):
        self.__saldo = saldo    

    def sacar(self, valor): 
        if self.__saldo >= valor and valor > 0:
            self.__saldo = self.__saldo - valor
            return 'R$ ' + str(self.__saldo)
        else:
            return False
        #return self.__saldo - valor 
    
    def depositar(self, valor):
        return self.__saldo + valor
             

    def __str__(self):
        return "\nNome: " + self.__nomeCliente+ "\nConta: " + str(self.__numConta) + "\nAgencia: " + str(self.__numAgencia) + "\nSaldo: R$" + str(self.__saldo) + '\n'



conta = ContaBancaria('Célio', '51524481-5', 123, 0)  
print(conta)
#sacar
def saque(): 
    novo_saldo = conta.sacar(float(input('Valor do saque: R$ ')))
    if novo_saldo is not False:
        print("\n\n\nSaque realizado com sucesso!\n\n\n")
        return str(novo_saldo)
    else:
        print("\n\n\nSaldo insuficiente ou valor inválido para saque\n\n\n")
        return None  

#depositar
def deposito():
    valor = float(input("Valor do deposito: R$ "))
    conta.setSaldo(conta.depositar(valor))




