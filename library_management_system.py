class Library:
    def __init__(self,listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("\n\t*****The books available in library are :*****")
        for index, books in enumerate(self.books):
            print(f" {index+1}. {books}")
        return True

    def borrowBooks(self,bookName):
        if bookName in self.books:
            print(f"\nYou have been sucessfully granted book named {bookName}.")
            self.books.remove(bookName)
        else:
            print("/nThe required book is not available at the moment")
        return True

    def returnBooks(self,bookName):
        print(f'\nThe book named {bookName} has been sucessfully returned.')
        self.books.append(bookName)
        return True
    
    def donateBooks(self):
        print("\nEnrter the name of the book you want to donate:")
        self.donatebook = input()
        self.books.append(self.donatebook)
        print("\nThe book has been sucessfully added to the library.")
        return True


class Student():
    booklist=[]
    def reqBook(self):
        book=input("\nEnter the name of the book you want to borrow : ") 
        self.booklist.append(book)
        return book

    def returnBook(self):
        print("\n\t*****The books you've borrowed from the library are :*****")
        for index, books in enumerate(self.booklist):
            print(f" {index+1} {books}")
        a = input("\nEnter the name of the book you want to return : ")
        self.booklist.remove(a)
        return a
        


centralLibrary = Library(["C++","Java","C","Visual Basics","Basic programming for beginners","C#","disctionary","advance python","data scientist"])
student=Student()
while(True):
    print('''\n\t^^^^^^^^^^^^Welcome to central library^^^^^^^^^^^^

        1. Display available Books.
        2. Borrow Books.
        3. Return Books.
        4. Donate Books.
        5. Exit.''')
    try:
        a=input("\nEnter your choice: ")
        if int(a)==1 :
            centralLibrary.displayAvailableBooks()

        elif int(a)==2:
            centralLibrary.borrowBooks(student.reqBook())
        
        elif int(a)==3:
            centralLibrary.returnBooks(student.returnBook())
        elif int(a)==4:
            centralLibrary.donateBooks()
        
        elif int(a)==5:
            exit()

        else:
            print("\nPlease enter a valid option")
    except Exception as e:
        print("\nEnter a valid option")
