class Commande:
    def __init__(self, id_commande, reservation, statut):
        self._id_commande = id_commande
        self._reservation = reservation
        self._statut = statut
        self._articles = []

    def ajouter_article(self, article_menu):
        self._articles.append(article_menu)

    def afficher_commande(self):
        print(f'Id: {self._id_commande}, Reservation: {self._reservation}, Articles: {self._articles}, Statut: {self._statut}')

    def calculer_total(self, prix, tva = 0.2 ,fs = 0.05):
        total = prix + ( prix * fs ) + ( prix * tva )
        return total