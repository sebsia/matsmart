class WebScraper:
    def fetch_page(self, url):
        import requests
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            raise Exception(f"Failed to fetch page: {response.status_code}")

    def parse_data(self, html):
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')
        # Example: Extracting all the titles from the page
        titles = soup.find_all('h1')
        return [title.get_text() for title in titles]