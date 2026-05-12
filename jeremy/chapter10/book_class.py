class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def describe(self):
        print(f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}")

book_1 = Book("something", "Henry Henryson the third", "-1")
book_2 = Book("nothing", "someone", "10218321847364")