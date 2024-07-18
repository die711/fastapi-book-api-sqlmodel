from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from src.db.models import Book
from .schemas import BookCreateModel


class BookService:
    """
        This class provides methods to create, read, update, and delete books
    """

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_books(self):
        """
        Get a list of all books
        :param book_data: data to create a new book
        :return: list: list of books
        """

        statement = select(Book).order_by(Book.created_at)
        result = await self.session.exec(statement)
        return result.all()

    async def get_book(self, book_uid: str) -> Book | None:
        """
        Get a book by its UUID
        :param book_uid: The UUID of the book
        :return: book object
        """

        statement = select(Book).where(Book.uuid == book_uid)
        result = await self.session.exec(statement)
        return result.first()

    async def create_book(self, book_data: BookCreateModel):
        """
        Create a new book
        :param book_data: data to create a new book
        :return: the new book
        """

        new_book = Book(**book_data.model_dump())
        self.session.add(new_book)
        await self.session.commit()

        return new_book

    async def update_book(self, book_uid: str, book_update_data: BookCreateModel):
        """
        Update a book
        :param book_uid: The UUID of the book
        :param book_update_data: The data to update the book
        :return: The updated book
        """

        statement = select(Book).where(Book.uuid == book_uid)
        result = await self.session.exec(statement)
        book = result.first()

        for key, value in book_update_data.model_dump().items():
            setattr(book, key, value)

        await self.session.commit()
        return book

    async def delete_book(self, book_uid: str):
        """
        Delete a book
        :param book_uid: the UUID of the book
        :return: None
        """

        statement = select(Book).where(Book.uuid == book_uid)
        result = await self.session.exec(statement)
        book = result.first()

        await self.session.delete(book)
        await self.session.commit()
