from services.library import Library

class CLI:
    def __init__(self):
        self.library = Library()
        
    def show_menu(self):
        print("\n=== Biblioteca CLI ===")
        print("1. Cadastrar Livro  ")
        print("2. Listar Livros   ")
        print("3. Cadastrar membro")
        print("4. Listar membros  ")
        print("5. Emprestar livro ")
        print("6. Devolver livro  ")
        print("7. Listar empréstimos")
        print("0. Sair            ")
        
    def run(self):
        while True:
            self.show_menu()
            choice = input("Escolha uma opção: ").strip()
            
            if choice == '1':
                title = input("Título: ")
                author = input("Autor: ")
                isbn = input("ISBN: ")
                year = input("Ano: ")
                try:
                    quantity = int(input("Quantidade: "))
                except ValueError:
                    print("Quantidade inválida.")
                    continue

                self.library.add_book(title, author, isbn, year, quantity)
                print("Livro cadastrado.")
            
            elif choice == '2':
                books = self.library.list_books()
                if not books:
                    print("Nenhum livro cadastrado.")
                else:
                    for b in books:
                        print(b)
                
            elif choice == '3':
                name = input("Nome: ")
                email = input("Email: ")
                phone = input("Telefone: ")
                
                self.library.register_member(name, email, phone)
                print("Membro cadastrado.")
                
            elif choice == '4':
                members = self.library.list_members()
                if not members:
                    print("Nenhum membro cadastrado.")
                else:
                    for m in members:
                        print(m)
                
            elif choice == '5':
                try:
                    member_id = int(input("ID do membro: "))
                except ValueError:
                    print("ID inválido.")
                    continue
                isbn = input("ISBN do livro: ")
                success = self.library.borrow_book(member_id, isbn)
                if success:
                    print("Empréstimo registrado.")
                else:
                    print("Empréstimo falhou.")
    
            elif choice == '6':
                try:
                    member_id = int(input("ID do membro: "))
                except ValueError:
                    print("ID inválido.")
                    continue
                isbn = input("ISBN do livro: ")
                success = self.library.return_book(member_id, isbn)
                if success:
                    print("Livro devolvido.")
                else:
                    print("Devolução falhou.")
    
            elif choice == '7':
                loans = self.library.list_loans()
                if not loans:
                    print("Nenhum empréstimo registrado.")
                else:
                    for l in loans:
                        print(l)
    
            elif choice == '0':
                print("Saindo...")
                break
                
            else:
                print("Opção inválida. Tente novamente.")
