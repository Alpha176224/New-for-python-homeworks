# Task 1: Weather HTML parsing
from bs4 import BeautifulSoup

with open("weather.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

rows = soup.find("table").find("tbody").find_all("tr")
weather_data = []

for row in rows:
    cols = row.find_all("td")
    day = cols[0].text
    temp = int(cols[1].text.replace("°C", ""))
    condition = cols[2].text
    weather_data.append({"day": day, "temperature": temp, "condition": condition})
    print(f"{day}: {temp}°C, {condition}")

max_temp = max(weather_data, key=lambda x: x["temperature"])["temperature"]
max_temp_days = [d["day"] for d in weather_data if d["temperature"] == max_temp]
sunny_days = [d["day"] for d in weather_data if d["condition"] == "Sunny"]

print("\nDay(s) with the highest temperature:", ", ".join(max_temp_days))
print("Sunny day(s):", ", ".join(sunny_days))

avg_temp = sum(d["temperature"] for d in weather_data) / len(weather_data)
print("Average temperature:", round(avg_temp, 2), "°C")
