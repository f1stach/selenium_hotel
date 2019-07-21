from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://www.kurs-selenium.pl/demo/")

# wprowadzamy nazwę miasta do wyszukiwarki:
driver.find_element_by_xpath("//span[text()='Search by Hotel or City Name']").click()

# lokalizujemy input za pomocą id diva nadrzędnego i przechodzimy do klasy niżej:
driver.find_element_by_xpath("//div[@id='select2-drop']//input").send_keys("Dubai")

# potwierdzamy, że to ten Dubai co trzeba (czyli symulujemy klik na podpowiedź) czyli
# szukamy po span, który ma konkretny tekst Dubai:
driver.find_element_by_xpath("//span[text()='Dubai']").click()

# data zameldowania i wymeldowania - metoda 1:
# lokalizujemy element po name i wysyłamy do inputa (pola tekstowego) daty:
driver.find_element_by_name("checkin").send_keys("28/07/2019")
driver.find_element_by_name("checkout").send_keys("31/07/2019")

"""
# data zameldowania i wymeldowania - metoda 2:
# lokalizujemy pole, klikamy i szukamy konkretnego pola w kalendarzu:
driver.find_element_by_name("checkin").click()
driver.find_element_by_xpath("//td[@class='day ' and text()='28']").click()

# przed wyborem daty wymeldowania sprawdzamy długość listy elementów pola w kalendarzu:
# print(len(driver.find_elements_by_xpath("//td[@class='day ' and text()='31']")))
elementy = driver.find_elements_by_xpath("//td[@class='day ' and text()='31']")

# output pokazał 7 elementów więc iterujemy po nich i wybierzemy jeden:
for element in elementy:
    if element.is_displayed():
        element.click()
        break

driver.find_element_by_xpath("//td[@class='day ' and text()='31']").click()
"""

# ustawienie liczby podróżnych - klik na pole:
driver.find_element_by_id("travellersInput").click()

# liczba podróżnych - wyczyszcenie pola i wpisanie liczby:
driver.find_element_by_id("adultInput").clear()
driver.find_element_by_id("adultInput").send_keys("4")
driver.find_element_by_id("childInput").clear()
driver.find_element_by_id("childInput").send_keys("4")

# klikamy na przycisk search - za pomocą tekstu Search
driver.find_element_by_xpath("//button[text()=' Search']").click()

# pobieramy listę nazw hoteli z wyników wyszukiwania - tag h4 jest nadrzędny dla tagu b, który zawiera
# tekst z nazwą hotelu. Wszystkie nazwy hoteli dostaniemy używając atrybutu textContent
hotels = driver.find_elements_by_xpath("//h4[contains(@class,'list_title')]//b")
hotel_names = [hotel.get_attribute("textContent") for hotel in hotels]

# wypisujemy nazwy hoteli w konsoli:
for name in hotel_names:
    print("Hotel name: " + name)


# pobieramy i wypisujemy ceny hoteli:
# cena jest w tagu b, wyzej jest div class, a jeszcze wyzej div class = price_tab
prices  = driver.find_elements_by_xpath("//div[contains(@class,'price_tab')]//b")
price_values = [price.get_attribute("textContent") for price in prices]

for price in price_values:
    print("Cena to: " + price)

# sprawdzamy poprawność nazw i cen za pomocą asercji:
assert hotel_names[0] == "Jumeirah Beach Hotel"
assert hotel_names[1] == "Oasis Beach Tower"
assert hotel_names[2] == "Rose Rayhaan Rotana"
assert hotel_names[3] == "Hyatt Regency Perth"

assert price_values[0] == "$22"
assert price_values[1] == "$50"
assert price_values[2] == "$80"
assert price_values[3] == "$150"

driver.quit()

