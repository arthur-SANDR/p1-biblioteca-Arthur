from dataclasses import dataclass
from datetime import date

@dataclass
class Loan:
    id: int | None
    book_id: int
    member_id: int
    date_borrowed: str
    date_due: str
    date_returned: str | None = None
    status: str = "borrowed"