class Library:
    def __init__(self, categories):
        self.categories = categories
        
        if not isinstance(categories, list):
            raise TypeError("Les catégories doivent être dans une liste")

         #Trouve une catégorie par son nom.
    def _find_category(self, category_name):

        for category in self.categories:
            if category.name == category_name:
                return category
        
        raise ValueError(f"La catégorie '{category_name}' n'existe pas")
    
    def borrow_book(self, category_name, title):
        #Emprunte un livre dans une catégorie spécifique.
        
        category = self._find_category(category_name)
        category.borrow(title)
    
    def return_book(self, category_name, book):
        #Rend un livre dans une catégorie spécifique.
        
        category = self._find_category(category_name)
        category.return_book(book)
    
    def total_available(self):
        #Calcule le nombre total de livres disponibles
        total = 0
        for category in self.categories:
            total += len(category.available_books())
        return total
    
    def __repr__(self):
        #Représentation textuelle de la bibliothèque
        return f"Bibliothèque avec {len(self.categories)} catégorie(s)"