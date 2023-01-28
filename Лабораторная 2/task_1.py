class Book:
    def __init__(self, id: int, name: str, pages: int):
        """
        Создание и подготовка к работе объекта "Book"
        :param id: номер книги
        :param name: название книги
        :param pages: количество страниц в книге
        Примеры:
        >>> book = Book(1, "Война и мир", 2000) # инициализация экземпляра класса
        """
        if not isinstance(id, int):
            raise TypeError("Номер книги должен быть типа int")

        if not(id > 0):
            raise ValueError("Номер книги должен быть больше 0")

        self.id = id

        if not isinstance(name, str):
            raise TypeError("Название книги должно быть типа str")

        self.name = name

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")

        if not(pages > 0):
            raise ValueError("Количество страниц должно быть больше 0")

        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'Book(id={self.id}, name={self.name!r}, pages={self.pages})'


book = Book(2, "Красная таблетка", 3000)
print(repr(book))
#end
