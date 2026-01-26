from tkinter import Tk, ttk
from datetime import datetime
from url_request import usd_data


now = datetime.strftime(datetime.now(), "%H:%M:%S %d.%m.%Y")

with open("statistics.txt", "a", encoding="utf-8") as file:
    file.write(f"Доллар США: {usd_data} руб. Дата: {now}.\n")

root = Tk()
frm = ttk.Frame(root, padding=25)
frm.grid()
ttk.Label(frm, text=f"Доллар США: {usd_data} руб.").grid(column=0, row=0)
ttk.Label(frm, text="Информация с сайта Центробанка РФ.").grid(column=0, row=1)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=5, row=5)
root.mainloop()
