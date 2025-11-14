class Category:
    def __init__(self, name, books):
        self.name =name
        self.books = books
        if not isinstance(name, str) or not name.strip():
            raise ValueError("la catégorie doit être une chaîne non vide")
        if not isinstance(books, list):
            raise TypeError("les lives doivent être dans une liste")
        
        # une methode pour renvoyer la liste des livres disponibles
        
    def available_books(self):
        return [book for book in self.books if book.available]
              
        # une methode pour emprunter un livre en le marquant comme non disponible
        
    def borrow(self, title):
          for book in self.books:
              if book.title == title :
               if not book.available:
                   raise RuntimeError(f"le livre '{title}' est déjà emprunté")
               book.available = False
               return
          raise ValueError(f"le livre '{title}' n'existe pas dans la catégorie'{self.name}'")
      # une methone pour rendre un livre en le marquant comme disponible
    def return_book(self, book):
       
                 if book not in self.books:
                    raise ValueError(f"Le livre '{book.title}' n'appartient pas à la catégorie '{self.name}'")
        
                 book.available = True
    # methode pour la représentation de la catégorie
    def __repr__(self):
        return f"Catégorie '{self.name}' avec {len(self.books)} livre"