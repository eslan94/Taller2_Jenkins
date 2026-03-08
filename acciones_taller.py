from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class AccionesTaller:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def login_portal(self):
        self.driver.get("https://webdriveruniversity.com/Login-Portal/index.html")
        
        credenciales = [("esteban_pro", "clave123"), ("admin", "admin456")]
        
        for usuario, clave in credenciales:
            self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="text"]'))).send_keys(usuario)
            self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(clave)
            self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
            
            alerta = self.wait.until(EC.alert_is_present())
            alerta.accept()
            self.driver.refresh()

    def gestionar_todo_list(self):
        self.driver.get("https://webdriveruniversity.com/To-Do-List/index.html")
        
        tarea = "Aprender Selenium Modular"
        
        input_tarea = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "input")))
        input_tarea.send_keys(tarea + "\n")
        
        xpath_tarea = f"//li[contains(text(), '{tarea}')]"
        elemento_tarea = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath_tarea)))
        elemento_tarea.click()
        
        basurero = self.driver.find_element(By.XPATH, f"{xpath_tarea}/span/i")
        self.driver.execute_script("arguments[0].click();", basurero)
        
        self.wait.until(EC.invisibility_of_element_located((By.XPATH, xpath_tarea)))
        print("Tarea gestionada y validada correctamente.")

    def configurar_dropdowns(self):
        self.driver.get("https://webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html")
        
        dropdown = Select(self.wait.until(EC.presence_of_element_located((By.ID, "dropdowm-menu-1"))))
        
        dropdown.select_by_visible_text("Python")
        dropdown.select_by_value("sql")
        dropdown.select_by_index(2)

    def manejar_iframes_y_popups(self):

        self.driver.get("https://webdriveruniversity.com/IFrame/index.html")
        self.wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "frame")))

        self.driver.find_element(By.ID, "button-find-out-more").click()
        
        self.driver.switch_to.default_content()

        self.driver.get("https://webdriveruniversity.com/Popup-Alerts/index.html")
        
     
        self.driver.find_element(By.ID, "button1").click()
        alerta = self.wait.until(EC.alert_is_present())
        alerta.accept()

        self.driver.find_element(By.ID, "button4").click()
        confirm = self.driver.switch_to.alert
        confirm.dismiss()
