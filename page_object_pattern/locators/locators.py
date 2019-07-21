"""
Przenoszenie lokatorów do oddzielnego pliku
Przenoszenie lokatorów do oddzielnego pliku jest promowane jako dobra praktyka dla testów Selenium w
Pythonie (opisana w dokumentacji i powielana w wielu opracowaniach).

O ile taki kod jest stosunkowo łatwy do utrzymania przy małych projektach, to dla większej aplikacji
utrzymanie selektorów w innym miejscu niż page object robi się problematyczne. Mimo wszystko lokatory
i metody są ze sobą ściśle powiązane i łatwiej jest je trzymać w jednej klasie

Dlatego mimo, że pokazuje jak wydzielać lokatory do oddzielnego pliku to zachęcam do unikania tej
praktyki i trzymania lokatorów i metod w jednej klasie .

W projektach komercyjnych bardzo rzadko spotykałem się z lokatorami w oddzielnym pliku, ale chciałbym
abyś miał/a świadomość, że istnieje taka możliwość i jeżeli zobaczysz taki kod to nie będzie on dla
Ciebie zaskoczeniem.
"""


# klasa dla lokatorów:
class SearchHotelLocators:

    search_hotel_span_xpath = "//span[text()='Search by Hotel or City Name']"
    search_hotel_input_xpath = "//div[@id='select2-drop']//input"
    location_match_span_xpath = "//span[text()='Dubai']"
    check_in_input_name = "checkin"
    check_out_input_name = "checkout"
    travellers_input_id = "travellersInput"
    adult_input_id = "adultInput"
    child_input_id = "childInput"
    search_button_xpath = "//button[text()=' Search']"


# druga klasa dla wynikow wyyszukiwania:
class SearchResultLocators:

    hotel_names_xpath = "//h4[contains(@class,'list_title')]//b"
    hotel_prices_xpath = "//div[contains(@class,'price_tab')]//b"
