bold_cyan = "\033[1;36m"
fin = "\033[0m"

class Reservation:
    def __init__(self, id_reservation, nom_client, nombre_personnes, date_time, table):
        self._id_reservation = id_reservation
        self._nom_client = nom_client
        self._nombre_personnes = nombre_personnes
        self._date_time = date_time
        self._table = table

    def afficher_reservation(self):
        print(f'{bold_cyan}Reservation id {self._id_reservation}, de Mme/M. {self._nom_client}, {self._nombre_personnes} personnes, à {self._date_time}, table n° {self._table}{fin}')