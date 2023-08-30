from ContaBancaria import ContaBancaria


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