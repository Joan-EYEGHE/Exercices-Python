
garde_robe = {"creme": 2, "Crocs": 1}


def afficherGardeRobe():
    print()
    print("========== Garde-Robe ==========")
    print("Garde-robe: " , garde_robe)
    print()


def ajouterVetement():
    isAjouter=True

    while isAjouter==True:

        # Ajouter un objet dans la liste 
        NomArticle= input("Nom de l'article: ")
        while True:
            nombreElements= input("Nombre d'objets: ")

            if not nombreElements.isdigit():
                print("Erreur : veuillez entrer un nombre.")
                continue

            # Ajout dans la listes
            garde_robe[NomArticle] = nombreElements
            break

        # Continuer d'ajouter
        isContinuer=True
        while isContinuer==True:
            ouiOuNon= input("Ajouter un autre objet (oui / non): ")
            ouiOuNon= ouiOuNon.lower()

            if not ouiOuNon in ("oui", "non"):
                print("Saisie invalide: saisissez  (Oui / Non) pour continuer.")
                continue
            isContinuer=False

        # Gérer réouverture et fermeture de la boucle
        if ouiOuNon=="oui":
            isAjouter=True
        elif ouiOuNon=="non":
            isAjouter=False

    afficherGardeRobe()


def menu():
    choix = 0

    while choix != 3:
        print("========== Menu ==========")
        print("1. Afficher la garde robe")
        print("2. Ajouter un vêtement")
        print("3. Quitter")

        # Boucle de contrôle de saisie
        while True:
            saisie = input("Choisissez une option (1, 2 ou 3) : ")

            if not saisie.isdigit():
                print("Erreur : veuillez entrer un nombre.")
                continue

            choix = int(saisie)

            if choix not in (1, 2, 3):
                print("Erreur : choix invalide.")
                continue

            break  # saisie valide

        print()

        if choix == 1:
            afficherGardeRobe()

        elif choix == 2: 
            ajouterVetement()

        elif choix == 3:
            print("Merci pour votre visite !")


menu()

