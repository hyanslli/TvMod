class Tv:
    def __init__(self, volume, start, channel):
        self.start = False
        self.volume = 10
        self.channel = 001

    def onOff(self, start):
        if start:
            start = False
            return
        else:
            start = True
            return
        
    def levelVolume(self, start, volume):
        if start:
           pass #precisa encontrar um meio de como irá chamar os funções aumentar/diminuir

    def upVolume(self, volume):
        if volume < 100:
            up = volume + 1
            return up
    
    def mute(self, volume): # irá ser colocado nas funções do controle
        pass
    
    def downVolume(self, volume):
        if volume > 0:
            down = volume - 1
            return down
        
    def levelChannel(self, start, channel): #pode ser colocado no controle
        if start:
            pass
    
    def upChannel(self, channel):
        if channel > 000:
            up = channel - 1
            return up
    
    def downChannel(self, channel):
        if channel > 100:
            down = channel - 1
            return down