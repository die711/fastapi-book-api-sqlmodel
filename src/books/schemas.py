from src.db.models import Book
from pydantic import BaseModel


class BookResponseModel(Book):
    """
    This class is used to validate the response when getting book objects
    """
    pass


class BookCreateModel(BaseModel):
    """
    This class is used to validate the request when creating or updating a book
    """

    title: str
    author: str
    isbn: str
    description: str

    model_config = {
        'json_schema_extra': {
            'example': {
                'title': 'Book',
                'author': 'John C',
                'isbn': '978-1-49339-1387-3',
                'description': 'A book written in Python'
            }
        }

    }
