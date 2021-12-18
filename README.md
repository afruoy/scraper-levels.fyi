# Scraper for levels.fyi website

### Goal?

Recover the complete compensation database for all the job types proposed in the dropdown menu at the top url [https://www.levels.fyi/comp.html](https://www.levels.fyi/comp.html).

Try to mimic as much as possible the database as it is stored at the levels.fyi servers ([sample](https://docs.google.com/spreadsheets/d/1brSr6NvdgkEGd7Lo1a_qlTVqLSUg1ENNxY3xDTtGFnI/edit#gid=0)).

### Why?

The filter, navigation and display tools provided by levels.fyi may seem constraining and couldn't allow to retrieve desired elaborate information.


### Difficulties?

The tables (and any other relevant information) are stored dynamically.

### How?

Basic web-scraping : 

* Navigating with the [Selenium webdriver](https://en.wikipedia.org/wiki/Selenium_(software))
* Scraping with 
    * [BeautifulSoup4](https://en.wikipedia.org/wiki/Beautiful_Soup_\(HTML_parser\))
    * [Requests-html](https://docs.python-requests.org/projects/requests-html/en/latest/)


### What to do next?

Each day, an minimum of 30 rows are added to their database. 

If one would want to rely, this makes this latest information very valuable (and desirable). 

Implement an ongoing update This evolving information as it is more recent.

### Is it illegal?

Nothing suggests it in the [robots.txt](https://www.levels.fyi/robots.txt) file.
