# """
# Współdzielenie metody setup() -> metoda 1.
# Ten plik stworzyliśmy po to, aby zawrzeć w nim metodę setup(), która będzie mogłą być używana
# w innych plikach testowych, bez jej ponownego definiowania z osobna.
# """
# import pytest
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
#
#
# class BaseTest:
#
#     # tworzymy setupową metodę, w niej tworzymy przeglądarkę i zamykamy ją
#
#     @pytest.fixture()
#     def setup(self):
#         self.driver = webdriver.Chrome(ChromeDriverManager().install())
#         self.driver.implicitly_wait(10)
#         self.driver.maximize_window()
#         yield
#         self.driver.quit()

# Wykomentowane na potrzeby sprawdzenia funkcjonalności metody nr 2. (czyli conftest)
