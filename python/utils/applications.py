
class Aplicacao():

    print('Programa que simula a chegada das aplicacoes')

    def __init__(self, appid, nome, tipo, requisito):
        self.__appid = appid
        self.__nome = nome
        self.__tipo = tipo
        self.__requisito = requisito

    def necessidade(self):

        return "%s" %  {self.__tipo} , {self.__requisito}

aplicacao1 = Aplicacao(1, 'Monitoracao', 'Light', 'Processamento')

aplicacao2 = Aplicacao(2, 'Monitoracao', 'Humidity', 'Memoria')

aplicacao3 = Aplicacao(3, 'Monitoracao', 'Temperature', 'Comunicacao')

aplicacao4 = Aplicacao(3, 'Monitoracao', 'Voltage', 'Processamento')

print(aplicacao1)

print(aplicacao1.__dict__)

print(aplicacao2.__dict__)

print(aplicacao3.__dict__)

print(aplicacao4.__dict__)

print('Necessidades das aplicacoes')

print(aplicacao1.necessidade())

print(aplicacao2.necessidade())

print(aplicacao3.necessidade())

print(aplicacao4.necessidade())


