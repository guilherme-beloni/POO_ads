from heranca import Funcionario


class Gerente(Funcionario):
    def __init__(self, matricula, nome, dataAdmissao, valorHora, valorHoraExtra, cargo, status, valorAdc):
        super().__init__(matricula, nome, dataAdmissao, valorHora, valorHoraExtra, cargo, status)
        self.__valorAdc = valorAdc


    def getValorAdc(self):
        return self.__valorAdc
    def setValorAdc(self, valorAdc):
        self.__valorAdc = valorAdc 

    
    def __str__(self):
        return super().__str__() + 'Valor Adicional: ' + str(self.__valorAdc)