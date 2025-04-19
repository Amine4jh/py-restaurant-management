import csv

class GestionFichier:
    def lire_fichier(self, nom_fichier):
        with open(nom_fichier, 'r') as file:
            lecteurCSV = csv.DictReader(file, delimiter=";")
            for ligne in lecteurCSV:
                return ligne

    def ecrire_fichier(self, nom_fichier, contenu):
        with open(nom_fichier, 'r') as file:
            lecteurCSV = csv.reader(file, delimiter=';')
            for ligne in lecteurCSV:
                if contenu == ligne:
                    return
        with open(nom_fichier, 'a', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(contenu)

    def chercher_dans_fichier(self, nom_fichier ,critere):
        with open(nom_fichier, 'r') as file:
            lecteurCSV = csv.reader(file, delimiter=';')
            for ligne in lecteurCSV:
                if critere in ligne:
                    return f'{critere} dans ligne: {ligne}'