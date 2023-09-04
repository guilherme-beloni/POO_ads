from ContaBancaria import ContaBancaria
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
        return super().__str__() + 'Dia de rendimento: ' + str(self.__diaRendimento) + '/09/2023' +' ' + '\nTaxa de rendimento: ' + str(self.__taxaRendimento) + '% ' 




contaPoupanca = ContaPoupanca('João Antunes', '100000-5', 123, 150000, 10, 0.5)
contaPoupanca.calculaNovoSaldo()
def opcao2():
    print('\n----Conta Poupanca---- ')
    print(contaPoupanca)


opcao2()
ipt3 = input('\nDeseja alterar a data do dia de rendimento para teste? S / N: ')
if ipt3 == 'S' or ipt3 == 's':
    diaRendimento = int(input('Digite o dia de hoje: '))
    contaPoupanca.setDiaDeRendimento(diaRendimento)
    contaPoupanca.calculaNovoSaldo()
    print(contaPoupanca)
elif ipt3 == 'N' or ipt3 == 'n':
    print('Até logo!')    

