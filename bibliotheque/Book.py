class Book:
    def __init__(self, title, author, year, available):
        self.title = title
        self.author =author
        self.year = year
        self.available = available
        
        if not isinstance(title, str) or not title.strip():
          raise ValueError ("le titre doit être une chaîne non vide")
        if not isinstance(author, str) or not author.strip():
          raise ValueError ("l'auteur doit être une chaîne non vide")
        if not isinstance(year, int):
          raise TypeError(" l'année doit être un entier")
        if year < 0 or year > 2025:
          raise ValueError("l'année doit être valide")
        if not isinstance(available, bool):
          raise  TypeError("la disponibilité doit être un booléen")
      
    def __repr__(self):
     status = "disponible" if self.available else "emprunté"
     return f"{self.title} par {self.author} ({self.year}) - {status}"