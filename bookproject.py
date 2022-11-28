class Book:
    ISBN = None
    Title = None
    Author = None
    No_of_pages = None
    publisher = None

    def getBookDetail(self):
        ISBN = int(input("enter the ISBN: "))
        Title = input("enter the title of the book: ")
        Author = input("enter the author of book: ")
        No_of_pages = int(input("enter the no of pages: "))
        publisher = input("enter the publisher: ")
        # return(ISBN,Title,Author,No_of_pages,publisher) remove it
    # print(isbn,----)


obj = Book()
# no of books=int(input("enter no of books ")
# for in range(no of books):
# print(obj.getbookdetails())


print(obj.BookDetail())

