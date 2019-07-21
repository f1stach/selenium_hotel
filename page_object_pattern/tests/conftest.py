"""
Współdzielenie metody setup() -> metoda 2.
Metoda setup zawarta jest w specjalnym pliku conftest.
Nie tworzymy tutaj klasy.
"""
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from page_object_pattern.utils.driver_factory import DriverFactory


# tworzymy setupową metodę, w niej tworzymy przeglądarkę i zamykamy ją
# dodatkowo jako argument przyjmuje parametr request, do którego w ciele przypisujemy
# zmienną driver - po to aby funkcje testowe nie pluły się o brak drivera.

@pytest.fixture()
def setup(request):
    # driver = webdriver.Chrome(ChromeDriverManager().install())

    # nie chcemy na sztywno wywoływać Chrome, tylko dac wybór więc korzystamy z DriverFacotry:

    driver = DriverFactory.get_driver("chrome")

    driver.implicitly_wait(10)
    # driver.maximize_window()
    request.cls.driver = driver

    # # dodajemy opcję wykonywania prtscr gdy test zostanie zakonczony niepowodzeniem
    # # najpierw sprawdzamy ile mamy testów, które zakonczyły się niepowodzeniem:
    # before_failed = request.session.testsfailed

    yield

    # # po tym jak metoda zostanie wykonana, sprawdzamy czy liczba obecnie failed testów
    # # jest różna od liczby sprzed metody testowej. Jeżeli różna to fail.
    # if request.session.testsfailed != before_failed:
    #     allure.attach(driver.get_screenshot_as_png(), name="Test failed", attachment_type=AttachmentType.PNG)
    # po złożeniu kodu powyżej wykonać polecenie terminala dot. allure aby wygenerowac raport ze screenem

    driver.quit()
