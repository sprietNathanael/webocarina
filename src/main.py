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
        print("7. Ajouter un type d'ocarina")
        print("8. Ajouter un interprète")
        print("9. Ajouter un type de média")
        print("10. Ajouter un media")
        print("11. Ajouter une occurence")
        print("12. Export vers CSV")
        print("13. Import depuis CSV")
        print("14. Type d'ocarina préféré d'un interprète")
        print("15. Interprête ayant le plus joué d'un Type d'ocarina")
        print("16. Type d'ocarina le plus utilisé pour un type de média")
        print("17. Type de media le plus joué avec un type d'ocarina")
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
            elif i == "7":
                try:
                    invite = "Entrez le nom : "
                    nom = (input(invite))
                    invite = "Entrez le nombre de trous : "
                    holes_nb = (input(invite))
                except KeyboardInterrupt:
                    pass
                except EOFError:
                    pass
                else:
                    try:
                        self.typeOcarina_orm.insert(nom, holes_nb)
                    except AttributeError:
                        print("Impossible d'enregistrer ce type d'ocarina")
            elif i == "8":
                try:
                    invite = "Entrez le nom : "
                    nom = (input(invite))
                except KeyboardInterrupt:
                    pass
                except EOFError:
                    pass
                else:
                    try:
                        self.performer_orm.insert(nom)
                    except AttributeError:
                        print("Impossible d'enregistrer cet interprète")
            elif i == "9":
                try:
                    invite = "Entrez le nom : "
                    nom = (input(invite))
                except KeyboardInterrupt:
                    pass
                except EOFError:
                    pass
                else:
                    try:
                        self.typeMedia_orm.insert(nom)
                    except AttributeError:
                        print("Impossible d'enregistrer ce type de média")
            elif i == "10":
                j = 0
                try:
                    invite = "Entrez le nom : "
                    nom = (input(invite))
                    invite = "Entrez la durée : "
                    length = (input(invite))
                    typeMediaArray = self.typeMedia_orm.findAll()
                    valid = False
                    while not valid:
                        j = 0
                        print("0 - Annuler")
                        for t in typeMediaArray:
                            j += 1
                            print("{} - {}".format(j, t.name))
                        invite = "Rentrez le type de média : "
                        typeMedia = (input(invite))
                        try:
                            if(int(typeMedia) < 0 or int(typeMedia) > j):
                                pass
                            else:
                                valid = True
                        except AttributeError:
                            pass
                except KeyboardInterrupt:
                    pass
                except EOFError:
                    pass
                else:
                    if(int(typeMedia) != 0):
                        try:
                            self.media_orm.insert(nom, length, typeMediaArray[int(typeMedia)-1].id_type_media)
                        except AttributeError:
                            print("Impossible d'enregistrer cet interprète")
                    else:
                        pass
            elif i == "11":
                j = 0
                try:
                    mediaArray = self.media_orm.findAll()
                    valid = False
                    while not valid:
                        j = 0
                        for t in mediaArray:
                            j += 1
                            print("{} - {}".format(j, t.name))
                        invite = "Rentrez le média : "
                        media = (input(invite))
                        try:
                            if(int(media) < 1 or int(media) > j):
                                pass
                            else:
                                valid = True
                        except AttributeError:
                            pass
                    typeOcarinaArray = self.typeOcarina_orm.findAll()
                    valid = False
                    while not valid:
                        j = 0
                        for t in typeOcarinaArray:
                            j += 1
                            print("{} - {}".format(j, t.name))
                        invite = "Rentrez le type d'ocarina : "
                        typeOcarina = (input(invite))
                        try:
                            if(int(typeOcarina) < 1 or int(typeOcarina) > j):
                                pass
                            else:
                                valid = True
                        except AttributeError:
                            pass
                    invite = "Entrez la durée : "
                    length = (input(invite))
                    invite = "Entrez un commentaire : "
                    comment = (input(invite))
                    performerArray = self.performer_orm.findAll()
                    valid = False
                    while not valid:
                        j = 0
                        for t in performerArray:
                            j += 1
                            print("{} - {}".format(j, t.name))
                        invite = "Rentrez l'interprète' : "
                        performer = (input(invite))
                        try:
                            if(int(performer) < 1 or int(performer) > j):
                                pass
                            else:
                                valid = True
                        except AttributeError:
                            pass
                except KeyboardInterrupt:
                    pass
                except EOFError:
                    pass
                else:
                    try:
                        self.occurrence_orm.insert(mediaArray[int(media)-1].id_media, typeOcarinaArray[int(typeOcarina)-1].id_type_ocarina, length, comment, performerArray[int(performer)-1].id_performer)
                    except AttributeError:
                        print("Impossible d'enregistrer cet interprète")
            elif i == "12":
                invite = "Entrez le fichier à enregistrer : "
                try:
                    path = (input(invite))
                except KeyboardInterrupt:
                    pass
                except EOFError:
                    pass
                else:
                    csv = ""
                    csv += self.typeOcarina_orm.toCSV() + "\n"
                    csv += self.typeMedia_orm.toCSV() + "\n"
                    csv += self.performer_orm.toCSV() + "\n"
                    csv += self.media_orm.toCSV() + "\n"
                    csv += self.occurrence_orm.toCSV()
                    try:
                        f = open(path, "w+")
                        f.write(csv)
                        f.close()
                    except IOError:
                        print("Impossible d'enregistrer le fichier ", path)
                    else:
                        print("Fichier ", path, "enregistré")
            elif i == "13":
                invite = "Entrez le fichier à ouvrir : "
                try:
                    path = (input(invite))
                except KeyboardInterrupt:
                    pass
                except EOFError:
                    pass
                else:
                    try:
                        f = open(path, "r")
                    except IOError:
                        print("Impossible d'ouvrir le fichier ", path)
                    line = f.readline()
                    while(line != "" and line != "\n"):
                            data = line.split(";")
                            try:
                                self.typeOcarina_orm.insert(data[0], data[1])
                                line = f.readline()
                            except AttributeError:
                                print("Impossible d'ouvrir le fichier ", path)
                    line = f.readline()
                    while(line != "" and line != "\n"):
                            try:
                                self.typeMedia_orm.insert(line)
                                line = f.readline()
                            except AttributeError:
                                print("Impossible d'ouvrir le fichier ", path)
                    line = f.readline()
                    while(line != "" and line != "\n"):
                            try:
                                self.performer_orm.insert(line)
                                line = f.readline()
                            except AttributeError:
                                print("Impossible d'ouvrir le fichier ", path)
                    line = f.readline()
                    while(line != "" and line != "\n"):
                            data = line.split(";")
                            try:
                                self.media_orm.insert(data[0], data[1], data[2])
                                line = f.readline()
                            except AttributeError:
                                print("Impossible d'ouvrir le fichier ", path)
                    line = f.readline()
                    while(line != "" and line != "\n"):
                            data = line.split(";")
                            try:
                                self.occurrence_orm.insert(data[0], data[1], data[2], data[3], data[4])
                                line = f.readline()
                            except AttributeError:
                                print("Impossible d'ouvrir le fichier ", path)            

                    f.close()
            elif i == "14":
                j = 0
                try:
                    performerArray = self.performer_orm.findAll()
                    valid = False
                    while not valid:
                        j = 0
                        for t in performerArray:
                            j += 1
                            print("{} - {}".format(j, t.name))
                        invite = "Rentrez l'interprète' : "
                        performer = (input(invite))
                        try:
                            if(int(performer) < 1 or int(performer) > j):
                                pass
                            else:
                                valid = True
                        except AttributeError:
                            pass
                except KeyboardInterrupt:
                    pass
                except EOFError:
                    pass
                else:
                    try:
                        print(self.performer_orm.getFavouriteTypeOcarina(performerArray[int(performer)-1].id_performer))
                    except TypeError:
                        print("Cet interprète n'a jamais joué d'ocarina")
            elif i == "15":
                j = 0
                try:
                    ocarinaArray = self.typeOcarina_orm.findAll()
                    valid = False
                    while not valid:
                        j = 0
                        for t in ocarinaArray:
                            j += 1
                            print("{} - {}".format(j, t.name))
                        invite = "Rentrez l'ocarina' : "
                        ocarina = (input(invite))
                        try:
                            if(int(ocarina) < 1 or int(ocarina) > j):
                                pass
                            else:
                                valid = True
                        except AttributeError:
                            pass
                except KeyboardInterrupt:
                    pass
                except EOFError:
                    pass
                else:
                    try:
                        print(self.typeOcarina_orm.getMaxPerformer(ocarinaArray[int(ocarina)-1].id_type_ocarina))
                    except TypeError:
                        print("Aucun interprète n'a joué de cet ocarina")
            elif i == "16":
                j = 0
                try:
                    typeMediaArray = self.typeMedia_orm.findAll()
                    valid = False
                    while not valid:
                        j = 0
                        print("0 - Annuler")
                        for t in typeMediaArray:
                            j += 1
                            print("{} - {}".format(j, t.name))
                        invite = "Rentrez le type de média : "
                        typeMedia = (input(invite))
                        try:
                            if(int(typeMedia) < 0 or int(typeMedia) > j):
                                pass
                            else:
                                valid = True
                        except AttributeError:
                            pass
                except KeyboardInterrupt:
                    pass
                except EOFError:
                    pass
                else:
                    try:
                        print(self.typeMedia_orm.getFavouriteTypeOcarina(typeMediaArray[int(typeMedia)-1].id_type_media))
                    except TypeError:
                        print("Ce type de média n'a jamais été joué à l'ocarina")
            elif i == "17":
                j = 0
                try:
                    typeOcarinaArray = self.typeOcarina_orm.findAll()
                    valid = False
                    while not valid:
                        j = 0
                        for t in typeOcarinaArray:
                            j += 1
                            print("{} - {}".format(j, t.name))
                        invite = "Rentrez le type d'ocarina : "
                        typeOcarina = (input(invite))
                        try:
                            if(int(typeOcarina) < 1 or int(typeOcarina) > j):
                                pass
                            else:
                                valid = True
                        except AttributeError:
                            pass
                except KeyboardInterrupt:
                    pass
                except EOFError:
                    pass
                else:
                    try:
                        print(self.typeOcarina_orm.getMaxTypeMedia(typeOcarinaArray[int(typeOcarina)-1].id_type_ocarina))
                    except TypeError:
                        print("Ce type d'ocarina n'a jamais été joué")
            elif i == "255":
                self.quitter()
            else:
                print("Votre choix est faux")

if __name__ == '__main__':
    myMain = Main()

