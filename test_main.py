import pytest_html_reporter
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
options.add_experimental_option("detach", True)


def test_LogInFallido():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get('http://127.0.0.1:5500/index.html')

    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.ID,
                                           "login"))) \
        .click()

    time.sleep(1)
    wait.until(EC.element_to_be_clickable((By.ID,
                                           "usuario"))) \
        .send_keys('micha3lol')

    wait.until(EC.element_to_be_clickable((By.ID,
                                           "contraseña"))) \
        .send_keys('m2692004+')

    time.sleep(2)
    driver.save_screenshot("resultados/login_success.png")
    wait.until(EC.element_to_be_clickable((By.ID,
                                           "ingresar"))) \
        .click()
    wait.until(EC.element_to_be_clickable((By.ID,
                                           "index"))) \
        .click()


def test_paginacion():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get('http://127.0.0.1:5500/index.html')

    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.ID,
                                           "catalogo"))) \
        .click()
    time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                           "i.fas.fa-angle-right"))) \
        .click()
    time.sleep(1)
    driver.save_screenshot("resultados/navegacion.png")
    time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                           "i.fas.fa-angle-left"))) \
        .click()

    time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.ID,
                                           "4"))) \
        .click()
    time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.ID,
                                           "index"))) \
        .click()


def test_peliculas():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get('http://127.0.0.1:5500/index.html')

    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.ID,
                                           "1"))) \
        .click()
    time.sleep(3)
    wait.until(EC.element_to_be_clickable((By.ID,
                                           "3"))) \
        .click()
    time.sleep(3)
    wait.until(EC.element_to_be_clickable((By.ID,
                                           "5"))) \
        .click()
    driver.save_screenshot("resultados/peliculas.png")
    time.sleep(3)
    wait.until(EC.element_to_be_clickable((By.ID,
                                           "index"))) \
        .click()


def test_trailerRep():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get('http://127.0.0.1:5500/index.html')

    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.ID,
                                           "catalogo"))) \
        .click()
    time.sleep(5)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                           "div.peliculaa"))) \
        .click()
    time.sleep(3)
    driver.save_screenshot("resultados/peliculas.png")
    time.sleep(5)
    wait.until(EC.element_to_be_clickable((By.ID,
                                           "index"))) \
        .click()

    time.sleep(4)
    driver.save_screenshot("resultados/trailer_reproducido.png")


def test_agregar():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get('http://127.0.0.1:5500/admin/agregar.html')

    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.ID,
                                           "Titulo"))) \
        .send_keys('El principito')

    time.sleep(1)
    wait.until(EC.element_to_be_clickable((By.ID,
                                           "Director"))) \
        .send_keys('Giovanni')

    time.sleep(1)
    wait.until(EC.element_to_be_clickable((By.ID,
                                           "Sinopsis"))) \
        .send_keys('texto de prueba')

    time.sleep(1)
    wait.until(EC.element_to_be_clickable((By.ID,
                                           "Reparto"))) \
        .send_keys('texto de prueba')

    time.sleep(1)
    wait.until(EC.element_to_be_clickable((By.ID,
                                           "Duracion"))) \
        .send_keys('texto de prueba')

    time.sleep(1)
    wait.until(EC.element_to_be_clickable((By.ID,
                                           "Generos"))) \
        .send_keys('texto de prueba')

    time.sleep(1)
    wait.until(EC.element_to_be_clickable((By.ID,
                                           "Fecha"))) \
        .send_keys('texto de prueba')
    time.sleep(1)
    wait.until(EC.element_to_be_clickable((By.ID,
                                           "YT"))) \
        .send_keys('texto de prueba')

    driver.save_screenshot("resultados/agregado_pelicula.png")
    time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.ID,
                                           "Agregar"))) \
        .click()
    time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.ID,
                                           "index"))) \
        .click()