from database.connection import get_connection

class MemberRepository:
    
    def create(self, name, email, phone):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO members (name, email, phone) VALUES (%s, %s, %s)",
            (name, email, phone)
        )
        conn.commit()
        conn.close()
        
    def list (self, member_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT  * FROM members WHERE id = ?", (member_id,))
        row = cursor.fetchone()
        conn.close()
        return row