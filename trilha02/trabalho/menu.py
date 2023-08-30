import datetime
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


def saque(): 
    novo_saldo = conta.sacar(float(input('Valor do saque: R$ ')))
    if novo_saldo is not False:
        print("\n\n\nSaque realizado com sucesso!\n\n\n")
        return str(novo_saldo)
    else:
        print("\n\n\nSaldo insuficiente ou valor inválido para saque\n\n\n")
        return None  


def deposito():
    valor = float(input("Valor do deposito: R$ "))
    conta.setSaldo(conta.depositar(valor))






class ContaPoupanca(ContaBancaria):
    def __init__(self, nomeCliente, numConta, numAgencia, saldo, diaRendimento, taxaRendimento):
        super().__init__(nomeCliente, numConta, numAgencia, saldo)
        self.__diaRendimento = diaRendimento
        self.__taxaRendimento = taxaRendimento

    def getDiaDeRendimento(self):
        return self.__diaRendimento    
    def setDiaDeRendimento(self, diaRendimento):
        self.__diaRendimento = diaRendimento


    def getTaxaRendimento(self):
        return self.__taxaRendimento
    def setTaxaRendimento(self, taxa):
        self.__taxaRendimento = taxa    


    def calculaNovoSaldo(self):
        hoje = datetime.datetime.now().day
        if hoje == self.__diaRendimento:
            rendimento = self.getSaldo() * (self.__taxaRendimento / 100)
            self.setSaldo(self.getSaldo() + rendimento)
            return True
        return False

    def __str__(self):
        return super().__str__() + 'Dia de rendimento: ' + str(self.__diaRendimento) + ' ' + '\nTaxa de rendimento: ' + str(self.__taxaRendimento) 
    

contaPoupanca = ContaPoupanca('Célio', '51524481-5', 123, 150, 29, 0.5)

contaPoupanca.calculaNovoSaldo()


print('\n----Conta Poupanca---- ')
print(contaPoupanca)






class ContaEspecial(ContaBancaria):
    def __init__(self, nomeCliente, numConta, numAgencia, saldo, limite):
        super().__init__(nomeCliente, numConta, numAgencia, saldo)
        self.__limite = limite



    def getLimite(self):
        return self.__limite    
    def setLimite(self, limite):
        self.__limite = limite

    def sacarLim(self, valor):
        if self.getSaldo() + self.__limite >= valor and valor > 0:
            self.setSaldo(self.getSaldo() - valor)
            return self.getSaldo()
        else:
            print("\n\n\nSaldo insuficiente ou valor inválido para saque\n\n\n")
            return None


    def __str__(self):
        return super().__str__() + 'Limite: R$' + str(self.__limite)



contaEspecial = ContaEspecial('Célio', '51524481-5', 123, 2000, 1000)
contaEspecial.sacarLim(3000)

def opcao3():
    print('\n----Conta Especial---- ')
    print(contaEspecial)






def menu():
    selecao = int(input('\nSelecione a conta que deseja consultar: \n(1) Conta Padrão \n(2) Conta Poupança \n(3) Conta Especial \n(0) para sair do sistema\n\n ' ))
    if selecao == 1:
        print('\n----Conta Padrão----')
        print(conta)
        ipt1 = input('Digite (S) para saque ou (D) para depósito: ')
        if ipt1 == 'S' or ipt1 == 's':
            saque()
            print(conta)
        elif ipt1 == 'D' or ipt1 == 'd':
            deposito()
            print(conta)
        else:
            print('Opção inválida')   
    elif selecao == 2:
        import ContaPoupanca
        ContaPoupanca.opcao2() 
    elif selecao == 3:
        import ContaEspecial
        ContaEspecial.opcao3() 
    elif selecao == 0:
        print('Até Breve!!')
    else:
        print('Opção inválida!')    

if __name__ == '__main__':
    menu()    