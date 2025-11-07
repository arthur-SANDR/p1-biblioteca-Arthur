from typing import List
from models.book import Book
from models.member import Member
from models.loan import Loan

class Library:
    def __init__(self, book_repo, member_repo, loan_repo):
        self.book_repo = book_repo
        self.member_repo = member_repo
        self.loan_repo = loan_repo
        
    def add_book(self, book: Book) -> Book:
        return self.book_repo.add(book)
    
    def register_member(self, member: Member) -> Member:
        return self.member_repo.add(member)
    
    def lend_book(self, book_id: int, member_id: int) -> Loan:
        raise NotImplementedError
    
    def return_book(self, loan_id: int) -> None:
        
        raise NotImplementedError