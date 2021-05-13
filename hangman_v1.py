# -*- coding: utf-8 -*-
"""

"""

import random

#kelime_listesi=["cennet","operasyon","kalantor","cehennem","civciv","karakartal","cimbombom","sarıkanarya"]

kelime_listesi=open("kelime_listesi.txt",'r')

ss=[]

for s in kelime_listesi:
	ss.append(s.rstrip("\n"))

isim_gir = input("İsmini_Gir : ")

print(isim_gir + " \nAdamı Kurtarabilecek misin?")

r=random.randint(0, 14)

gizli_kelime=ss[r]

#alttaki satır sonucu test etmek için yazıldı
#print(gizli_kelime)






girilen_karakter = ""

kalan_hak = 10

while kalan_hak > 0:

	kalan_tahmin = 0

	for harf in gizli_kelime:

		if harf in girilen_karakter:

			print(harf)
		else:
			print("-")
			kalan_tahmin += 1

	if kalan_tahmin == 0:
		print("Adam Senindir !!!")	
		break


	tahmin = input("Adamını Yaşatmak için bir harf gir : ")
	girilen_karakter += tahmin

	if tahmin not in gizli_kelime:
		kalan_hak -= 1
		print("Dostum Dikkat Et - Cevabın Yanlış")
		print(f" {kalan_hak} hakkın kaldı")

		if kalan_hak == 0:  print("\nDostum Adamın Öldü !")
