def generiranje(broj, lista):
	'''Funkcija za generiranje proizvoljno duge liste neponavljajucih slucajnih brojeva.'''
	from random import shuffle, seed #Ucitavanje funkcija shuffle i seed iz modula random.
	seed() #Postavljanje generatora pseudo-slucajnih brojeva na slucajno :-)
	niz = [i for i in range(1, lista + 1)] #Generiranje pocetne liste brojeva.
	#print(niz) #provjera za debugiranje
	shuffle(niz) #Permutacija liste brojeva.
	#print(niz) #provjera za debugiranje
	del(niz[broj:]) #Brisanje viska permutirane liste.
	#print(niz) #provjera za debugiranje
	return niz #Izlazna vrijednost funkcije.

def main():
	'''Glavna funkcija programa za generiranje proizvoljno duge liste neponavljajucih slucajnih brojeva.'''
	broj = int(input('Upišite koliko brojeva želite generirati: '))
	lista = int(input('Upišite broj do kojega želite generiranje liste: '))
	print(generiranje(broj, lista)) #Poziv funkcije "generiranje" sa odgovarajucim vrijednostima.

if __name__ == '__main__':
	main()
	