from __future__ import annotations
import tkinter as tk
class QuadTree:
    """
    Classe représentant un QuadTree pour organiser des données spatiales.
    """
    NB_NODES : int = 4
    def __init__(self, hg: bool | QuadTree, hd: bool | QuadTree, bd: bool | QuadTree,bg: bool | QuadTree):
        """
        Initialise un nœud QuadTree avec ses quatre sous-arbres.

        Args:
            hg (bool | QuadTree): Sous-arbre Nord-Ouest.
            hd (bool | QuadTree): Sous-arbre Nord-Est.
            bd (bool | QuadTree): Sous-arbre Sud-Ouest.
            bg (bool | QuadTree): Sous-arbre Sud-Est.
        """

    @property
    def depth(self) -> int:
        """
        Renvoie la profondeur de la récursion du QuadTree.

        Returns:
            int: La profondeur de la récursion.
        """
        return 1


    @staticmethod
    def fromFile(filename):
        """
        Crée un QuadTree à partir d'un fichier.

        Args:
            filename (str): Le nom du fichier contenant les données du QuadTree.

        Returns:
            QuadTree: Le QuadTree créé à partir du fichier.
        """
        with open(filename, 'r') as file:
            data = eval(file.read())  # On utilise eval pour convertir le fichier texte en structure de liste
        return QuadTree.fromList(data)

    @staticmethod
    def fromList(data):
        """
        Crée un QuadTree à partir de données sous forme de liste.

        Args:
            data (list): Les données pour créer le QuadTree.

        Returns:
            QuadTree: Le QuadTree créé à partir des données.
        """
        if isinstance(data, list):
            # On vérifie si la liste contient des sous-listes
            if isinstance(data[0], list):
                hg, hd, bg, bd = (QuadTree.fromList(sublist) for sublist in data)
                return QuadTree(hg, hd, bg, bd)
            else:
                # Si la liste est une feuille, on crée un QuadTree avec les valeurs booléennes
                return QuadTree(*data)

class TkQuadTree(QuadTree):
    """
    Classe représentant une interface graphique pour représenter un QuadTree avec Tkinter.
    Hérite de la classe QuadTree.
    """
    def __init__(self, data):
        """
        Initialise l'interface graphique Tkinter pour représenter un QuadTree.

        Args:
            data: Les données du QuadTree sous forme de liste.
        """
        # Appeler le constructeur de la classe parent avec des valeurs arbitraires, car ils seront remplacés dans la méthode draw
        super().__init__(None, None, None, None)
        self.data = data
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()
        self.draw(0, 0, 400, self.data)

    def draw(self, x, y, size, node):
        """
        Dessine le QuadTree de manière récursive.

        Args:
            x (int): Coordonnée X de la zone de dessin.
            y (int): Coordonnée Y de la zone de dessin.
            size (int): Taille de la zone de dessin.
            node: Le nœud actuel du QuadTree.
        """
        if isinstance(node, list):
            half_size = size // 2
            self.draw(x, y, half_size, node[0])
            self.draw(x + half_size, y, half_size, node[1])
            self.draw(x, y + half_size, half_size, node[2])
            self.draw(x + half_size, y + half_size, half_size, node[3])
        elif isinstance(node, int):
            fill_color = 'white' if node == 0 else 'black'
            self.canvas.create_rectangle(x, y, x + size, y + size, fill=fill_color, outline='black')

    def paint(self):
        """
        Démarre la boucle principale de l'interface graphique Tkinter pour afficher le dessin du QuadTree.
        """
        self.root.mainloop()

if __name__ == '__main__':
    filename = 'quadtree.txt'
    with open(filename, 'r') as file:
        data = eval(file.read())
    tk_quadtree = TkQuadTree(data)
    tk_quadtree.paint()


