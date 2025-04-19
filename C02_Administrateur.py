from Lists_Dicts import *
from C01_Utilisateur import Utilisateur
red = "\033[31m"
bold_cyan = "\033[1;36m"
fin = "\033[0m"

class Administrateur(Utilisateur):
    def __init__(self, nom, id_utilisateur, mot_de_passe, role):
        super().__init__(nom, id_utilisateur, mot_de_passe, role)

    def afficher_info(self):
        print(f'Administrateur: {self._nom}, ID: {self._id_utilisateur}, Mot de Passe: {self._mot_de_passe}')

    def gerer_utilisateurs(self, action, utilisateur, new_user_info = ''):
        if action == 'ajouter':
            try:
                for user in users[utilisateur._role]:
                    if utilisateur._id_utilisateur == user._id_utilisateur:
                        return f'{red}Utilisateur {utilisateur._id_utilisateur} est dèja existe.{fin}'
                users[utilisateur._role].append(utilisateur)
                return f'{bold_cyan}Utilisateur {utilisateur._id_utilisateur} est ajouté.{fin}'
            except:
                return f'{red}Le role saisi n\'est pas existe!{fin}'

        elif action == 'supprimer':
            if utilisateur._role == 'administrateur':
                if len(users['administrateur']) == 1:
                    return f'{red}Vous ne pouvez pas supprimer le seul administrateur existant{fin}'
            if utilisateur in users[utilisateur._role]:
                users[utilisateur._role].remove(utilisateur)
                return f'{bold_cyan}Utilisateur {utilisateur._nom} est supprimé.{fin}'
            return f'{red}Utilisateur {utilisateur._nom} n\'est pas existe!{fin}'

        elif action == 'modifier' or action == 'm':
            for i in users[utilisateur._role]:
                if i == utilisateur:
                    users[utilisateur._role][users[utilisateur._role].index(i)] = new_user_info
                    if new_user_info._role != utilisateur._role:
                        users[utilisateur._role].remove(new_user_info)
                        users[new_user_info._role].append(new_user_info)
                    return f'{bold_cyan}{utilisateur._nom} a ete modifier avec succès.{fin}'
            return f'{red}{utilisateur._nom} n\'est pas existe!{fin}'

    def gerer_menus(self, action, article_menu, new_article_menu = ''):
        if action == 'ajouter':
            menu.append(article_menu)
            return f'{article_menu._nom} a ete ajouter avec succès'
        
        elif action == 'supprimer':
            menu.remove(article_menu)
            return f'{article_menu._nom} a ete supprimer avec succès'
        
        elif action == 'modifier':
            for i in menu:
                if i == article_menu:
                    menu[menu.index(i)] = new_article_menu
                    if new_article_menu._nom != article_menu._nom:
                        menu.remove(new_article_menu)
                        menu.append(new_article_menu)
                    return f'{new_article_menu._nom} a ete modifier avec succès'
            return f'{new_article_menu._nom} n\'est pas existe'
        return 'Choix est invalable'