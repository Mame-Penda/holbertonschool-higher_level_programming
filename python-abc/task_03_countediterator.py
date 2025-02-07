class CountedIterator:
    """
    Une classe qui étend un itérateur standard en comptant le nombre itérés.
    """

    def __init__(self, iterable):
        """
        Initialise l'itérateur avec un itérable donné et un compteur à zéro.

        Args:
            iterable: Un itérable (par exemple, une liste, un tuple, etc.).
        """
        self.iterator = iter(iterable)  # Convertit l'itérable en itérateur
        self.counter = 0  # Initialise le compteur à zéro

    def __next__(self):
        """
        Retourne l'élément suivant de l'itérateur et incrémente le compteur.

        Returns:
            Le prochain élément de l'itérateur.

        Raises:
            StopIteration: Si l'itérateur est épuisé.
        """
        item = next(self.iterator)  # Récupère le prochain élément
        self.counter += 1  # Incrémente le compteur
        return item

    def get_count(self):
        """
        Retourne le nombre d'éléments itérés jusqu'à présent.

        Returns:
            int: Le nombre d'éléments itérés.
        """
        return self.counter
