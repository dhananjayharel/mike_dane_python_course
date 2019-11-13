class Book:
  def __init__(self, title, author, numPages):
      self.title = title
      self.author = author
      self.numPages = numPages

book1 = Book("Harry Potter", "JK Rowling", 500);
# book1.title = "Half-Blood Prince"

print(book1.title)
