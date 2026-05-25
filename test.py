import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Baca Excel
file_excel = r"C:\Users\ratna\OneDrive\Desktop\template_entry_kunjungan.xlsx"
data = pd.read_excel(file_excel)

# Ambil pasien pertama
pasien = data.iloc[0]

# Buka Chrome
driver = webdriver.Chrome()

# Buka website BPJS
driver.get("https://pcarejkn.bpjs-kesehatan.go.id/eclaim/")

print("Silakan login dulu...")
time.sleep(20)

print("Nama pasien dari Excel:")
print(pasien["Nama Pasien"])

# Chrome tetap terbuka
input("Tekan ENTER untuk menutup browser...")

driver.quit()
