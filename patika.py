print("1. Soru")
"""
Bir listeyi düzleştiren (flatten) fonksiyon yazın. 
Elemanları birden çok katmanlı listtlerden ([[3],2] gibi) oluşabileceği gibi,
 non-scalar verilerden de oluşabilir. 
 
 Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]

"""

liste= [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

print(f"Girdi : {liste}")

def flatten_fonk(x):
	yeni_liste = []
	for i in x:
		if type(i) == list:
			for j in i:
				if type(j) == list:
					for k in j:
						if type(k) == list:
							for l in k:
								yeni_liste.append(l)
						else:
							yeni_liste.append(k)
				else:
					yeni_liste.append(j)
		else:
			yeni_liste.append(i)
	return yeni_liste

print(f"Çıktı : {flatten_fonk(liste)}")

print("*"*50)

print("2. Soru")
""" 
    Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. 
    Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. 
    
    Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[[7, 6, 5], [4, 3], [2, 1]]
"""

liste_2= [[1, 2], [3, 4], [5, 6, 7]]

print(f"Girdi: {liste_2}")


def ters_cevir(y):
	for i in y[::-1]:
		i.reverse()

	return y[::-1]

print(ters_cevir(liste_2))