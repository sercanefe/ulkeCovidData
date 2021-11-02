"""
API ile istenilen ülkenin covid19 verilerini ve genel bilgilerini çekme
"""

import requests

# API
url = "https://covid-api.mmediagroup.fr/v1/cases"

# Datayı dict olarak çekme
response = requests.get(url)
data = response.json()

# Kullanıcıdan ülke alma
country = input("Ülke:")

# Ülke datasını çekme
country_data = data[country.title()]['All']

# Dataları sınıflandırıp değişkenlere atama
population = country_data['population']
confirmed = country_data['confirmed']
deaths = country_data['deaths']
continent = country_data['continent']
location = country_data['location']
capitalCity = country_data['capital_city']
sqKmArea = country_data['sq_km_area']

print("Nüfus:", population)
print("Toplam Vaka:", confirmed)
print("Toplam Ölüm:", deaths)
print("Kıtası:", continent)
print("Konumu:", location)
print("Başkenti:", capitalCity)
print("Yüz ölçümü:", sqKmArea)
