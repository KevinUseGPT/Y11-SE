class Book: #create the Book class
    def __init__(self, book_id, title, author): #giving it properties
        self.book_id = book_id  #The book id, title and the author
        self.title = title 
        self.author = author 
        self.is_loaned = False #Boolean variable

class Borrower: #Class for the person borrowing the book
    def __init__(self, borrower_id, name): #The properties of the person
        self.borrower_id = borrower_id
        self.name = name #Their name

class Loan: #Class for the Loan of the book
    def __init__(self, book, borrower):
        self.book = book 
        self.borrower = borrower

class BookManager: #Class for the library of books
    def __init__(self):
        self.books = {} #Dictionary to store the book

    def add_book(self, book_id, title, author): #Function that stores the book id, title and the author into the dictionary
        if book_id in self.books:
            raise ValueError("Book ID already exists.") #If book is already inside the book manager dictionary it will not add the book
        self.books[book_id] = Book(book_id, title, author)

    def remove_book(self, book_id): #Remove function in the library If a book id is entered, it will delete the book
        if book_id in self.books:
            del self.books[book_id]
        else: 
            raise ValueError("Book ID not found.") #If there is no book with that id it will print no book found

    def search_book(self, book_id): #enters a book id
        return self.books.get(book_id, None) #returns the book

class BorrowerManager: #class for borrower
    def __init__(self):
        self.borrowers = {} #A dictionary of the borrowers

    def add_borrower(self, borrower_id, name): #Adds the borrower and their name into the dictionary
        if borrower_id in self.borrowers: #if its already in it will print they already exist
            raise ValueError("Borrower ID already exists.")
        self.borrowers[borrower_id] = Borrower(borrower_id, name) #if not then it will be added into the dictionary

    def remove_borrower(self, borrower_id):#a borrower id is obtained
        if borrower_id in self.borrowers: #if its inside the dictionary it will delete
            del self.borrowers[borrower_id]
        else:
            raise ValueError("Borrower ID not found.") #if not it will print the error

    def search_borrower(self, borrower_id): #searches the borrower id
        return self.borrowers.get(borrower_id, None) #this will return their name and id

class LoanManager:#new class for loan
    def __init__(self):
        self.loans = [] #list for loaned books

    def create_loan(self, book, borrower): #function to check if the book is loaned
        if book.is_loaned:
            raise ValueError("Book is already loaned.") #if its loaned then it will print this
        loan = Loan(book, borrower) #the loaned book will now be the name and the borrower
        self.loans.append(loan) #loaned book gets appended into the loaned book list
        book.is_loaned = True #boolean of the book status

    def return_loan(self, book):  #a book is entered
        for loan in self.loans:  #for loops for searching all book in the list
            if loan.book.book_id == book.book_id: #if the book is in the loaned list, it will get removed
                self.loans.remove(loan)
                book.is_loaned = False #false loaned status
                break
