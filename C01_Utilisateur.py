from abc import ABC, abstractmethod

class Utilisateur(ABC):
    def __init__(self, nom, id_utilisateur, mot_de_passe, role):
        self._nom = nom
        self._id_utilisateur = id_utilisateur
        self._mot_de_passe = mot_de_passe
        self._role = role

    @abstractmethod
    def afficher_info(self):
        pass
    
    def modifier_le_mot_de_passe(self, nouveau_mot_de_passe):
        self._mot_de_passe = nouveau_mot_de_passe