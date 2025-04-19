from Lists_Dicts import *
import csv

class Authentification:
    def se_connecter(self, id_utilisateur, mot_de_passe):
        for role, user_list in users.items():
            for user in user_list:
                if id_utilisateur == user._id_utilisateur and mot_de_passe == user._mot_de_passe:
                    return user._role
        return False

    def se_deconnecter(self):
        pass