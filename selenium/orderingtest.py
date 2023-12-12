from logintest import login  # Importeer de login-functie uit firsttest.py
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

driver = login()  # Roep de <-- //Hergebruikbare test// login-functie aan om de driver te initialiseren

if driver is not None:
    try:
        driver.get("https://testnsg.order4sure.nl")
        
        driver.find_element(By.XPATH,"/html/body/div[1]/section[2]/div/div/div/div[2]/p").click()
        print('Doorverwezen naar pagina')
        driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div[2]/div/div/div[1]/p").click()
        print('Doorverwezen naar pagina')
        driver.find_element("id", "bedrijfnaamnum").send_keys("3065860, Falkena Glas en Schilderwerken")
        
        dropdown_levering = Select(driver.find_element("id", "leverggvns"))
        element_to_scroll = driver.find_element("id", "leverggvns")
        driver.execute_script("arguments[0].scrollIntoView(true);", element_to_scroll)
        time.sleep(2)  
        dropdown_levering.select_by_value("standaard")



        # dropdown_levering =  Select(driver.find_element("id", "leverggvns"))
        # element_to_scroll = driver.find_element("id", "leverggvns").click()
        # time.sleep(2) 
        # driver.execute_script("arguments[0].scrollIntoView(true);", element_to_scroll)
        # dropdown_levering.select_by_value("standaard")

        element_to_scroll = dropdown_groep = Select(driver.find_element("id", "groep[1]"))
        time.sleep(2) 
        driver.execute_script("arguments[0].scrollIntoView(true);", element_to_scroll)
        dropdown_groep.select_by_value("isolat")

        element_to_scroll = dropdown_subgroep = Select(driver.find_element("id", "subgroep[1]"))
        time.sleep(2) 
        dropdown_subgroep.select_by_value("S3")
          
        element_to_scroll = dropdown_opbouw = Select(driver.find_element("id", "opbouw[1]"))
        time.sleep(2) 
        dropdown_opbouw.select_by_value("4-spouw-*4 S3")

        element_to_scroll = dropdown_spouw = Select(driver.find_element("id", "spouw[1]"))
        time.sleep(2) 
        dropdown_spouw.select_by_value("6")

        element_to_scroll = dropdown_spouwtype = Select(driver.find_element("id", "spouwtype[1]"))
        time.sleep(2) 
        dropdown_spouwtype.select_by_value("nothing")

        driver.find_element("id", "aantal[1]").send_keys("4")
        driver.find_element("id", "breedte[1]").send_keys("1500")
        driver.find_element("id", "hoogte[1]").send_keys("1500")

        driver.find_element("id", "submitorderform").click()
        print('Bestelling met succes geplaatst')
    
    except Exception as e:
        print(f'Er is een fout opgetreden: {str(e)}')
    
    finally:
        driver.quit()

















# from firsttest import login  # Importeer de login-functie uit firsttest.py
# from selenium import webdriver
# from selenium.webdriver.support.ui import Select

# driver = login()  # Roep de login-functie aan om de driver te initialiseren

# if driver is not None:
#     try:
#         driver.get("https://testnsg.order4sure.nl")

#     driver.find_element_by_css_selector('p[onclick*="/order/home"]').click(): print('Doorverwezen naar pagina')
#     driver.find_element_by_css_selector('p[onclick*="/order/newOrder"]').click()
#     print('Doorverwezen naar pagina')
#     driver.find_element("id", "bedrijfnaamnum").send_keys("3065860, Falkena Glas en Schilderwerken")
    
#     dropdown_levering =  Select(driver.find_element_by_id("id_leverggvns"))
#     dropdown_levering.select_by_value("standaard")

#     dropdown_groep = Select(driver.find_element_by_id("id_groep[1]"))
#     dropdown_groep.select_by_value("isolat")

#     dropdown_subgroep = Select(driver.find_element_by_id("id_subgroep[1]"))
#     dropdown_subgroep.select_by_value("S3")
      
#     dropdown_opbouw = Select(driver.find_element_by_id("id_opbouw[1]"))
#     dropdown_opbouw.select_by_value("4-spouw-*4 S3")

#     dropdown_spouw = Select(driver.find_element_by_id("id_spouw[1]"))
#     dropdown_spouw.select_by_value("6")

#     dropdown_spouwtype = Select(driver.find_element_by_id("id_spouwtype[1]"))
#     dropdown_spouwtype.select_by_value("nothing")

#     driver.find_element("id", "aantal[1]").send_keys("4")
#     driver.find_element("id", "breedte[1]").send_keys("1500")
#     driver.find_element("id", "hoogte[1]").send_keys("1500")

#     driver.find_element("id", "submitorderform").click()
#     print('Bestelling met succes geplaatst')
    
#     finally:
#         driver.quit() 






# from firsttest import login
# from selenium import webdriver
# from selenium.webdriver.support.ui import Select

# driver = login()

# if driver is not None: 
#  try:
    
#     driver.get("https://testnsg.order4sure.nl")

#     # Verwijder enkele enkele aanhalingstekens uit de CSS-selector
#     if driver.find_element_by_css_selector('p[onclick*="/order/home"]').click(): print('Doorverwezen naar pagina')
#     driver.find_element_by_css_selector('p[onclick*="/order/newOrder"]').click()
#     print('Doorverwezen naar pagina')
#     driver.find_element("id", "bedrijfnaamnum").send_keys("3065860, Falkena Glas en Schilderwerken")
    
#     dropdown_levering =  Select(driver.find_element_by_id("id_leverggvns"))
#     dropdown_levering.select_by_value("standaard")

#     dropdown_groep = Select(driver.find_element_by_id("id_groep[1]"))
#     dropdown_groep.select_by_value("isolat")

#     dropdown_subgroep = Select(driver.find_element_by_id("id_subgroep[1]"))
#     dropdown_subgroep.select_by_value("S3")
      
#     dropdown_opbouw = Select(driver.find_element_by_id("id_opbouw[1]"))
#     dropdown_opbouw.select_by_value("4-spouw-*4 S3")

#     dropdown_spouw = Select(driver.find_element_by_id("id_spouw[1]"))
#     dropdown_spouw.select_by_value("6")

#     dropdown_spouwtype = Select(driver.find_element_by_id("id_spouwtype[1]"))
#     dropdown_spouwtype.select_by_value("nothing")

#     driver.find_element("id", "aantal[1]").send_keys("4")
#     driver.find_element("id", "breedte[1]").send_keys("1500")
#     driver.find_element("id", "hoogte[1]").send_keys("1500")

#     driver.find_element("id", "submitorderform").click()
#     print('Bestelling met succes geplaatst')


# except Exception as e:
#     print("Er is een fout opgetreden: {str(e)}")
 

# finally:
#     driver.quit()
