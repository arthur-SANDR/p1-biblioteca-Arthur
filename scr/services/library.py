import sqlite3
from datetime import date, timedelta

DB_NAME = "library.db"

class Library:
    
    def __init__(self):
        self._create_tables()

    # ---------------------------
    # Banco de Dados
    # ---------------------------
    def _connect(self):
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row
        return conn

    def _create_tables(self):
        conn = self._connect()
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                isbn TEXT UNIQUE NOT NULL,
                year INTEGER NOT NULL,
                quantity INTEGER NOT NULL
            )
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS members (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT NOT NULL
            )
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS loans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                book_id INTEGER NOT NULL,
                member_id INTEGER NOT NULL,
                date_borrowed TEXT NOT NULL,
                date_due TEXT NOT NULL,
                date_returned TEXT,
                status TEXT NOT NULL,
                FOREIGN KEY(book_id) REFERENCES books(id),
                FOREIGN KEY(member_id) REFERENCES members(id)
            )
        """)

        conn.commit()
        conn.close()

    # ---------------------------
    # LIVROS
    # ---------------------------
    def add_book(self, title, author, isbn, year, quantity):
        conn = self._connect()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO books (title, author, isbn, year, quantity)
            VALUES (?, ?, ?, ?, ?)
        """, (title, author, isbn, year, quantity))

        conn.commit()
        conn.close()
        print("📚 Livro registrado com sucesso!")

    def list_books(self):
        conn = self._connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM books")
        rows = cur.fetchall()
        conn.close()

        if not rows:
            print("Nenhum livro cadastrado.")
        else:
            for b in rows:
                print(f"[{b['id']}] {b['title']} - {b['author']} | Qtd: {b['quantity']}")

    def _update_book_quantity(self, book_id, amount):
        conn = self._connect()
        cur = conn.cursor()

        cur.execute("""
            UPDATE books SET quantity = quantity + ?
            WHERE id = ?
        """, (amount, book_id))

        conn.commit()
        conn.close()

    def _get_book(self, book_id):
        conn = self._connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM books WHERE id = ?", (book_id,))
        book = cur.fetchone()
        conn.close()
        return book

    # ---------------------------
    # MEMBROS
    # ---------------------------
    def register_member(self, name, email, phone):
        conn = self._connect()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO members (name, email, phone)
            VALUES (?, ?, ?)
        """, (name, email, phone))

        conn.commit()
        conn.close()
        print("👤 Membro registrado!")

    def list_members(self):
        conn = self._connect()
        cur = conn.cursor()

        cur.execute("SELECT * FROM members")
        rows = cur.fetchall()
        conn.close()

        if not rows:
            print("Nenhum membro cadastrado.")
        else:
            for m in rows:
                print(f"[{m['id']}] {m['name']} - {m['email']}")

    def _get_member(self, member_id):
        conn = self._connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM members WHERE id = ?", (member_id,))
        member = cur.fetchone()
        conn.close()
        return member

    # ---------------------------
    # EMPRÉSTIMOS
    # ---------------------------
    def lend_book(self, book_id, member_id):
        book = self._get_book(book_id)
        member = self._get_member(member_id)

        if not book:
            print("❌ Livro não encontrado.")
            return
        if not member:
            print("❌ Membro não encontrado.")
            return
        if book["quantity"] <= 0:
            print("⚠️ Livro indisponível.")
            return

        data_hoje = str(date.today())
        data_devolucao = str(date.today() + timedelta(days=7))

        conn = self._connect()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO loans (book_id, member_id, date_borrowed, date_due, status)
            VALUES (?, ?, ?, ?, 'borrowed')
        """, (book_id, member_id, data_hoje, data_devolucao))

        conn.commit()
        conn.close()

        self._update_book_quantity(book_id, -1)

        print(f"📖 Empréstimo registrado! Devolução até {data_devolucao}.")

    def return_book(self, loan_id):
        conn = self._connect()
        cur = conn.cursor()

        cur.execute("SELECT * FROM loans WHERE id = ?", (loan_id,))
        loan = cur.fetchone()

        if not loan:
            print("❌ Empréstimo não encontrado.")
            conn.close()
            return

        if loan["status"] == "returned":
            print("Este livro já foi devolvido.")
            conn.close()
            return

        cur.execute("""
            UPDATE loans
            SET status = 'returned',
                date_returned = ?
            WHERE id = ?
        """, (str(date.today()), loan_id))

        conn.commit()
        conn.close()

        self._update_book_quantity(loan["book_id"], +1)

        print("✔ Livro devolvido com sucesso!")

    def list_loans(self):
        conn = self._connect()
        cur = conn.cursor()

        cur.execute("SELECT * FROM loans")
        rows = cur.fetchall()
        conn.close()

        if not rows:
            print("Nenhum empréstimo registrado.")
        else:
            for l in rows:
                status = "📕 Emprestado" if l["status"] == "borrowed" else "✔ Devolvido"
                print(f"[{l['id']}] Livro {l['book_id']} → Membro {l['member_id']} | {status}")
