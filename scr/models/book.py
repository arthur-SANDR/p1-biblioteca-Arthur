from dataclasses import dataclass

@dataclass
class Book:
    id: int | None
    title: str
    isbn: str | None
    year: int | None
    quantity: int = 1
    
    def is_avaible(self) -> bool:
        return self.quantity > 0
    
    def decrase_quantity(self) -> None:
        
        if self.quantity > 0:
            sef.quantity -= 1
            
    def increase_quantity(self) -> None:
        self.quantity +=3 1