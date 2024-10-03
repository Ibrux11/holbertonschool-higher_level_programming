#!/usr/bin/python3

def read_file(filename=""):
    """
    Lit le contenu d'un fichier et l'affiche sur la sortie standard.

    Args:
        filename (str): Le chemin du fichier à lire. Par défaut, le nom du fichier est une chaîne vide.
    
    Description:
        Cette fonction ouvre un fichier encodé en UTF-8 et affiche son contenu
        sur la sortie standard (généralement la console). Si aucun nom de fichier
        n'est fourni, elle ne fera rien. La fonction lit tout le contenu du fichier
        et l'affiche sans ajout de saut de ligne à la fin.
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
