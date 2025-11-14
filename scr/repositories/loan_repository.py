from database.connection import get_connection

class LoanRepository:
    
    def create(self, book_id, member_id, date_borrowed, date_due):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO loans (book_id, member_id, date_borrowed, date_due) VALUES (%s, %s, %s, %s)",
            (book_id, member_id, date_borrowed, date_due)
        )
        conn.commit()
        conn.close()
        
    def list(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM loans")
        rows = cursor.fetchall()
        conn.close()
        return rows

    def get_by_id(self, loan_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM loans WHERE id = %s", (loan_id,))
        row = cursor.fetchone()
        conn.close()
        return row
    
    def close_loan(self, loan_id, date_returned):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE loans SET date_returned = %s WHERE id = %s",
            (date_returned, loan_id)
        )
        conn.commit()
        conn.close()