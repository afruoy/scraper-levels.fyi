# Scraper for the *levels.fyi* website

### Goal?

- Recover the complete compensation database for all the job types proposed in the dropdown menu at the top url [https://www.levels.fyi/comp.html](https://www.levels.fyi/comp.html).

- Try to mimic as much as possible the database as it is stored at the *levels.fyi* servers (sample [here](https://docs.google.com/spreadsheets/d/1brSr6NvdgkEGd7Lo1a_qlTVqLSUg1ENNxY3xDTtGFnI/edit#gid=0)).

- Keep the csv files up-to-date twice a day.

### Why?

The filter, navigation and display tools provided by *levels.fyi* may seem constraining and couldn't allow to retrieve desired elaborate information.


### Difficulties?

The tables are stored dynamically and some changes can be made after a row has been added. 

### How?

Basic web-scraping.

* Navigating with : 
	* [Selenium webdriver](https://en.wikipedia.org/wiki/Selenium_(software)#Selenium_WebDriver)
	* [Chromedriver](https://chromedriver.chromium.org/)
* Scraping with : 
    * [BeautifulSoup4](https://en.wikipedia.org/wiki/Beautiful_Soup_\(HTML_parser\))
    * [Requests-html](https://docs.python-requests.org/projects/requests-html/en/latest/)
* Ongoing updating on a RaspberryPi 3B with : 
	* [Keychain](https://www.funtoo.org/Keychain)
	* [Cron](https://en.wikipedia.org/wiki/Cron)

### What to do next?

- **Cleaning and normalizing**

    The data we are recovering isn't "cleaned nor normalized" compared to the [one](https://www.levels.fyi/offerings/) *levels.fyi* offer to their subscribed clients. 
    - Remove duplicates
    - "Google", "google", "GOOGLE" should refer to the same company
    - ...

- **Improving performance**

    The current fetch rate is about 8 rows/s.

### Is it illegal?

Nothing suggests it in the [robots.txt](https://www.levels.fyi/robots.txt) file or in the [T&Cs](https://www.levels.fyi/about/terms.html) page, as long as this repo stays private.
