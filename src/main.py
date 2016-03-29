# -*-coding:UTF-8 -*

from sqlalchemy.ext.declarative import declarative_base
from typeOcarinaORM import TypeOcarinaORM


class Main(object):
    """docstring for Main"""
    def __init__(self,):
        self.typeOcarina_orm = TypeOcarinaORM()
        while True:
            self.afficherMenu()
            self.validerMenu()

    def afficherMenu(self):
        print("1. Bonjour")
        print("2. Afficher tous les types d'ocarina")
        print("255. Quitter")

    def quitter(self):
        print("Merci d'avoir utilisé notre programme !")
        quit()

    def validerMenu(self):
        invite = "Faites votre choix : "
        try:
            i = (input(invite))
        except KeyboardInterrupt:
            print("\nPour quitter, faites le choix 255")
        except EOFError:
            print("\nPour quitter, faites le choix 255")
        else:
            if i == "1":
                print("Bonjour !\n")
            elif i == "2":
                print(self.typeOcarina_orm.typeList())
            elif i == "255":
                self.quitter()
            else:
                print("Votre choix est faux")

if __name__ == '__main__':
    myMain = Main()

