from Lists_Dicts import *
from C01_Utilisateur import Utilisateur

class ChefDeCuisine(Utilisateur):
    def __init__(self, nom, id_utilisateur, mot_de_passe, role):
        super().__init__(nom, id_utilisateur, mot_de_passe, role)

    def afficher_info(self):
        print(f"Serveur: {self._nom}, ID: {self._id_utilisateur}, Mot de Passe: {self._mot_de_passe}")

    def consulter_commandes(self):
        for c in commandes:
            if c._statut != 'pret':
                print(f'{c._id_commande}- {c._statut}')

    def mettre_a_jour_statut_commande(self, commande, statut):
        if commande._statut == 'pret':
            return f'Commande {commande._id_commande} est deja pret.'
        else:
            if statut == 'pret':
                commande._statut = 'pret'
                return f'Commande {commande._id_commande} est {statut}.'
            elif statut == 'en preparation':
                commande._statut = 'en preparation'
                return f'Commande {commande._id_commande} est {statut}.'
            else:
                return 'Statut unavailable.'