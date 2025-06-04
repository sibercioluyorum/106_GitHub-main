import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import Workbook

options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36")
driver_path = r'C:\Selenium\chromedriver.exe'
service = Service(driver_path)
browser = webdriver.Chrome(service=service, options=options)
browser.get('https://www.nytimes.com/search?dropmab=false&endDate=2022-03-03&lang=en&query=&sort=oldest&startDate=2015-11-01')
time.sleep(2)
wait = WebDriverWait(browser, 10)

# Excel workbook and sheet setup
workbook = Workbook()
sheet = workbook.active
sheet.title = "NYTimes Data"
sheet.append(["Başlık", "Kategori", "İçerik"])  # Column headers

# Set to keep track of unique titles
unique_titles = set()


def veriAl():
    previous_haber_count = 0

    while True:
        haber_elements = browser.find_elements(By.CLASS_NAME, "css-e1lvw9")
        current_haber_count = len(haber_elements)

        # Only process new articles
        for i in range(previous_haber_count, current_haber_count):
            haber_element = haber_elements[i]
            try:
                haber_baslik = haber_element.find_element(By.TAG_NAME, "h4").text
                haber_kategori = haber_element.find_element(By.TAG_NAME, "p").text

                # İçeriği bulurken alternatif bir yol kullanıyoruz.
                try:
                    haber_icerik = haber_element.find_element(By.XPATH, ".//p[contains(@class, 'css-16nhkrn')]").text
                except:
                    haber_icerik = ""  # İçerik bulunamazsa boş bırak

                # Aynı başlıktan tekrar eklememek için kontrol
                if haber_baslik in unique_titles:
                    continue
                unique_titles.add(haber_baslik)

                # Veriyi ekrana yazdır ve Excel'e kaydet
                print("Başlık:", haber_baslik)
                print("Kategori:", haber_kategori)
                print("İçerik:", haber_icerik)
                print("-" * 20)

                sheet.append([haber_baslik, haber_kategori, haber_icerik])

            except Exception as e:
                print("Veri alınamadı:", e)
                continue

        # Update the count of processed articles
        previous_haber_count = current_haber_count

        # Save data every 10 new articles to avoid frequent saving
        if current_haber_count % 10 == 0:
            workbook.save("NYTimesData2.9.xlsx")

        # 'Show More' butonunu bul ve tıkla
        try:
            show_more_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Show More')]"))
            )
            browser.execute_script("arguments[0].scrollIntoView();", show_more_button)
            show_more_button.click()


        except Exception as e:
            print("No more articles to load or 'Show More' button not found:", e)
            break

    # Final save after loop
    workbook.save("NYTimesData2.9.xlsx")


veriAl()
