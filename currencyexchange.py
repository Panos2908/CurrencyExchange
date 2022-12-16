from tkinter import *
import requests,json

win = Tk()
var1 = StringVar()
var1.set("currency")
options1 = ["USD","EUR","JPY","TRY"]
var2 =StringVar()
var2.set("currenncy")
options2 = ["USD","EUR","JPY","TRY"]


def clear_all():
    amount_entry .delete(0,END)
    var1.set("currency")
    var2.set("currency")


def exchange():
    base_url = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
    from_currency = var1.get()
    to_currency = var2.get()
    api_key = "K3MQO5ISZGAYC6NI"
    main_url = base_url + "&from_currency=" + from_currency + "&to_currency=" + to_currency + "&apikey=" + api_key
    print(main_url)
    req_ob = requests.get(main_url)
    result = req_ob.json()
    rate = float(result["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
    print(rate)

    amount = amount_entry.get()
    final = round(float(rate) *float(amount),2)
    convert_entry.insert(0,final)


lbl1 = Label(win,text="welcome to Real Time Currency Convertor")
lbl1.grid(column=2,row=1)

amountlbl = Label(win,text="Amount:")
amountlbl.grid(column=1,row=2)

amount_entry = Entry(win)
amount_entry.grid(column=2,row=2)

fromcur_lbl = Label(win,text="From currency:")
fromcur_lbl.grid(column=1,row=3)

tocur_lbl = Label(win,text="To currency:")
tocur_lbl.grid(column=1,row=4)

a = OptionMenu(win,var1,*options1)
a.grid(row=4,column=2)

b = OptionMenu(win,var2,*options2)
b.grid(column=2,row=3)

convert_entry = Entry(win)
convert_entry.grid(column=2,row=5)

convert_btn = Button(win,text="Convert",command=exchange)
convert_btn.grid(column=2,row=6)

clear_btn = Button(win,text="Clear",command=clear_all)
clear_btn.grid(column=2,row=7)

convertedamount_lbl = Label(win,text="Converted Amount:")
convertedamount_lbl.grid(column=1,row=5)




win.mainloop()