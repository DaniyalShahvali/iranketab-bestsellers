import requests
import bs4
import pandas as pd
url = 'https://www.iranketab.ir/tag/209-bestsellers'
r = requests.get(url)
soup = bs4.BeautifulSoup(r.text, 'lxml')



book_card = soup.find_all('a', class_ = 'card product-card-simple')
# book_name = book_card.find('h5').get_text()
# book_author = book_card.find('h6').get_text()
# book_price = book_card.find(class_ = 'toman text-primary font-bold').get_text()

# print(book_name)

book_list = []
for book in book_card:
  book_name = book.find('h5').get_text()
  book_author = book.find('h6').get_text()
  book_price = book.find(class_ = 'toman text-primary font-bold').get_text()
  book_link = 'https://www.iranketab.ir'+book.get('href')

  data = {
        'Name' : book_name,
        'Author' : book_author,
        'Price' : book_price,
        'Link' : book_link
    }
  book_list.append(data)

def export_csv():
    df = pd.DataFrame(book_list)
    df.to_csv('Bestseller.csv', encoding= 'utf-8-sig')
    print("Excel file has been created.")

    
print('----------------- Welcome to Iranketab best seller scrapper -----------------')

main = True
while main == True:
    for i in range(100):
        user_input = input("1) Show the Books\n2) Export a CSV\n3) Exit\n")
        if user_input == '1':
            for book in book_list:
                book_name = book['Name']
                book_author = book['Author']
                book_price = book['Price']
                print(f"{book_name} نویسنده {book_author}: {book_price} تومان")
        if user_input == '2':
            export_csv()
        if user_input == '3':
            main = False
            break