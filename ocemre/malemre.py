import os
import time
while True:
	print("""
===========================
Programa Hoşgeldin
===========================

[1] Toplama İşlemi
[2] Çıkartma İşlemi
[3] Çarpma İşlemi
[4] Bölme İşlemi
[Q] Programdan Çıkış

		""")

	veri = input("İşlem :")

	if veri == "1":
		print("== Toplama İşlemi ==")
		x = float(input("1. Sayıyı giriniz :"))
		y = float(input("2. Sayıyı giriniz :"))
		print("Sonuç :",x+y)
		c = input("Ana menüye dönmek için 'enter'")
		os.system("cls")  # os.system("") içerisindeki ler cmd de çalışacak kodlar linux da isen clear de  veya editörde kullanıcaksan bu komutu sil 

	elif veri == "2":
		print("== Çıkartma İşlemi ==")
		x = float(input("1. Sayıyı giriniz :"))
		y = float(input("2. Sayıyı giriniz :"))
		print("Sonuç :",x-y)
		c = input("Ana menüye dönmek için 'enter'")
		os.system("cls")

	elif veri == "3":
		print("== Çarpma İşlemi ==")
		x = float(input("1. Sayıyı giriniz :"))
		y = float(input("2. Sayıyı giriniz :"))
		print("Sonuç :",x*y)
		c = input("Ana menüye dönmek için 'enter'")
		os.system("cls")

	elif veri == "4":
		print("== Bölme İşlemi ==")
		x = float(input("1. Sayıyı giriniz :"))
		y = float(input("2. Sayıyı giriniz :"))
		print("Sonuç :",x/y)
		c = input("Ana menüye dönmek için 'enter'")
		os.system("cls")

	elif veri == "Q" or veri == "q":
		print("Programdan Çıkılıyor ...")
		time.sleep(2)  # 2 sani bekleyecek
		exit()  
		quit() 
		break   # döngüyü bitirdi

	else:
		print("Yanlış veri girdin aq salağı Tekrar dene")