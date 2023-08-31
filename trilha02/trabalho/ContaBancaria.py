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










def menu():
    selecao = int(input('\nSelecione a conta que deseja consultar: \n(1) Conta Corrente \n(2) Conta Poupança \n(3) Conta Especial \n(0) Sair do sistema\n\n ' ))
    if selecao == 1:
        print('\n----Conta Corrente----')
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
        ipt2 = input('\nDigite (C) para consultar ou (S) para sair:')
        if ipt2 == 'C' or ipt2 == 'c':
            import ContaPoupanca
            ContaPoupanca.opcao2()
        elif ipt2 == 'S' or ipt2 == 's':
            print('Até Breve!!')
    elif selecao == 3:
        ipt3 = input('\nDigite (C) para consultar ou (S) para sair:')
        if ipt3 == 'C' or ipt3 =='c':
            import ContaEspecial
            ContaEspecial.opcao3() 
    elif selecao == 0:
        print('Até Breve!!')
    else:
        print('Opção inválida!')    

if __name__ == '__main__':
    menu()    