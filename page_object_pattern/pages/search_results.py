"""
Ten page object będzie odpowiedzialny za wyniki wyszukiwania.
"""
# w ramach przeniesienia lokatorów do oddzielnego pliku, importujemy klasę je zawierającą:
from page_object_pattern.locators.locators import SearchResultLocators

# dodajemy loggera - na jego podstawie będziemy znali wprowadzone wartości oraz problemy z wyszukaniem
import logging

class SearchResultsPage:

    def __init__(self, driver):
        self.driver = driver

        # dodajemy logger:
        self.logger = logging.getLogger(__name__)

        # mapujemy lokatory:
        # # xpath lokalizujący elementy zawierające nazwy i ceny hoteli:
        # self.hotel_names_xpath = "//h4[contains(@class,'list_title')]//b"
        # self.hotel_prices_xpath = "//div[contains(@class,'price_tab')]//b"

        # definiujemy (mapujemy) lokatory z funkcji search_hotel_test w metodzie init
        # korzystając z klasy zawierającej przeniesione lokatory:
        self.hotel_names_xpath = SearchResultLocators.hotel_names_xpath
        self.hotel_prices_xpath = SearchResultLocators.hotel_prices_xpath

    # funkcja zwracająca listę z nazwami hoteli:
    def get_hotel_names(self):

        # znajdujemy elementy na stronie i wyciągamy tekst z tych elementów:

        hotels = self.driver.find_elements_by_xpath(self.hotel_names_xpath)
        # return [hotel.get_attribute("textContent") for hotel in hotels]

        # zmiana na potrzeby logowania: wycofujemy się z returna w linii wyżej i iterujemy:
        names = [hotel.get_attribute("textContent") for hotel in hotels]
        self.logger.info("Available hotels are: ")
        for name in names:
            self.logger.info(name)
        return names


    # funkcja zwracająca listę z cenami hoteli:
    def get_hotel_prices(self):

        # wyszukujemy elementy z cenami na stronie i wyciągamy tekst z tych elementów zawierający ceny:

        prices = self.driver.find_elements_by_xpath(self.hotel_prices_xpath)
        # return [price.get_attribute("textContent") for price in prices]

        # zmiana na potrzeby logowania: wycofujemy się z returna w linii wyżej i iterujemy:
        hotel_prices = [price.get_attribute("textContent") for price in prices]
        self.logger.info("Prices are: ")
        for price in hotel_prices:
            self.logger.info(price)
        return hotel_prices

        # return aby w teście mozna było dokonać asercji
