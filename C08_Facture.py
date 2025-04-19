from Lists_Dicts import *
bold_cyan = "\033[1;36m"
yellow = "\033[33m"
fin = "\033[0m"

class Facture:
    def __init__(self, id_facture, commande, ttc, ht, tva=0.2, fs=0.05):
        self._id_facture = id_facture
        self._commande = commande
        self._total_ht = ht
        self._tva = tva
        self._frais_service = fs
        self._total_ttc = ttc

    def afficher_facture(self):
        print(f'\n{yellow}########## Facture ##########{fin}')
        print(f'{yellow}- Facture id:{fin} {self._id_facture}')
        print(f'{yellow}- Commande id:{fin} {self._commande._id_commande}')
        print(f'{yellow}- Total hors taxes:{fin} {self._total_ht} dh')
        print(f'{yellow}- Frais services:{fin} {self._total_ht * self._frais_service:.2f} dh')
        print(f'{yellow}- TVA:{fin} {self._total_ht * self._tva:.2f} dh')
        print(f'{bold_cyan}- TTC: {self._total_ttc:.2f} dh{fin}')
        print(f'{yellow}#{fin}'*29)

    def calculer_total(self):
        self._total_ttc =  self._total_ht + (self._total_ht * self._tva) + (self._total_ht * self._frais_service)
        return f'TTC: {self._total_ttc}'