import datetime # Modul untuk pengolahan tanggal dan waktu
import os       # Pada program ini, modul ini digunakan untuk menggunakan fungsi 'cls'
import locale   # Pada program ini, modul ini digunakan untuk mengkonversi angka menjadi format mata uang
import msvcrt   # Modul ini digunakan untuk menggunakan fungsi getch()

# Untuk menampilkan tanggal dan waktu
present = datetime.datetime.now()
date_time = present.strftime("%d-%m-%Y %H:%M")

# Untuk mengatur modul locale supaya menggunakan default wilayah Indonesia
locale.setlocale(locale.LC_ALL, 'id_ID')

class Customer:
    def __init__(self, name):
        self.name = name
        
    def display(self):
        print(f" {self.name} ".center(40, "="))
        
class Menu():
    def __init__(self):
        self.menu_items = {"Americano" : 15000,
                           "Espresso" : 15000,
                           "Caffe late" : 17000,
                           "Vanilla late" : 20000,
                           "Koppi Aceh" : 17000,
                           "Es teh" : 7000,
                           "Green tea late" : 18000,
                           "Caramel Late" : 20000}
        
    def display(self):
        print("="*17 + " Menu " + "="*17)
        for product, price in self.menu_items.items():
            price = locale.format_string("%d", price, grouping=True)
            print(product.ljust(20) + price.rjust(20))
            
def Menu_Order():
    global total
    for order, qty in order_list.items():
        item_price = menu.menu_items[order]
        item_price = locale.format_string("%d", item_price, grouping=True)
        price = menu.menu_items[order] * qty
        price = locale.format_string("%d", price, grouping=True)
        print("\n" + order)
        print(f"{qty} x {item_price}".ljust(20) + str(price).rjust(20))

    total = locale.format_string("%d", total, grouping=True)
    print("\n" + "="*40)
    print("Total".ljust(20) + str(total).rjust(20))

def Payment_Details():
    Clear()
    print("="*40)
    print("Detail Pembayaran".center(40))
    print("="*40)
    
    Menu_Order()
    
def Receipt():
    global money
    global changes
    global name
    
    Clear()
    print("Receipt".center(40))
    print("="*40)
    
    Menu_Order()
    
    money = locale.format_string("%d", money, grouping=True)
    changes = locale.format_string("%d", changes, grouping=True)
    print("="*40)
    print("Cash".ljust(20) + f"{money}".rjust(20))
    print("Changes".ljust(20) + f"{changes}".rjust(20))
    
    Cst.display()
    print(f" {date_time} ".center(40, "="))
    msvcrt.getch()
    

def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
# Program Utama    
total = 0
menu = Menu()
order_list = {}

while True:    
    Clear()
    
    menu.display()
    print("\nKetik '0' untuk menyelesaikan pesanan!")
    order = str (input("Menu yang anda pilih : "))

    if order == "0":
        break
    elif order in menu.menu_items:
        qty = int (input("Jumlah pesanan\t     : "))
        if qty < 1:
            Clear()
            menu.display()
            print (end="\n" + "Inputan tidak valid!".center(40))
            msvcrt.getch()
        else:
            price = menu.menu_items[order] * qty
            order_list[order] = qty
            total += price
            
    elif order not in menu.menu_items:
        Clear()
        menu.display()
        print(end="\n" + "Mohon maaf, menu tidak tersedia".center(40))
        print(end="\n" + "Silahkan pilih menu kembali".center(40))
        msvcrt.getch()

name = str(input("Pesanan atas nama : "))
Cst = Customer(name)
# Menampilkan detail pembayaran
Payment_Details()

# Memasukkan uang untuk membayar
total = locale.atof(total)
total = int(total)
money = int(input("\nNominal uang untuk membayar : "))

while money < total:
    Payment_Details()
    total = locale.atof(total)
    total = int(total)
    print("\n" + "Nominal uang tidak mencukupi!".center(40))
    print("Silahkan input kembali!".center(40))
    money = int(input("\nNominal uang untuk membayar : "))
    
changes = money - total   

Receipt()