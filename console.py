from models.author import Author
from models.book import Book

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

# book_repository.delete_all()
# author_repository.delete_all()

author_1 = Author('Ian', 'Rankine')
author_2 = Author('Raymond', 'Chandler')

author_repository.save(author_2)
author_repository.save(author_1)

book_1 = Book('The Big Sleep', 'Crime', 'Bloomsbury', author_2)
book_2 = Book('There\'s Been a Murdurrr', 'Crime', 'Penquin', author_1)

book_repository.save(book_1)
book_repository.save(book_2)

#author_repository.save(author_1)



#book_repository.save(author_1)