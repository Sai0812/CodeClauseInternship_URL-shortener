import pyperclip
import pyshorteners
from tkinter import *

root = Tk()
root.geometry("400x200")
root.title("URL SHORTENER")
root.configure(bg="#49A")
url=StringVar()
url_address = StringVar()

def urlshortner():
    urladdress=url.get()
    url_short=pyshorteners.Shortener().tinyurl.short(urladdress)
    url_address.set(url_short)

def copyurl():
    url_short=url_address.get()
    pyperclip.copy(url_short)

Label(root,text="URL Shortener", font="poppins").pack(pady=10)
Entry(root, textvariable=url).pack(pady=10)
Button(root, text="Generate Short URL", command=urlshortner).pack(pady=10)
Entry(root,textvariable=url_address).pack(pady=10)
Button(root, text="Copy URL", command=copyurl).pack(pady=10)

root.mainloop()