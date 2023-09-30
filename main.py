from selenium import webdriver
from selenium.webdriver.common.by import By
from db import MongoDriver



driver = webdriver.Chrome()
driver.get("https://deporspeed.com/")
search_box = driver.find_element(by=By.CSS_SELECTOR, value="#second-site-navigation > div > div > form > input.header-search-input")
search_box.send_keys("Head")

search_button = driver.find_element(by=By.CSS_SELECTOR, value="#second-site-navigation > div > div > form > button > i")
search_button.click()

Raqueta = driver.find_elements(By.CSS_SELECTOR, "#site-content > div > div > article")

mongodb = MongoDriver()

for card in Raqueta:
    try:
        Nombre = card.find_element(By.CSS_SELECTOR, "#site-content > div > div > article > ul > li.product.type-product.post-2795.status-publish.first.instock.product_cat-raquetas-jr-raquetas.has-post-thumbnail.sale.taxable.shipping-taxable.purchasable.product-type-simple > a.woocommerce-LoopProduct-link.woocommerce-loop-product__link > h2").text
        Precio = card.find_element(By.CSS_SELECTOR, "#site-content > div > div > article > ul > li.product.type-product.post-2795.status-publish.first.instock.product_cat-raquetas-jr-raquetas.has-post-thumbnail.sale.taxable.shipping-taxable.purchasable.product-type-simple > a.woocommerce-LoopProduct-link.woocommerce-loop-product__link > span.price > ins > span > bdi").text
        print(Nombre)
        print(Precio)


        Productos = {
            "Nombre": Nombre,
            "Precio": Precio,
        }

        mongodb.insert_record(record=Productos, username="Adriana")

        print("*********")
    except Exception as e:
        print(e)
        print("*********")


driver.close()
