from Lists_Dicts import *

class Table:
    def __init__(self, numero_table, capacite):
        self._numero_table = numero_table
        self._capacite = capacite
        self._est_ocupee = True

    def afficher_info_table(self):
        print(f'Capacite: {self._capacite}, N° Table: {self._numero_table}')

    def occuper_table(self):
        if self._est_ocupee == False:
            self._est_ocupee = True
            return 'Table est occupée.'
        return 'Table est deja libre.'

    def liberer_table(self):
        if self._est_ocupee == True:
            self._est_ocupee = False
            return 'Table est libre'
        return 'Table est deja occupée.'