with open('C:\Users\7sylw\OneDrive\Pulpit\fekcyz\Książki « - Księgarnia informatyczna Helion.html', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'C:\Users\7sylw\OneDrive\Pulpit\fekcyz\Książki « - Księgarnia informatyczna Helion.html.parser')

titles = Książki.find_all('h1')
book_titles = [title.text.strip() for title in titles]
prices = soup.find_all('span', class_='cena')
book_prices = [price.text.strip() for price in prices]
for title, price in zip(book_titles, book_prices):
    print("Tytuł:", title)
    print("Cena:", price)
    print();