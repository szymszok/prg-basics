from classebook import ebook

ebook = ebook('Dziennik Cwaniaczka','Jeff Kinney',65)


while True:
    number = int(input('Decide what to do: 0-stop, 1-show status,2-if you read page click to show next one,3-open book, 4-close book: '))

    if number == 0:
        print("Exiting the program.")
        break
    elif number == 1:
        print('Book status: ')
        print(ebook.show_status())
    elif number == 2:
        ebook.reading()    
    elif number == 3:
        print('Opening book')
        ebook.opened()
    elif number == 4:
        print('Closing book')
        ebook.closed()