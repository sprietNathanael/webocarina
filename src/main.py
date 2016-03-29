# -*-coding:UTF-8 -*


class Main(object):
    """docstring for Main"""
    def __init__(self,):
        while True:
            self.afficherMenu()
            self.validerMenu()

    def afficherMenu(self):
        print("1. Bonjour")
        print("2. Quitter")

    def quitter(self):
        print("Merci d'avoir utilisé notre programme !")
        quit()

    def validerMenu(self):
        invite = "Faites votre choix : "
        try:
            i = (input(invite))
        except KeyboardInterrupt:
            print("\nPour quitter, faites le choix 2")
        except EOFError:
            print("\nPour quitter, faites le choix 2")
        else:
            if i == "1":
                print("Bonjour !\n")
            elif i == "2":
                self.quitter()
            else:
                print("Votre choix est faux")

if __name__ == '__main__':
    myMain = Main()
