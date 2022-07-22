class App(object):

	print('Aplicacoes na WSN:\n')

	
        def __init__(self, AppID, sts, srs):    
		self.__AppID = AppID #App Identification
        	self.__sts = sts #Sensing unit
		self.__srs = srs #Sensing rate

		
app1 = (1, 'Voltage', 50)
print(app1)

app2 = (2, 'Humidity', 100)
print(app2)

app3 = (3, 'Temperature', 150)
print(app3)

app4 = (4, 'Light', 10)
print(app4)


