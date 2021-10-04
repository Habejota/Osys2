# Importando as dependencias
from os import system, chdir, mkdir, rmdir
from time import sleep
from socket import gethostname, gethostbyname

# Informações
__version__ = "1.0"
__tag_version__ = "Osys2 Beta"

# Ethernet and Socket informations
hostname = gethostname()
host = gethostbyname(hostname)

# Modulos e funções do OSys2
def clearDisplay():
    system("cls")


# Aplicativos



# Kernel
class kernel:
    def  __init__(self):
        clearDisplay()
        try: 
            self.db = open("home\config.log").read()
        except FileNotFoundError:
            try:
                mkdir("home")
            except FileExistsError:
                a = open("home\config.log", "wt+")
                print("Welcome to Osystem"), sleep(2)
                print("")
                print("here you can simule Linux in your Windows NT")
                print("Create your accont to use this sub-desktop")
                nsm = str(input("Username: ")).strip()
                a.write(nsm)
                a.close()
                del nsm
            else:
                a = open("home\config.log", "wt+")
                print("Welcome to Osystem"), sleep(2)
                print("")
                print("here you can simule Linux in your Windows NT")
                print("Create your accont to use this sub-desktop")
                nsm = str(input("Username: ")).strip()
                a.write(nsm)
                a.close()
                del nsm
            self.db = open("home\config.log").read()
        clearDisplay()
        self.inital_mensage()
        self.command_prompt()
        
        
    def command_prompt(self):
        while True:
            cmd: str = input("{}@{}:$ ".format(hostname, self.db))
    def inital_mensage(self):
        print("Welcome to Osystem Beta: {} - (Gnu\Linux {})".format(__version__, __tag_version__))
        print("")
        


# Executando
kernel()


