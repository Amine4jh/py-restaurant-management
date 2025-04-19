from Lists_Dicts import *
from C01_Utilisateur import Utilisateur
bold_cyan = "\033[1;36m"
fin = "\033[0m"

class Serveur(Utilisateur):
    def __init__(self, nom, id_utilisateur, mot_de_passe, role):
        super().__init__(nom, id_utilisateur, mot_de_passe, role)

    def afficher_info(self):
        print(f"Serveur: {self._nom}, ID: {self._id_utilisateur}, Mot de Passe: {self._mot_de_passe}")

    def prendre_reservation(self, reservation):
        reservations.append(reservation)
        return '\nReservation a ete ajouter avec succes'

    def prendre_commande(self, commande):
        commandes.append(commande)
        return f'\n{bold_cyan}Commande a ete ajouter avec succes{fin}'

    def generer_facture(self, commande):
        if commande not in factures:
            factures.append(commande)
        

    def consulter_reservations(self):
        for reservation in reservations:
            print(f'Reservation id {reservation._id_reservation}, de Mme/M. {reservation._nom_client}, {reservation._nombre_personnes} personnes, à {reservation._date_time}, table n° {reservation._table}')

    def consulter_commandes(self):
        for commande in commandes:
            print(f'Id: {commande._id_commande}, Statut: {commande._statut}')