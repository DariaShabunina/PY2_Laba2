from typing import Optional

from typing import List

from pydantic import BaseModel


class Book(BaseModel):
    name: str
    id: int


class Library(BaseModel):
    books: Optional[List[Book]] = []

    def get_next_book_id(self) -> int:
        return len(self.books) + 1

    def get_index_by_book_id(self, search: int) -> int:
        for i in range(len(self.books)):
            if self.books[i].id == search:
                return i
        raise ValueError("Книги с запрашиваемым id не существует")


books = [
    {
        "author": "Пушкин А. С.",
        "id": 500,
    },
    {
        "author": "Лермонтов М. Ю.",
        "id": 250,
    },
]
list_books = [Book(name=book["author"], id=book["id"]) for book in books]
library = Library(books=list_books)
print(library.get_index_by_book_id(400))
#end
