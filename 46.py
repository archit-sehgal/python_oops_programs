class book:
    def __init__(self,Title,Author,Price):
        self.Title=Title
        self.Author=Author
        self.Price=Price
    def View(self):
        print(f"Title of Book: {self.Title}\nAuthor Of Book: {self.Author}\nPrice of Book: {self.Price}")
call=book("JavaEssentials","Joseph Murphy",500)
call.View()