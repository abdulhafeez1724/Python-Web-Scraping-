from scraper import scrape_website
from database import store_data_in_db, Base, engine

def main():
    # Create tables if they don't exist
    Base.metadata.create_all(engine)

    base_url = 'http://books.toscrape.com/'
    scraped_data = scrape_website(base_url, num_pages=10)
    store_data_in_db(scraped_data)

if __name__ == "__main__":
    main()
