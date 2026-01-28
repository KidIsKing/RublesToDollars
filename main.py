from tkinter import Tk, ttk
from datetime import datetime
from read_statistics import price_old_data, info_is_ready
from url_request import usd_data, eur_data, gbp_data, aed_data, cny_data


price_data = [
    usd_data,
    eur_data,
    gbp_data,
    aed_data,
    cny_data
]
name_of_data = [
    "Доллар США",
    "Евро",
    "Фунт стерлингов",
    "Дирхам ОАЭ",
    "Юань"
]

info_list = []
if info_is_ready:
    for i in range(5):
        if price_old_data[i] != price_data[i]:
            price_delta = price_old_data[i] - price_data[i]
            if price_delta < 0:
                info = "дороже"
            else:
                info = "дешевле"
            info_list.append(
                f"\"{name_of_data[i]}\" изменил цену c "
                f"{price_old_data[i]} руб. на {price_data[i]} руб. "
                f"Стало {info} на: {abs(price_delta):.3f} руб."
            )
        else:
            info_list.append(f"Изменений цены для \"{name_of_data[i]}\" нет.")
else:
    print("Для анализа курсов валют информации недостаточно...")

now = datetime.strftime(datetime.now(), "%H:%M:%S %d.%m.%Y")

with open("statistics.txt", "a", encoding="utf-8") as file:
    file.write(
        f"=========== Дата: {now}. ===========\n"
        f"{usd_data} руб. - доллар США.\n"
        f"{eur_data} руб. - евро.\n"
        f"{gbp_data} руб. - фунт стерлингов.\n"
        f"{aed_data} руб. - дирхам ОАЭ.\n"
        f"{cny_data} руб. - юань.\n"
    )
    if info_is_ready:
        file.write("============ Информация об изменениях ============\n")
        for info in info_list:
            file.write(
                f"{info}\n"
            )
        file.write(
                "========== Информация от Центробанка РФ ==========\n\n\n"
            )

root = Tk()
frm = ttk.Frame(root, padding=40)
frm.grid()

ttk.Label(frm, text=f"Доллар США: {usd_data} руб.").grid(column=0, row=0)
ttk.Label(frm, text=f"Евро: {eur_data} руб.").grid(column=0, row=1)
ttk.Label(frm, text=f"Фунт стерлингов: {gbp_data} руб.").grid(column=0, row=2)
ttk.Label(frm, text=f"Дирхам ОАЭ: {aed_data} руб.").grid(column=0, row=3)
ttk.Label(frm, text=f"Юань: {cny_data} руб.").grid(column=0, row=4)

ttk.Label(frm, text="Информация с сайта Центробанка РФ.").grid(column=0, row=6)
root.mainloop()
