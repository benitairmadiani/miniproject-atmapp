import random, datetime
from customer import Customer
from atm_card import ATMCard

customer1 = Customer(1234, 1234, 10000)

while True:
    id = int(input("Masukkan pin anda: "))
    trial = 0

    while (id != int(atm.checkPin()) and trial < 3):
        id = int(input("Pin anda salah. Silahkan masukkan lagi: "))
        trial +=1
        if trial == 3:
            print("Error. Silahkan ambil kartu dan coba lagi")

    while True:
        print("Selamat datang")
        print("0: Cek saldo, 1: Debet, 2: Simpan, 3: Ganti pin, 4: Keluar")
        selected_menu = int(input("Pilih menu di atas dalam (0-4): "))
        
        if selected_menu == 0:
            customer.checkBalance()
        
        elif selected_menu == 1:
            nominal = int(input("Masukkan nominal uang yang akan ditarik: "))
            if nominal < custBalance:
                customer.withdrawBalance()
            else:
                nominal = int(input("Saldo anda tidak mencukupi. Masukkan nominal uang yang akan ditarik: "))
        
        elif selected_menu == 2:
            nominal = int(input("Masukkan nominal uang yang anda tambahkan: "))
            customer.depositBalance()
        
        else:
            menu = int(input("Pilih menu di atas dalam (0-4): "))
     
