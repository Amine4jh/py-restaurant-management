class CalculateurFinancier:
    def calculer_tva(montant, taux = 0.20):
        total = montant + (montant * taux)
        return total

    def calculer_frais_services(montant, taux=0.5):
        total = montant + (montant * taux)
        return total