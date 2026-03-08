
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from acciones_taller import AccionesTaller
import time

ruta_driver = "msedgedriver.exe"
service = Service(executable_path=ruta_driver)

driver = webdriver.Edge(service=service)
driver.maximize_window()

taller = AccionesTaller(driver)

try:    
    taller.login_portal()
    taller.gestionar_todo_list()
    taller.configurar_dropdowns()
    taller.manejar_iframes_y_popups()

finally:
    
    time.sleep(10)
    driver.quit()