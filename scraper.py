from selenium import webdriver
from time import sleep
from data import addresses, home
from functions.home_url_dissection import _home_url
from functions.url_dissection import _url_dissection
from functions.distances import _distances_
from functions.plot import make_plot
import copy


class MapScraper:
    def __init__(self, data):
        self.driver = webdriver.Chrome()
        self.addresses = addresses
        self.driver.get("https://google.com/maps")
        sleep(2)

    def _get_home(self):
        sleep(1)
        self.driver.find_element_by_id("searchboxinput").send_keys(home)
        sleep(3)
        self.driver.find_element_by_id("searchbox-searchbutton").click()
        sleep(3)
        home_url = self.driver.current_url
        sleep(1)
        self.driver.find_element_by_id("searchboxinput").clear()
        return home_url

    def _get_urls(self):
        urls = []
        for address in addresses:
            sleep(1)
            self.driver.find_element_by_id("searchboxinput").send_keys(address)
            sleep(1)
            self.driver.find_element_by_id("searchbox-searchbutton").click()
            sleep(3)
            urls.append(self.driver.current_url)
            sleep(1)
            self.driver.find_element_by_id("searchboxinput").clear()
        return urls

    def _grabURLS(self):
        urlList = self._get_urls()
        return _url_dissection(urlList)

    def compare(self):
        home_url = self._get_home()
        CoordinateList = self._grabURLS()
        home = _home_url(home_url)
        CoordinateList_copy = copy.deepcopy(CoordinateList)
        _distances_(home, CoordinateList_copy)
        self.driver.quit()

        make_plot(home, CoordinateList)


scraper_bot = MapScraper(addresses)
scraper_bot.compare()
