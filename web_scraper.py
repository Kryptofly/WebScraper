import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = soup.find_all('h2')
    
    print("Scraped Titles:")
    for title in titles:
        print(title.get_text())

def main():
    url = 'https://example.com'  # Replace with the URL you want to scrape
    scrape_website(url)

if __name__ == "__main__":
    main()
