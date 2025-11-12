from typing import List
from datetime import date, timedelta
from models.book import Book
from models.member import Member
from models.loan import Loan

class Library:
    def __init__(self):
        self.books: List[Book] = []
        self.members: List[Member] = []
        self.loans: List[Loan] = []
        self.next_book_id = 1
        self.next_member_id = 1
        self.next_loan_id = 1
        
    def add_book(self, title: str, author: str, isbn: str, year: int, quantity: int =1) -> Book:
        book = Book(
            id=self.next_book_id,
            title=title,
            author=author,
            isbn=isbn,
            year=year,
            quantity=quantity
        )
        self.books.append(book)
        self.next_book_id += 1
        print(f"Livro '{book.title}'adicionado com sucesso!")
        return book
    def list_books(self):
        if not self.books:
            print("Nenhum livro cadastrado.")
        else:
            for b in self.books:
                status = "Disponível" if b.is_available() else "Indisponível"
                print(f"[{b.id}] {b.title} - {b.author} ({b.year}) | {status} | Qtd: {b.quantity}")
    def register_member(self, name: str, email: str, phone: str):
        member = Member(id=self.next_member_id, name=name, email=email, phone=phone)
        self.members.append(member)
        self.next_member_id += 1
        print(f"Membro '{member.name}' registrado com sucesso!")
        return member
    
    def list_members(self):
        if not self.members:
            print("Nenhum membro cadastrado.")
        else:
            for m in self.members:
                print(f"[{m.id}] {m.name} - Email: {m.email}")
                
    def lend_book(self, book_id: int, member_id: int):
        book = next((b for b in self.books if b.id == book_id), None)
        member = next((m for m in self.members if m.id == member_id), None)
        
        if not book:
            print("Livro não encontrado.")
            return
        if not member:
            print("Membro não encontrado.")
            return
        if not book.is_available():
            print("Livro indisponível para empréstimo.")
            return
        
        loan = Loan(
            id=self.next_loan_id,
            book=book,
            member=member,
            loan_date=date.today(),
            due_date=date.today() + timedelta(days=14)
        )
        self.loans.append(loan)
        book.quantity -= 1
        self.next_loan_id += 1
        print(f"Livro '{book.title}' emprestado para '{member.name}' com sucesso!")
        
    def return_book(self, loan_id: int):
        loan = next((l for l in self.loans if l.id == loan_id), None)
        
        if not loan:
            print("Empréstimo não encontrado.")
            return
           if loan.status == "returned":
            print("Livro já foi devolvido.")
            return
        
        book = next((b for b in self.books if b.id == loan.book.id), None)

        if book:
            book.increase_quantity()
            
        loan.status = "returned"
        load.date_returned = date.today()
        print(f"Livro '{loan.book.title}' devolvido por '{loan.member.name}' com sucesso!")
        
    def list_loans(self):
        if not self.loans:
            print("Nenhum empréstimo registrado.")
        else:
            for l in self.loans:
                status = "devolvido" if l.status == "returned" else "emprestado"
                
                print(f"[{l.id}] Livro: {l.book.id} -> Membro {l.member.id} | {status}")
