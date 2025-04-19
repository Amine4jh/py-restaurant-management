from Lists_Dicts import *

class Menu:
    def __init__(self, id_article, nom, description, prix, categorie):
        self._id_article = id_article
        self._nom = nom
        self._description = description
        self._prix = prix
        self._categorie = categorie

    def afficher_article(self):
        print(f'Id: {self._id_article}, Nom: {self._nom}, Description: {self._description} Prix; {self._prix}, Categorie: {self._categorie}.')