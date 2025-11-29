print("Starting the web scraping application...")

from scraper import WebScraper

def main():
    url = "https://example.com"  # Replace with the target URL
    scraper = WebScraper()
    
    html_content = scraper.fetch_page(url)
    data = scraper.parse_data(html_content)
    
    print("Scraped Data:", data)

if __name__ == "__main__":
    main()