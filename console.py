import pdb
from models.author import Author
from models.book import Book

import repositories.author_repository as author_repo
import repositories.book_repository as book_repo 

book_repo.delete_all()
author_repo.delete_all()

author1 = Author("Sam Neil")
author_repo.save (author1)

author2= Author ("George Michael")
author_repo.save (author2)

book1=Book ("Jurrasic Park", "non-fiction", author1)
book_repo.save (book1)

book2=Book ("Jurrasic Park - the playground hunt", "non-fiction", author1)
book_repo.save (book2)

book3=Book ("My story", "Biogrophy", author2)
book_repo.save (book3)

# all_books =book_repo.select_all ()
# print (all_books.__dict__)