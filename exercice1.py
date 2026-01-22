
articles = ["peluche", "bracelet", "casserole", "bouteille", "crème"]

def afficherArticles():
    print("===== Articles ====")
    for i, article in enumerate(articles):
        print(f"{i+1}: {article}")
    print()


def supprimerArticle(index):
    index-=1
    return (f"{articles.pop(index)} supprimé(e) avec succès")


def menu():
    choix = 0

    while choix != 3:
        print("========== Menu ==========")
        print("1. Afficher les articles")
        print("2. Retirer un article")
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
            afficherArticles()

        elif choix == 2: 
            afficherArticles()
            article = input("Choisissez le numéro de l’article à supprimer : ")
            # pas de contrôle pour l'exemple
            article = int(article)
            supprimerArticle(article)

        elif choix == 3:
            print("Merci pour votre visite !")


menu()


