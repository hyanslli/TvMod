from prettytable import PrettyTable
class Tv:
    def __init__(self):
        self.start = False
        self.volume = 1
        self.channel = 1

    def onOff(self): # função para ligar/Desligar TV
        self.start = not self.start
        if self.start:
            print('Tv Ligada')
            self.info()
            return
        else:
            print('Desligando TV')

    def upVolume(self): # Função para aumentar o volume
        if self.start:
            if self.volume < 10:
                self.volume += 1
                print(f'Vol. {self.volume}')
                return
            
            if self.volume == 10:
                print('Vol. máximo')
                return
   
    def downVolume(self): # Função para diminuir o volume
        if self.start:
            if self.volume > 0:
                self.volume -= 1
                print(f'Vol. {self.volume}')
                return
            
            if self.volume == 0:
                print('Vol. mínimo')
                return
    
    def upChannel(self): # Função para aumentar o canal em 1
        if self.start:
            self.channel += 1
                
            if self.channel == 10:
                self.channel = 1
                
            self.info()                

    def downChannel(self): # Função para diminuir o canal em 1
        if self.start:
            self.channel -= 1

            if self.channel == 0:
                self.channel = 9
            
            self.info()
    
    def mute(self): # irá ser colocado nas funções do controle
        if self.start:
            mut = self.volume

            if not hasattr(self, 'mudo'):
                self.mudo = False  # Define 'mudo' como verdadeiro se ainda não estiver definido
            
            self.mudo = not self.mudo  # Inverte o valor de 'mudo'
            
            if self.mudo:
                self.volume = 0
                print('Tv mutada')
            else:
                self.volume = mut
                print('Tv desmutada')

    def levelChannel(self, canal): #pode ser colocado no controle
        if self.start:
            if canal > 0 and canal < 10:
                self.channel = canal
                self.info()
            

    def info(self):
        if self.start:
            info = PrettyTable()
            info.add_column('Get', ['Volume', 'Canal', 'Info'])
            info.add_column('Info', [self.volume, self.channel, self.infochannel()])
            info.align['Get'] = 'l'
            print(info)

    def infochannel(self):
        if self.channel == 1:
            return 'Você esta assistindo a Rede Globo'
        elif self.channel == 2:
            return 'Você esta assistindo a SBT'
        elif self.channel == 3:
            return 'Você esta assistindo a Record TV'
        elif self.channel == 4:
            return 'Você esta assistindo a Band Tv'
        elif self.channel == 5:
            return 'Você esta assistindo a Rede TV'
        elif self.channel == 6:
            return 'Você esta assistindo a Tv Cultura'
        elif self.channel == 7:
            return 'Você esta assistindo a TV Aparecida'
        elif self.channel == 8:
            return 'Você esta assistindo a TV Futura'
        else:
            return 'Você esta assistindo a TV Senado'
        