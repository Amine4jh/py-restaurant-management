from C01_Utilisateur import Utilisateur
from C02_Administrateur import Administrateur
from C03_Serveur import Serveur
from C04_ChefDeCuisine import ChefDeCuisine
from C05_Menu import Menu
from C06_Reservation import Reservation
from C07_Commande import Commande
from C08_Facture import Facture
from C09_Table import Table
from C10_GestionFichier import GestionFichier
from C11_Authentification import Authentification
from C12_CalculateurFinancier import CalculateurFinancier
from Lists_Dicts import *
from types import SimpleNamespace
from datetime import datetime
import csv
import maskpass

# Normal Colors
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
magenta = "\033[35m"

# Bold colors
bold_yellow = "\033[1;33m"
bold_cyan = "\033[1;36m"
bold_blue = "\033[1;34m"

# BackGround Colors
bg_white = "\033[47m"

# Turn off Color
fin = "\033[0m"

def save_data_from_csv(nom_fichier, liste, object_type=SimpleNamespace):
    with open(nom_fichier, 'r', encoding='UTF8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for ligne in reader:
            if object_type == SimpleNamespace:
                user_object = SimpleNamespace(**ligne)
            else:
                user_object = object_type(**ligne)
            liste.append(user_object)

def save_data_from_lists(nom_fichier, liste):
    with open(nom_fichier, 'w', newline='', encoding='UTF8') as file:
        if len(liste) > 0:
            if isinstance(liste[0], dict):
                fieldnames = liste[0].keys()
            else:
                fieldnames = liste[0].__dict__.keys()
            writer = csv.DictWriter(file, delimiter=';', fieldnames=fieldnames)
            writer.writeheader()
            for user in liste:
                if isinstance(user, dict):
                    user_dict = user
                else:
                    user_dict = user.__dict__
                writer.writerow(user_dict)
        else:
            file.write("")

def save_users_from_csv(nom_fichier, users):
    with open(nom_fichier, 'r', encoding='UTF8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for ligne in reader:
            obj = SimpleNamespace(**ligne)
            role = ligne.get('_role', '').lower()
            if role in users:
                users[role].append(obj)

def save_users_from_lists(nom_fichier, liste):
    for k, v in liste.items():
        filename = f'Users_Data/{k}.csv'
        with open(filename, 'w', newline='', encoding='UTF8') as file:
            if len(v) > 0:
                fieldnames = v[0].__dict__.keys()
                writer = csv.DictWriter(file, delimiter=';', fieldnames=fieldnames)
                writer.writeheader()
                for user in v:
                    writer.writerow(user.__dict__)
            else:
                file.write("")


authentification = Authentification()
gestionFichier = GestionFichier()
admin = Administrateur('Amine', 'amine', '0000', 'administrateur')
serveur = Serveur('0', '0', '0', 'serveur')
chef = ChefDeCuisine('0', '0', '0', 'chef')
save_users_from_csv('Users_Data/administrateur.csv', users)
save_users_from_csv('Users_Data/serveur.csv', users)
save_users_from_csv('Users_Data/chef.csv', users)
save_data_from_csv('Object_Data/menu.csv', menu)
save_data_from_csv('Object_Data/reservation.csv', reservations)
save_data_from_csv('Object_Data/commande.csv', commandes)
save_data_from_csv('Object_Data/facture.csv', factures)

def connexion():
    print(f'\n{bg_white}##############{fin} {bold_cyan}Connectez Vous!{fin} {bg_white}##############{fin}')
    util = input(f'\n{bold_blue}- Identifiant: {fin}')
    mopa = maskpass.askpass(prompt=f'{bold_blue}- Mot De Passe: {fin}', mask='*')
    print('')
    print(f'{bg_white}#{fin}' * 45)
    if authentification.se_connecter(util, mopa) == 'administrateur':
        admin_menu()
    elif authentification.se_connecter(util, mopa) == 'serveur':
        serveur_menu()
    elif authentification.se_connecter(util, mopa) == 'chef':
        chef_menu()
    else:
        print(f'{red}Mot de Passe ou Id d\'Utilisateur est Incorrecte.{fin}')
        mdp_incorrecte()
                
def mdp_incorrecte():
    choix = 1
    while choix != 0:
        print(f'\n{green}1- Essayez une autre fois.{fin}')
        print(f'{red}0- Quitter{fin}')
        try:
            choix = int(input(f'{blue}- Saisir votre choix: {fin}'))
        except:
            print(f'{red}Vous devez entrer un numéro!{fin}')
            mdp_incorrecte()
            return
        if choix == 1:
            connexion()
            return
        elif choix == 0:
            print(f'\n{magenta}Au Revoir!{fin}\n')
            return
        else:
            print(f'{red}Choix incorrecte{fin}')
            mdp_incorrecte()
            return

def se_deconnecter():
    choix = 1
    while choix != 0:
        print(f'{green}1- Connecter{fin}')
        print(f'{red}0- Quitter{fin}')
        try:
            choix = int(input(f'{blue}- Saisir votre choix: {fin}'))
        except:
            print(f'{red}Vous devez entrer un numéro!{fin}')
            mdp_incorrecte()
            return
        if choix == 1:
            connexion()
            return
        elif choix == 0:
            print(f'\n{magenta}Au Revoir!{fin}\n')
            return
        else:
            print(f'{red}Choix est incorrecte.{fin}')

def admin_menu():
    choix = 1
    while choix != 0:
        print(f'\n{"#"*15} {bold_yellow}Bienvenue Administrateur!{fin} {"#"*15}')
        print(f'{green}1- Ajouter un utilisateur{fin}')
        print(f'{green}2- Modifier un utilisateur{fin}')
        print(f'{green}3- Supprimer un utilisateur{fin}')
        print(f'{green}4- Ajouter un article de menu{fin}')
        print(f'{green}5- Modifier un article de menu{fin}')
        print(f'{green}6- Supprimer un article de menu{fin}')
        print(f'{red}0- Decconecter{fin}')
        try:
            choix = int(input(f'\n{blue}- Saisir votre choix: {fin}'))
        except:
            print(f'{red}Vous devez entrer un numéro!{fin}')
            admin_menu()
            return
        print(f'{"#" * 57}\n')

        if choix == 1:
            nom = str(input('Saisir le nom d\'utilisateur: ').capitalize().strip())
            id_u = str(input('Saisir l\'identifiant: ').lower().strip())
            mdp = str(input('Saisir le mot de passe: '))
            role = str(input('Choisir le role (administrateur, serveur ou chef): ').lower().strip())
            user = Administrateur(nom, id_u, mdp, role)
            print(admin.gerer_utilisateurs('ajouter', user))

        elif choix == 2:
            user_type = input(f'Modifier Administrateur {bold_cyan}(A){fin}, Serveur {bold_cyan}(S){fin} ou Chef {bold_cyan}(C){fin}: ').capitalize().strip()
            if user_type == 'A' or user_type == 'Administrateur':
                if users['administrateur'] == []:
                    print(f'{red}Il y a aucun administrateur!{fin}')
                else:
                    for i in users['administrateur']:
                        print(i._id_utilisateur)
                    mod_user = input('Entrer l\'identifiant: ').lower().strip()
                    for i in users['administrateur']:
                        if mod_user == i._id_utilisateur:
                            try:
                                print(f'{yellow}=== Entrer les nouveaux informations ==={fin}')
                                nom = str(input('Saisir le nom d\'utilisateur: ').capitalize().strip())
                                id_u = str(input('Saisir l\'identifiant: ').lower().strip())
                                mdp = str(input('Saisir le mot de passe: '))
                                role = str(input('Choisir le role (administrateur, serveur ou chef): ').lower().strip())
                                user = ChefDeCuisine(nom, id_u, mdp, role)
                                print(admin.gerer_utilisateurs('m', i, user))
                            except:
                                print(f'{red}Le role saisi n\'est pas existe!{fin}')
                            break
                    else:
                        print(f'{red}L\'identifiant saisi est incorrect!{fin}')
            
            elif user_type == 'S' or user_type == 'Serveur':
                if users['serveur'] == []:
                    print(f'{red}Il y a aucun serveur!{fin}')
                else:
                    for i in users['serveur']:
                        print(i._id_utilisateur)
                    mod_user = input('Entrer l\'identifiant: ').lower().strip()
                    for i in users['serveur']:
                        if mod_user == i._id_utilisateur:
                            try:
                                print(f'{yellow}=== Entrer les nouveaux informations ==={fin}')
                                nom = str(input('Saisir le nom d\'utilisateur: ').capitalize().strip())
                                id_u = str(input('Saisir l\'identifiant: ').lower().strip())
                                mdp = str(input('Saisir le mot de passe: '))
                                role = str(input('Choisir le role (administrateur, serveur ou chef): ').lower().strip())
                                user = ChefDeCuisine(nom, id_u, mdp, role)
                                print(admin.gerer_utilisateurs('m', i, user))
                            except:
                                print(f'{red}Le role saisi n\'est pas existe!{fin}')
                            break
                    else:
                        print(f'{red}L\'identifiant saisi est incorrect!{fin}')
            
            elif user_type == 'C' or user_type == 'Chef':
                if users['chef'] == []:
                    print(f'{red}Il y a aucun chef!{fin}')
                else:
                    for i in users['chef']:
                        print(i._id_utilisateur)
                    mod_user = input('Entrer l\'identifiant: ').lower().strip()
                    for i in users['chef']:
                        if mod_user == i._id_utilisateur:
                            try:
                                print(f'{yellow}=== Entrer les nouveaux informations ==={fin}')
                                nom = str(input('Saisir le nom d\'utilisateur: ').capitalize().strip())
                                id_u = str(input('Saisir l\'identifiant: ').lower().strip())
                                mdp = str(input('Saisir le mot de passe: '))
                                role = str(input('Choisir le role (administrateur, serveur ou chef): ').lower().strip())
                                user = ChefDeCuisine(nom, id_u, mdp, role)
                                print(admin.gerer_utilisateurs('m', i, user))
                            except:
                                print(f'{red}Le role saisi n\'est pas existe!{fin}')
                            break
                    else:
                        print(f'{red}L\'identifiant saisi est incorrect!{fin}')
            else:
                print(f'{red}Le role saisi n\'est pas existe!{fin}')

        elif choix == 3:
            for role, user_list in users.items():
                for user in user_list:
                    print(f'{user._id_utilisateur}, {bold_cyan}({user._role}){fin}')
            user_id = input('Entrez l\'id d\'utilisateur: ')
            found = False
            for role, user_list in users.items():
                for user in user_list:
                    if user_id == user._id_utilisateur:
                        print(admin.gerer_utilisateurs('supprimer', user))
                        found = True
                        break
                if found:
                    break
            if not found:
                print(f'{red}L\'identifiant saisi n\'est pas existe!{fin}')

        elif choix == 4:
            id_art = input('Saisir l\'id de l\'article: ')
            nom_menu = input('Saisir le nom de l\'article: ')
            desc = input('Decrire l\'article: ')
            prix = int(input('Saisir le prix de l\'article: '))
            categ = input('Choisir la categorie (entree, plat, dessert, boisson): ')
            menu_1 = Menu(id_art, nom_menu, desc, prix, categ)
            print(admin.gerer_menus('ajouter', menu_1))

        elif choix == 5:
            if not menu:
                print('Le Menu est vide.')
            else:
                for i in menu:
                    print(f'{i._id_article}- {i._nom}')
                menu_nom = input('Choisir un article menu par son id: ')
                for i in menu:
                    if menu_nom == i._id_article:
                        n_id_art = input('Saisir l\'id de l\'article: ')
                        n_nom_menu = input('Saisir le nom de l\'article: ')
                        n_desc = input('Decrire l\'article: ')
                        n_prix = input('Saisir le prix de l\'article: ')
                        n_categ = input('Choisir la categorie (entree, plat, dessert, boisson): ')
                        menu_2 = Menu(n_id_art, n_nom_menu, n_desc, n_prix, n_categ)
                        print(admin.gerer_menus('modifier', i, menu_2))

        elif choix == 6:
            if not menu:
                print('Le menu est vide.')
            else:
                for i in menu:
                    print(f'{i._id_article}- {i._nom}')
                menu_nom = input('Choisir un article menu par son id: ')
                for i in menu:
                    if menu_nom == i._id_article:
                        print(admin.gerer_menus('supprimer', i))
                        break

        elif choix == 0:
            save_users_from_lists('Users_Datausers_object.csv', users)
            save_data_from_lists('Object_Data/menu.csv', menu)
            se_deconnecter()

        else:
            print(f'{red}Choix est incorrecte.{fin}')

def serveur_menu():
    choix = 1
    while choix != 0:
        print(f'\n{"#"*15} {bold_yellow}Bienvenue Serveur!{fin} {"#"*15}')
        print(f'{green}1- Prendre des reservations{fin}')
        print(f'{green}2- Prendre des commandes{fin}')
        print(f'{green}3- Gerer facture{fin}')
        print(f'{green}4- Consulter reservation{fin}')
        print(f'{green}5- Consulter commande{fin}')
        print(f'{red}0- Decconecter{fin}')
        try:
            choix = int(input(f'\n{blue}- Saisir votre choix: {fin}'))
        except:
            print(f'{red}Vous devez entrer un numéro!{fin}')
            serveur_menu()
            return
        print(f'{"#" * 50}\n')

        if choix == 1:
            id_res = input('Saisir l\'id de reservation: ').strip()
            nom_client = input('Saisir le nom de client: ').capitalize().strip()
            nombre = input('Saisir le nombre des personnes: ').strip()
            while True:
                date = input("Saisir la date (DD-MM-YYYY HH:MM): ")
                try:
                    datetime_obj = datetime.strptime(date, "%d-%m-%Y %H:%M")
                    break
                except:
                    print("Invalid date format. Please use the format DD-MM-YYYY HH:MM.")
            table = input('Saisir le numero de la table: ').strip()
            reservation = Reservation(id_res, nom_client, nombre, datetime_obj, table)
            print(serveur.prendre_reservation(reservation))
            reservation.afficher_reservation()

        elif choix == 2:
            if reservations:
                id_com = input('Saisir l\'id de Commande: ')
                print('++ Resrvations ++')
                for i in reservations:
                    print(i._id_reservation, i._nom_client)
                print('+'*17)
                res = input('Choisir une reservation par son Id: ')
                for i in reservations:
                    if res == i._id_reservation:
                        commande = Commande(id_com, i, 'en attente')
                print(f'\n{yellow}++++++++ Menu ++++++++{fin}')
                for i in menu:
                    print(f'{yellow}{i._id_article}-{fin} {i._nom} : {i._prix} dh')
                print(f'{yellow}+{fin}'*22)
                article_id = input('Choisir l\'article par son Id: ')
                n = int(input('Nombre: '))
                for i in menu:
                    if article_id == i._id_article:
                        for x in range(n):
                            commande.ajouter_article(i)
                ch = 1
                while ch != 0:
                    print('\n1- Ajouter quelque chose d\'autre')
                    print('0- Terminer')
                    try:
                        ch = int(input('Saisir votre choix: '))
                        if ch == 1:
                            print(f'\n{yellow}++++++++ Menu ++++++++{fin}')
                            for i in menu:
                                print(f'{yellow}{i._id_article}-{fin} {i._nom} : {i._prix} dh')
                            print(f'{yellow}+{fin}'*22)
                            article_id = input('Choisir l\'article par son Id: ')
                            n = int(input('Nombre: '))
                            for i in menu:
                                if article_id == i._id_article:
                                    for x in range(n):
                                        commande.ajouter_article(i)
                    except:
                        print(f'{red}Vous devez entrer un numéro!{fin}')
                if commande._articles:
                    print(serveur.prendre_commande(commande))
            else:
                print(f'{red}Il y a aucun reservation!{fin}')

        elif choix == 3:
            try:
                if commandes:
                    id_fac = input('Saisir l\'id de facture: ')
                    print('== Commandes ==')
                    for c in commandes:
                        print(c._id_commande)
                    print('='*15)
                    com = input('Choisir l\'Id de commande: ')
                    for c in commandes:
                        if com == c._id_commande:
                            total_ht = 0
                            for i in c._articles:
                                total_ht += int(i._prix)
                    facture = Facture(id_fac, c, 0,total_ht)
                    facture.calculer_total()
                    facture.afficher_facture()
                    serveur.generer_facture(facture)
                else:
                    print(f'{red}Il y a aucun commande!{fin}')
            except:
                print(f'{red}Cette facture est deja payé!{fin}')

        elif choix == 4:
            serveur.consulter_reservations()

        elif choix == 5:
            serveur.consulter_commandes()

        elif choix == 0:
            save_data_from_lists('Object_Data/reservation.csv', reservations)
            save_data_from_lists('Object_Data/commande.csv', commandes)
            save_data_from_lists('Object_Data/facture.csv', factures)
            se_deconnecter()

        else:
            print(f'{red}Choix est incorrecte.{fin}')

def chef_menu():
    choix = 1
    while choix != 0:
        print(f'\n{"#"*15} {bold_yellow}Bienvenue Chef!{fin} {"#"*15}')
        print(f'{green}1- Consulter commande{fin}')
        print(f'{green}2- Mettre a jour statut de commande{fin}')
        print(f'{red}0- Decconecter{fin}')
        try:
            choix = int(input(f'\n{blue}- Saisir votre choix: {fin}'))
        except:
            print(f'{red}Vous devez entrer un numéro!{fin}')
            chef_menu()
            return
        print(f'{"#" * 47}\n')

        if choix == 1:
            print(f'{yellow}=== Commandes en cours ==={fin}')
            chef.consulter_commandes()
            print(f'{yellow}={fin}'*26)

        elif choix == 2:
            print(f'{yellow}=== Commandes en cours ==={fin}')
            chef.consulter_commandes()
            print(f'{yellow}={fin}'*26)
            com_id = input('Choisir commande par son Id: ')
            N_statut = input('Choisir la nouvelle statut (en preparation ou pret): ')
            for commande in commandes:
                if com_id == commande._id_commande:
                    print(chef.mettre_a_jour_statut_commande(commande, N_statut))

        elif choix == 0:
            save_data_from_lists('Object_Data/commande.csv', commandes)
            se_deconnecter()

        else:
            print(f'{red}Choix est incorrecte.{fin}')

connexion()