"""
Page Object Pattern
Wykorzystamy go po to, aby nie kopiować kodu dot. hoteli aby znaleźć dane dla innego
miasta, pasażera czy daty. Ponadto testy mogą failować z powodu zmiany nazw selektorów.
"""

# w ramach przeniesienia lokatorów do oddzielnego pliku, importujemy klasę je zawierającą:
from page_object_pattern.locators.locators import SearchHotelLocators

# dodajemy loggera - na jego podstawie będziemy znali wprowadzone wartości oraz problemy z wyszukaniem
import logging


# tworzymy klasę:
class SearchHotelPage:

    # tworzymy metodę init, w której przekazujemy drivera, aby móc się do niego odnosić w innych funkcjach
    def __init__(self, driver):
        self.driver = driver

        # dodajemy logger:
        self.logger = logging.getLogger(__name__)


        # definiujemy (mapujemy) lokatory z funkcji search_hotel_test w metodzie init:

        # self.search_hotel_span_xpath = "//span[text()='Search by Hotel or City Name']"
        # self.search_hotel_input_xpath = "//div[@id='select2-drop']//input"
        # self.location_match_span_xpath = "//span[text()='Dubai']"
        # self.check_in_input_name = "checkin"
        # self.check_out_input_name = "checkout"
        # self.travellers_input_id = "travellersInput"
        # self.adult_input_id = "adultInput"
        # self.child_input_id = "childInput"
        # self.search_button_xpath = "//button[text()=' Search']"

        # Metoda 1 - mapowanie korzystając z klasy zawierającej przeniesione lokatory:
        self.search_hotel_span_xpath = SearchHotelLocators.search_hotel_span_xpath
        self.search_hotel_input_xpath = SearchHotelLocators.search_hotel_input_xpath
        self.location_match_span_xpath = SearchHotelLocators.location_match_span_xpath
        self.check_in_input_name = SearchHotelLocators.check_in_input_name
        self.check_out_input_name = SearchHotelLocators.check_out_input_name
        self.travellers_input_id = SearchHotelLocators.travellers_input_id
        self.adult_input_id = SearchHotelLocators.adult_input_id
        self.child_input_id = SearchHotelLocators.child_input_id
        self.search_button_xpath = SearchHotelLocators.search_button_xpath

        # Metoda 2 - można usunąć pola w init i odwoływać się do pól klas z przeniesionymi lokatorami
        # bezpośrednio w metodach

    # tworzymy funkcję wyboru miasta ze zmapowanymi lokatorami:
    def set_city(self, city):

        # dodajemy logger:
        # zapis jak ponizej zamieni nawias klamrowy na wartość zmiennej city:
        self.logger.info("Setting city {}".format(city))

        # klikamy na pole z nazwą miasta:
        self.driver.find_element_by_xpath(self.search_hotel_span_xpath).click()

        # wpisujemy nazwę miasta do pola tekstowego (argument city, a nie na sztywno Dubai):
        self.driver.find_element_by_xpath(self.search_hotel_input_xpath).send_keys(city)

        # klikamy na match (podpowiedź miasta):
        self.driver.find_element_by_xpath(self.location_match_span_xpath).click()

    # tworzymy funkcję ustawiania zakresu pobytu ze zmapowanymi lokatorami:
    def set_date_range(self, check_in, check_out):

        # dodajemy logger:
        self.logger.info("Setting check in {checkin} and {checkout} dates".format(checkin=check_in, checkout=check_out))

        # ustawiamy datę przyjazdu:
        self.driver.find_element_by_name(self.check_in_input_name).send_keys(check_in)

        # ustawiamy datę powrotu:
        self.driver.find_element_by_name(self.check_out_input_name).send_keys(check_out)

    # ustawiamy liczbę dzieci i dorosłych:
    def set_travellers(self, adults, child):

        # dodajemy logger:
        self.logger.info("Setting travellers adults - {adults} and children - {kids}".format(adults=adults, kids=child))

        # ustawienie liczby podróżnych - klik na pole:
        self.driver.find_element_by_id(self.travellers_input_id).click()

        # liczba podróżnych - wyczyszcenie pola i wpisanie liczby:
        self.driver.find_element_by_id(self.adult_input_id).clear()
        self.driver.find_element_by_id(self.adult_input_id).send_keys(adults)
        self.driver.find_element_by_id(self.child_input_id).clear()
        self.driver.find_element_by_id(self.child_input_id).send_keys(child)

    # klikamy na przycisk wyszukiwania:
    def perform_search(self):

        # dodajemy logger, ze wykonujemy wyszkiwanie:
        self.logger.info("Performing search")

        # klikamy na przycisk search - za pomocą tekstu Search
        self.driver.find_element_by_xpath(self.search_button_xpath).click()

