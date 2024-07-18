from typing import List
from fastapi import APIRouter, Depends, status
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session
from .service import BookService
from .schemas import BookCreateModel, BookResponseModel

book_router = APIRouter(
    prefix='/books'
)


@book_router.get('/', status_code=status.HTTP_200_OK, response_model=List[BookResponseModel])
async def read_books(session: AsyncSession = Depends(get_session)):
    books = await BookService(session).get_all_books()
    return books


@book_router.get('/{id}', status_code=status.HTTP_200_OK)
async def read_book(id: str, session: AsyncSession = Depends(get_session)):
    book = await BookService(session).get_book(id)
    return book


@book_router.post('/', status_code=status.HTTP_201_CREATED)
async def create_book(book: BookCreateModel, session: AsyncSession = Depends(get_session)):
    new_book = await BookService(session).create_book(book)
    return new_book


@book_router.put('/{id}', status_code=status.HTTP_200_OK)
async def update_book(id: str, data: BookCreateModel, session: AsyncSession = Depends(get_session)):
    updated_book = await BookService(session).update_book(id, data)
    return updated_book


@book_router.delete('{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(id: str, session: AsyncSession = Depends(get_session)):
    await BookService(session).delete_book(id)
