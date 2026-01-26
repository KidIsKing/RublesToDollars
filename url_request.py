import requests


response = requests.get(
    "https://www.cbr-xml-daily.ru/daily_json.js",
    timeout=5  # ждать ответа не более 5 секунд
    )
# Преобразуем ответ страницы html в .json формат.
data = response.json()
# Из данных страницы находим по ключам словаря .json нужное значение
usd_data = data["Valute"]["USD"]["Value"]

if __name__ == "__main__":
    print(f"Доллар США: {usd_data} руб.")
