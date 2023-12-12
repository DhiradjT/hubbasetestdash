import3222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                

from selenium import webdriver
from selenium.webdriver.common.by import By

def login():
    driver = webdriver.Firefox()
    try:
        driver.get("https://testnsg.order4sure.nl")
        if driver.find_element("id", "submit_button").is_displayed():
            driver.find_element("id", "username").send_keys("Hubbase_stage")
            driver.find_element("id", "password").send_keys("logistics")
            driver.find_element("id", "submit_button").click()
            driver.implicitly_wait(10)
            akkoord_button = driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/div/div/div/div/div/div/div/div[4]/button")
            akkoord_button.click()
            print('login succes') 
        return driver 
    except Exception as e:
        print(f'Er is een fout opgetreden: {str(e)}')
        return None
    finally:
        # driver.quit() Hier de driver niet sluiten in firsttest.py, zodat deze beschikbaar blijft voor andere tests
        pass  # Zet driver.quit() uit

# Zorg ervoor dat de inlogfunctie alleen wordt uitgevoerd als firsttest.py zelf wordt uitgevoerd
if __name__ == "__main__":
    login()

















# from selenium import webdriver

# # Defineer de login-functie
# def login():
#     # Initialiseer de Selenium-webdriver (kies de gewenste browser)
# driver = webdriver.Firefox()

# try:
#         # Navigeer naar de inlogpagina
#         driver.get("https://testnsg.order4sure.nl")

#         # Controleer of de inlogknop aanwezig is (dit kan variëren afhankelijk van de website)
#         if driver.find_element("id", "submit_button").is_displayed():
#             # Voer de inlogstappen uit (bijvoorbeeld invullen van gebruikersnaam en wachtwoord)
#             driver.find_element("id", "username").send_keys("Hubbase_stage")
#             driver.find_element("id", "password").send_keys("logistics")
#             driver.find_element("id", "submit_button").click()
#             print('login succes')
#             return driver
# except Exception as e:
#        print(f'Er is een fout opgetreden: {str(e)}')
#     return None            
        
#             # Hier kun je verdere stappen van je test uitvoeren nadat je bent ingelogd
#     #         return driver
#     # except Exception as e:
#     #     print(f'Er is een fout opgetreden: {str(e)}')
#     #     return None
    
# finally:
#         pass
#         # Sluit de browser altijd, ongeacht of er een fout is opgetreden of niet

# # Voeg een if-statement toe om de login-functie alleen uit te voeren als firsttest.py direct wordt uitgevoerd
# if __name__ == "__main__":
#     login()