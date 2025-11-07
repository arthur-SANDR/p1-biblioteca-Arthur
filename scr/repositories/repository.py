from typing import Generic, TypeVar, List, Optional

T = TypeVar("T")

class Repository(Generic[T]):
    def add(self, entity: T) -> T:
        raise NotImplementedError

    def get_by_id(self, id: int) -> Optional[T]:
        raise NotImplementedError

    def list_all(self) -> List[T]:
        raise NotImplementedError
    
    def update(self, entity: T) -> T:
        raise NotImplementedError

    def delete(self, id: int) -> None:
        raise NotImplementedError