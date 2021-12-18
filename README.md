# Scraper for levels.fyi website

### Goal?

Recover the complete compensation database for all the job types proposed in the dropdown menu at this url [https://www.levels.fyi/comp.html](https://www.levels.fyi/comp.html).


### Difficulties?

The tables are stored dynamically.

### How?

Basic web-scraping : 

* Navigating with [selenium-based webdriver](https://en.wikipedia.org/wiki/Selenium_(software))
* Scraping with 
    * [BeautifulSoup4](https://en.wikipedia.org/wiki/Beautiful\_/Soup\_/(HTML\_/parser) 
    * [Requests-html](https://docs.python-requests.org/projects/requests-html/en/latest/)
