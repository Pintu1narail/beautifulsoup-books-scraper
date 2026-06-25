# Books Data Scraper 📚

An automated Python web scraping script designed to extract book details from the "Books to Scrape" sandbox website.

## Features
- **Full Website Scraping:** Iterates through all 50 pages dynamically.
- **Rating Conversion:** Automatically maps text-based ratings (e.g., "Three") to numerical integers (e.g., 3).
- **Clean Data Extraction:** Captures full book titles from the HTML attributes and cleans currency symbols.
- **Structured Export:** Saves 1000 book records into a clean `book_list.csv` file.

## Data Fields Extracted
- Book Name (Full Title)
- Price (in £)
- Stock Availability
- Rating (1 to 5 Stars)

## Tech Stack
- Python 3
- Requests
- BeautifulSoup4
- Pandas
