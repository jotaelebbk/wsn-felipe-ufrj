from csv import DictReader

with open('data.csv') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=' ') 
    for linha in leitor_csv:
        print( "%s" % "Data: {linha['Data']}  Hora: {linha['Hora']} Epoch: {linha['Epoch']} Moteid: {linha['Moteid']} Temperature: {linha['Temperature']} Humidity: {linha['Humidity']} Light: {linha['Light']} Voltage: {linha['Voltage']}")
