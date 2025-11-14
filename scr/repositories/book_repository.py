from database.connection import get_connection

class BookRepository:
    
    def create(self, title, author, published_year, isbn):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO books (title, author, published_year, isbn)
            VALUES (?, ?, ?, ?)
        ''', (title, author, isbn, year, quantity))
        conn.commit()
        conn.close()
        
    def list(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM books')
        books = cursor.fetchall()
        conn.close()
        return books
    
    def update_quantity(self, book_id, amount):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE books
            SET quantity = ?
            WHERE id = ?
        ''', (amount, book_id))
        conn.commit()
        conn.close()
        
    def get_by_id(self, book_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM books WHERE id = ?', (book_id,))
        row = cursor.fetchone()
        conn.close()
        return row 