# -*-coding:UTF-8 -*

from controlers import *


class Main(object):
    """docstring for Main"""
    def __init__(self,):
        self.typeOcarina_orm = TypeOcarinaORM()
        self.typeMedia_orm = TypeMediaORM()
        self.performer_orm = PerformerORM()
        self.media_orm = MediaORM()
        self.occurrence_orm = OccurrenceORM()
        while True:
            self.afficherMenu()
            self.validerMenu()

    def afficherMenu(self):
        print("1. Bonjour")
        print("2. Afficher tous les types d'ocarina")
        print("3. Afficher tous les interprètes")
        print("4. Afficher tous les types de médias")
        print("5. Afficher tous les médias")
        print("6. Afficher toutes les occurrences")
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
                print(self.typeOcarina_orm)
            elif i == "3":
                print(self.performer_orm)
            elif i == "4":
                print(self.typeMedia_orm)
            elif i == "5":
                print(self.media_orm)
            elif i == "6":
                print(self.occurrence_orm)
            elif i == "255":
                self.quitter()
            else:
                print("Votre choix est faux")

if __name__ == '__main__':
    myMain = Main()

