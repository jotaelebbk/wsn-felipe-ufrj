class Sensor(object):

	print('Estrutura dos sensores')

	
        def __init__(self, NodeID, Sts, Srs):    
		self.__NodeID = NodeID #Identificador do node
        	self.__Sts = Sts #Sensing unit
		self.__Srs = Srs #Sensing rate
  		

sensor1 = (1, 'Light', 100)
print(sensor1)

sensor2 = (2, 'Humidity', 100)
print(sensor2)

sensor3 = (3, 'Temperature', 100)
print(sensor3)

sensor4 = (4, 'Voltage', 10)
print(sensor4)
