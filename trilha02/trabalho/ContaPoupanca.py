from menu import ContaBancaria
import datetime


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

def opcao2():
    print('\n----Conta Poupanca---- ')
    print(contaPoupanca)
