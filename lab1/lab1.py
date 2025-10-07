from PIL import Image
import numpy as np

inicjaly = Image.open("inicjaly.bmp")               # ustawia inicjaly jako obraz "inicjaly.bmp"

# Zad 2
print("-----------------Zad 2-----------------")
print("tryb:", inicjaly.mode)
print("format:", inicjaly.format)
print("rozmiar:", inicjaly.size)
#obraz.show()               # pokazuje obraz


# Zad 3
print("-----------------Zad 3-----------------")
dane_obrazka = np.asarray(inicjaly)
#np.savetxt("inicjaly.txt", dane_obrazka, fmt="%2d")                 # zapis obrazka jako tablica zerojedynkowa
print("Zapisano obraz jako tablica zerojedynkowa (inicjaly.txt)")

# Zad 4
print("-----------------Zad 4-----------------")
pixel1 = inicjaly.getpixel((50,30))
pixel2 = inicjaly.getpixel((90,40))
pixel3 = inicjaly.getpixel((99,0))
pixel4 = inicjaly.getpixel((35,26))

print("Pixel 1: ", pixel1)
print("Pixel 2: ", pixel2)
print("Pixel 3: ", pixel3)
print("Pixel 4 (czarny): ", pixel4)

# Zad 5
print("-----------------Zad 5-----------------")
tablica_bool = np.loadtxt("inicjaly.txt", dtype=np.bool_)
print("typ danych tablicy t1: ", tablica_bool.dtype)  # typ danych przechowywanych w tablicy
print("rozmiar tablicy t1: ", tablica_bool.shape)  # rozmiar tablicy - warto porównac z rozmiarami obrazka
print("wymiar tablicy t1: ", tablica_bool.ndim)  # wymiar mówi czy to jest talica 1D, 2d, 3D ...

# Zad 6
print("-----------------Zad 6-----------------")
tablica_uint8 = np.loadtxt("inicjaly.txt", dtype=np.uint8)
print("typ danych tablicy t1: ", tablica_uint8.dtype)
print("rozmiar tablicy t1: ", tablica_uint8.shape)
print("wymiar tablicy t1: ", tablica_uint8.ndim)
