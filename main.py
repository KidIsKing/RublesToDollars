from tkinter import Tk, ttk
from datetime import datetime
from read_statistics import old_valutes_of_data, info_is_ready
from url_request import name_of_data, valutes_of_data


info_list = []
if info_is_ready:
    for i in range(5):
        if old_valutes_of_data[i] != valutes_of_data[i]:
            price_delta = old_valutes_of_data[i] - valutes_of_data[i]
            if price_delta < 0:
                info = "дороже"
            else:
                info = "дешевле"
            info_list.append(
                f"\"{name_of_data[i]}\" изменил цену c "
                f"{old_valutes_of_data[i]} руб. на {valutes_of_data[i]} руб. "
                f"Стало {info} на: {abs(price_delta):.3f} руб."
            )
        else:
            info_list.append(f"Изменений цены для \"{name_of_data[i]}\" нет.")
else:
    for i in range(5):
        info_list.append(
            f"Недостаточно информации для анализа \"{name_of_data[i]}\"."
            )
    print("Для анализа курсов валют информации недостаточно...")

now = datetime.strftime(datetime.now(), "%H:%M:%S %d.%m.%Y")

with open("statistics.txt", "a", encoding="utf-8") as file:
    file.write(
        f"============= Дата: {now}. =============\n"
        f"{valutes_of_data[0]} руб. - доллар США.\n"
        f"{valutes_of_data[1]} руб. - евро.\n"
        f"{valutes_of_data[2]} руб. - фунт стерлингов.\n"
        f"{valutes_of_data[3]} руб. - дирхам ОАЭ.\n"
        f"{valutes_of_data[4]} руб. - юань.\n"
    )

    file.write("============== Информация об изменениях ==============\n")
    for info in info_list:
        file.write(
            f"{info}\n"
        )
    file.write(
            "============ Информация от Центробанка РФ ============\n\n\n"
        )


root = Tk()
frm = ttk.Frame(root, padding=40)
frm.grid()

# Вывод текста с курсами валют в центре окна приложения.
for i in range(5):
    ttk.Label(
        frm,
        text=f"{name_of_data[i]}: {valutes_of_data[i]} руб."
    ).grid(column=0, row=i)

ttk.Label(frm, text="Информация с сайта Центробанка РФ.").grid(column=0, row=6)
root.mainloop()
