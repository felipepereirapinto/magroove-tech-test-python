from bs4 import BeautifulSoup
import requests

def print_article(title, link):
  message = 'Title: {}\nLink: {}\n'
  print(message.format(title, link))

def main():
  link = 'https://qz.com/africa/latest/'
  html_text = requests.get(link).text

  soup = BeautifulSoup(html_text, 'html.parser')
  articles = soup.find_all('li', class_ = '_8OV9v _1dOXL')
  for article in articles:
    title = article.find('div', class_ = 'esSAQ _8S5gh').text
    link = 'https://qz.com' + article.a['href']
    print_article(title, link)

main()