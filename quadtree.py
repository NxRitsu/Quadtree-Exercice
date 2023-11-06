from __future__ import annotations
class QuadTree:
    """
    Classe représentant un QuadTree pour organiser des données spatiales.
    """
    NB_NODES : int = 4
    def __init__(self, hg: bool | QuadTree, hd: bool | QuadTree, bd: bool | QuadTree,bg: bool | QuadTree):
        pass

    @property
    def depth(self) -> int:
        """ Recursion depth of the quadtree"""
        return 1


    @staticmethod
    def fromFile(filename):
        with open(filename, 'r') as file:
            data = eval(file.read())  # On utilise eval pour convertir le fichier texte en structure de liste
        return QuadTree.fromList(data)

    @staticmethod
    def fromList(data):
        if isinstance(data, list):
            # On vérifie si la liste contient des sous-listes
            if isinstance(data[0], list):
                hg, hd, bg, bd = (QuadTree.fromList(sublist) for sublist in data)
                return QuadTree(hg, hd, bg, bd)
            else:
                # Si la liste est une feuille, on crée un QuadTree avec les valeurs booléennes
                return QuadTree(*data)

import tkinter as tk

class TkQuadTree(QuadTree):
    def __init__(self, data):
        # Appeler le constructeur de la classe parent avec des valeurs arbitraires, car ils seront remplacés dans la méthode draw
        super().__init__(None, None, None, None)
        self.data = data
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()
        self.draw(0, 0, 400, self.data)

    def draw(self, x, y, size, node):
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
        self.root.mainloop()

if __name__ == '__main__':
    filename = 'quadtree.txt'
    with open(filename, 'r') as file:
        data = eval(file.read())
    tk_quadtree = TkQuadTree(data)
    tk_quadtree.paint()


