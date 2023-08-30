from heranca import Funcionario
from gerente import Gerente



bjF = Funcionario(125, 'Paulo', '28/12/1996', 30, 25.36, 'ADM', 'Ativo')
print(bjF.getNome() + ':  ' + str(bjF.calculaSalario(10)))


bjG = Gerente(123, 'John', '25/08/1995', 35, 35.98, 'CO', 'Ativo', 100)
print(bjG.getNome() + ':  ' + str(bjG.calculaSalario(10)))