# tworzymy klasę, która w zależności od podanych danych uruchomi chrome lub firefox
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class DriverFactory:

    # na początku dodajemy dekorator @staticmethod, który mówi, ze to metoda statyczna,
    # która nie wymaga tworzenia obiektu klasy aby ją wywołać. Dzięki temu mozna usunąć
    # self z argumentów
    @staticmethod
    def get_driver(browser):
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            return webdriver.Chrome(ChromeDriverManager().install(), options=options)
        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument("start-maximized")
            return webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
        # jezeli ani to ani to to wywal info:
        raise Exception("Provide valid driver name")