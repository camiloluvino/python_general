#%%
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import xlwings as xl

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

#%%

driver = webdriver.Chrome(executable_path= "chromedriver\chromedriver.exe")
url = "https://www.portalinmobiliario.com/arriendo/departamento/valparaiso"

driver.get(url)
time.sleep(2)
# xpath = "/html/body/main/div/div[2]/section/div[5]/ul/li[3]"
clase_precio = "price-tag-fraction"
clase_unidad = "price-tag-symbol"
clase_m2 = "ui-search-card-attributes__attribute"
clase_direccion = "ui-search-item__group__element.ui-search-item__location.shops__items-group-details"

# clase_boton = "andes-pagination__arrow-title"
clase_boton = "andes-dropdown__trigger"
clase_boton_2 = "andes-list__item.andes-list__item--size-compact"

boton = driver.find_element(By.CLASS_NAME, clase_boton)
boton.click()
time.sleep(1)
lista = driver.find_elements(By.CLASS_NAME, clase_boton_2)
textos = [element.text for element in lista]
lista[3].click()
time.sleep(2)

lista = driver.find_elements(By.CLASS_NAME, clase_precio)
precio = [element.text for element in lista]

lista = driver.find_elements(By.CLASS_NAME, clase_unidad)
unidad = [element.text for element in lista]

lista = driver.find_elements(By.CLASS_NAME, clase_m2)
metros = [element.text for element in lista]

lista = driver.find_elements(By.CLASS_NAME, clase_direccion)
ubicacion = [element.text for element in lista]

# necesito sacar el link para añadirlo

# andes-list andes-floating-menu andes-list--default andes-list--selectable

# element = driver.find_element(By.LINK_TEXT, "Siguiente")

# actions = ActionChains(driver)
# actions.move_to_element(element).click().perform()
# # element.click()

# # time.sleep(2)
# lista = driver.find_elements(By.CLASS_NAME, clase_precio)
# precio1 = [element.text for element in lista]

# lista = driver.find_elements(By.CLASS_NAME, clase_m2)
# m21 = [element.text for element in lista]


# precio = precio + precio1
# m2 = m2+m21

driver.close()    


#%%
i=0
metros_datos = []

while i<len(metros):
    aux = metros[i]
    metros_datos.append(aux)
    i+=2
    
i=1
dorm_datos = []
while i<len(metros):
    aux = metros[i]
    dorm_datos.append(aux)
    i+=2
    
datos = {"precio": precio,
         "unidad": unidad,
         "ubicacion": ubicacion,
         "metros": metros_datos,
         "dormitorio": dorm_datos,}    
df = pd.DataFrame(datos)

xl.view(df)

#%%