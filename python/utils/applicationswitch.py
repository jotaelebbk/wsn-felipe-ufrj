from threading import Thread

class applicationSwitch():
    
    print('Programa que simula a chegada das aplicacoes na rede')

   
#Thread que escreve os dados escutados na console.

    #private baseStationListener escutarBS = new baseStationListener();
    #private Thread baseStation = new Thread(escutarBS);

    
#Switchs que servem para dar o input das aplicacoes
    
    #private ISwitch sw1 = (ISwitch)Resources.lookup(ISwitch.class, "SW1");
    #private ISwitch sw2 = (ISwitch)Resources.lookup(ISwitch.class, "SW2");
    #private ILightSensor light = (ILightSensor) Resources.lookup(ILightSensor.class);
    
  
#Representam as aplicacoes que devem rodar na rede

    application1 = False
    application2 = False

    APP_VECTOR = 'V'
    START = 'S'
     
    

    
    def startApp():
        
 	print('Base Station do Shared Leach Ligada')
        enviarStart()
    
   

    def enviarStart():
        print('enviar start')


    
    def pauseApp():
        pass
    

    def destroyApp():
        pass

    
    def inserirAplicacoesNaRede():
        pass



class escutarBS(Thread): #baseStationListener

                def __init__ (self, num):
                      Thread.__init__(self)
                      self.num = num

                def run(self):

                      print "Hello "
                      print self.num


a = escutarBS(10)
a.start()
    
    

