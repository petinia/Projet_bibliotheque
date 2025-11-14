from Book import Book
from Category import Category
from Library import Library

def clean_line(line):
    # pour Nettoyer et valider une ligne du fichier CSV.

    parts = line.strip().split(';')
    
    if len(parts) != 5:
        return None
    
    category = parts[0].strip()
    title = parts[1].strip()
    author = parts[2].strip()
    year_str = parts[3].strip()
    available_str = parts[4].strip().lower()
    
    if not all([category, title, author, year_str, available_str]):
        return None
    
    try:
        year = int(year_str)
    except ValueError:
        return None
    
    if available_str == 'yes':
        available = True
    elif available_str == 'no':
        available = False
    else:
        return None
    
    return {
        'category': category,
        'title': title,
        'author': author,
        'year': year,
        'available': available
    }


def load_books_from_csv(filename):
    #pour Charger les livres depuis un fichier CSV.
    
    books_by_category = {}
    
    with open(filename, 'r', encoding='utf-8') as file:
        next(file)
        
        for line in file:
            cleaned_data = clean_line(line)
            
            if cleaned_data is None:
                continue
            
            try:
                book = Book(
                    cleaned_data['title'],
                    cleaned_data['author'],
                    cleaned_data['year'],
                    cleaned_data['available']
                )
                
                category_name = cleaned_data['category']
                if category_name not in books_by_category:
                    books_by_category[category_name] = []
                
                books_by_category[category_name].append(book)
                
            except (ValueError, TypeError) as e:
                print(f"Erreur lors de la création du livre: {e}")
                continue
    
    return books_by_category


def main():
    #Fonction principale du programme.
    
    print("GESTION DE LA BIBLIOTHÈQUE MUNICIPALE")
    
    print()
    
    try:
        books_dict = load_books_from_csv('books.csv')
        
        categories = []
        for category_name, books_list in books_dict.items():
            category = Category(category_name, books_list)
            categories.append(category)
        
        library = Library(categories)
        
        print(f" {len(categories)} catégories")
        for category in categories:
            print(f"   - {category.name}: {len(category.books)} livre(s)")
            
        print()
        total_books = sum(len(category.books) for category in categories)
        print(f"Nombre total de livres dans la bibliothèque: {total_books}")
        print(f" total de livres disponibles: {library.total_available()}")
        print(f"Livres empruntés: {total_books - library.total_available()}")
        print()
        
        print("Emprunt d'un livre  dans la catégorie 'Roman'...")
        try:
            library.borrow_book('Roman', "Madame Bovary")
            print("  Livre emprunté avec succès!")
        except (ValueError, RuntimeError) as e:
            print(f"  Erreur: {e}")
        print()
        
        print(f"Total de livres disponibles: {library.total_available()}")
        print()
        
        print("Tentative d'emprunt (d'un livre déjà emprunté)")
        try:
            library.borrow_book('Roman', "Madame Bovary")
            print("  Livre emprunté avec succès!")
        except RuntimeError as e:
            print(f"   Erreur attendue: {e}")
        except ValueError as e:
            print(f"  Erreur: {e}")
        print()
        
        print(" Recherche du livre pour le retour...")
        book_to_return = None
        for category in categories:
            if category.name == 'Roman':
                for book in category.books:
                    if book.title == "Madame Bovary":
                        book_to_return = book
                        break
        
        if book_to_return:
            print(f" Retour du livre '{book_to_return.title}'...")
            try:
                library.return_book('Roman', book_to_return)
                print("   Livre retourné avec succès!")
            except ValueError as e:
                print(f"  Erreur: {e}")
        print()
        
        print(f"Nombre total de livres disponibles: {library.total_available()}")
        print()
        
        
        print("STATISTIQUES PAR CATÉGORIE")
        
        for category in categories:
            available = len(category.available_books())
            total = len(category.books)
            print(f"{category.name}: {available}/{total} disponibles")
        
    except FileNotFoundError:
        print("Erreur: Le fichier 'books.csv' est introuvable.")
    except Exception as e:
        print(f" Erreur inattendue: {e}")


if __name__ == "__main__":
    main()