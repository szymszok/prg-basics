class ebook:
    def __init__(self,title,author,pages):
        self.is_on = False
        self.title = title
        self.author = author
        self.page = pages
        self.current_page = 1
    def opened(self):
        self.is_on = True

    def closed(self):
        self.is_on = False

    def show_status(self):
        return f'\n Title: {self.title}\n Author: {self.author}\n current page: {self.current_page}'

    def reading(self):
        if self.is_on == True:
            print('Changing page ...')
            self.current_page += 1
            return self.current_page
        else:
            print('Book is closed :(')




