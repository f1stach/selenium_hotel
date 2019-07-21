import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from page_object_pattern.pages.search_hotel import SearchHotelPage
from page_object_pattern.pages.search_results import SearchResultsPage
import allure
# from page_object_pattern.tests.base_test import BaseTest


# robimy tutaj analogicznie jak w test_hotel_search:
# aby uzywac metody setup() z base_test używamy poniższego fixture z nazwą metody setup w argumencie.
# Rozszerzamy też klasę BaseTest za pomocą klasy TestHotelSearch dorzucając argument (BaseTest).

@pytest.mark.usefixtures("setup")
# class TestHotelSearch(BaseTest): # metoda nr 1 dla setup - rozszerzenie klasy BaseTest
class TestHotelSearch:  # metoda nr 2 dla setup - tylko setup w fixture, bez rozszerzania klasy

    # Wyrzucamy stąd metodę setup, bo jest zawarta w pliku base_test jako dostępna dla wielu plików.

    # # tworzymy setupową metodę, w niej tworzymy przeglądarkę i zamykamy ją
    # @pytest.fixture()
    # def setup(self):
    #     self.driver = webdriver.Chrome(ChromeDriverManager().install())
    #     self.driver.implicitly_wait(10)
    #     self.driver.maximize_window()
    #     yield
    #     self.driver.quit()

    # tworzymy metodę testową:

    def test_hotel_search(self, setup):
        # otwieramy stronę:
        self.driver.get("http://www.kurs-selenium.pl/demo/")

        # tworzymy nowy obiekt klasy SearchHotelPage
        search_hotel_page = SearchHotelPage(self.driver)
        search_hotel_page.set_city("Dubai")
        search_hotel_page.set_date_range("28/07/2019", "31/07/2019")
        search_hotel_page.set_travellers("2", "2")
        search_hotel_page.perform_search()

        # Weryfikacja wyników wszysukiwania za pomocą asercji:
        results_page = SearchResultsPage(self.driver)
        hotel_names = results_page.get_hotel_names()
        price_values = results_page.get_hotel_prices()

        # dodajemy asercje aby potwierdzić prawdziwość pobranych danych (kopia z pierwotnego pliku):
        assert hotel_names[0] == "Jumeirah Beach Hotel"
        assert hotel_names[1] == "Oasis Beach Tower"
        assert hotel_names[2] == "Rose Rayhaan Rotana"
        assert hotel_names[3] == "Hyatt Regency Perth"

        assert price_values[0] == "$22"
        assert price_values[1] == "$50"
        assert price_values[2] == "$80"
        assert price_values[3] == "$150"
