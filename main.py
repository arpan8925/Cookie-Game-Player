import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

value = driver.find_element(By.ID, "money")





def buy_item():
    cursor_price = int(driver.find_element(By.ID, "buyCursor").text.split()[2])
    print(cursor_price)
    grandma_price = int(driver.find_element(By.ID, "buyGrandma").text.split()[2])
    print(grandma_price)
    factory_price = int(driver.find_element(By.ID, "buyFactory").text.split()[2])
    print(factory_price)
    shipment_price = int(driver.find_element(By.ID, "buyShipment").text.split()[2].replace(",", ""))
    print(shipment_price)
    alchemy_lab_price = int(driver.find_element(By.ID, "buyAlchemy lab").text.split()[3].replace(",", ""))
    print(alchemy_lab_price)
    portal_price = int(driver.find_element(By.ID, "buyPortal").text.split()[2].replace(",", ""))
    print(portal_price)
    time_machine_price = int(driver.find_element(By.ID, "buyTime machine").text.split()[3].replace(",", ""))
    print(time_machine_price)
    # delay = 60*60
    # close_time = time.time()+delay
    # if time.time() < close_time:
    value = driver.find_element(By.ID, "money")
    money = int(value.text)  
    if money < cursor_price:
        return
    elif money >= cursor_price and money < grandma_price:
        buy_cursor = driver.find_element(By.ID, "buyCursor")
        buy_cursor.click()

    elif money >= grandma_price and money < factory_price:
        buy_cursor = driver.find_element(By.ID, "buyGrandma")
        buy_cursor.click()

    elif money >= factory_price and money < shipment_price:
        buy_cursor = driver.find_element(By.ID, "buyFactory")
        buy_cursor.click()

    elif money >= shipment_price and money < alchemy_lab_price:
        buy_cursor = driver.find_element(By.ID, "buyShipment")
        buy_cursor.click()
        
    elif money >= alchemy_lab_price and money < portal_price:
        buy_cursor = driver.find_element(By.ID, "buyAlchemy lab")
        buy_cursor.click()

    elif money >= portal_price and money < time_machine_price:
        buy_cursor = driver.find_element(By.ID, "buyPortal")
        buy_cursor.click()

    elif money >= time_machine_price:
        buy_cursor = driver.find_element(By.ID, "buyTime machine")
        buy_cursor.click()
    else:
        buy_item()




while True:
    try:
        buy_item()
        cookie = driver.find_element(By.ID, "cookie")
        cookie.click()
    except Exception as e:
        print(f"An error occurred: {e}")
        break







    
    

