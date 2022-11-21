import argparse


def analyser_commande():
    """Génère un interpréteur de commande.

    Returns:
        Namespace: Un objet Namespace tel que retourné par parser.parse_args().
                   Cette objet aura l'attribut «idul» représentant l'idul du joueur
                   et l'attribut «parties» qui est un booléen True/False.
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("Idul", type=str,
                     help="IDUL du joueur")
    parser.add_argument("-p", "--parties", action="count",
                    help="lister les parties existantes")

    return parser.parse_args()





analyser_commande()
