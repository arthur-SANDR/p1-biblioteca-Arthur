from dataclasses import dataclass

@dataclass
class Member:
    id : int | None
    name: str
    email: str | None
    phone: str | None
    
    def can_borrow(self) -> bool:
        return True