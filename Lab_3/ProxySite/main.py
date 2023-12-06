import tkinter as tk
from site import Site
from site_proxy import SiteProxy

def get_page():
    url = entry.get()
    result = my_site.get_page(url)
    label_result.config(text=result)

root = tk.Tk()
root.title("Web Page Proxy")
root.geometry("500x150")

label = tk.Label(root, text="Введіть URL сторінки:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Отримати сторінку", command=get_page)
button.pack()

label_result = tk.Label(root, text="")
label_result.pack()

my_site = SiteProxy(Site())

root.mainloop()