from PIL import Image
import numpy as np

#------------------Zad 1------------------
def rysuj_ramki_szare(w, h, grub, kolor, kolor_ramki):
    wymiary = (h, w)
    tab_obraz = np.ones(wymiary, dtype=np.uint8)
    ile = int(w/grub)

    for i in range(ile):
        top = i * grub
        right = w - i * grub
        bottom = h - i * grub
        left = i * grub

        if i % 2 == 1:
            tab_obraz[top:bottom, left:right] = kolor
        else:
            tab_obraz[top:bottom, left:right] = kolor_ramki

    return Image.fromarray(tab_obraz)

#rysuj_ramki_szare(200, 200, 8, 100, 67).show()


def rysuj_pasy_pionowe_szare(w,h,grub, kolor):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    ile = int(w / grub)
    for x in range(ile):
        for y in range(grub):
            j = x * grub + y
            for i in range(h):
                tab[i, j] = (y + kolor) % 256
    return Image.fromarray(tab)

#rysuj_pasy_pionowe_szare(200, 150, 10, 60).show()


#------------------Zad 2------------------
# a)
gwiazdka_bmp = Image.open("gwiazdka.bmp")
print("Gwiazdka mode: ",gwiazdka_bmp.mode)


def negatyw(obraz):
    if obraz.mode == "L":
        tab = np.asarray(obraz)
        h, w = tab.shape
        tab_neg = tab.copy()
        for i in range(h):
            for j in range(w):
                tab_neg[i, j] = 255 - tab[i, j]
        return Image.fromarray(tab_neg)

    elif obraz.mode == "1":
        tab = np.asarray(obraz)
        h, w = tab.shape
        tab_neg = tab.copy()
        for i in range(h):
            for j in range(w):
                tab_neg[i, j] = ~tab[i, j]
        return Image.fromarray(tab_neg)

    elif obraz.mode == "RGB":
        tab = np.asarray(obraz)
        h, w = tab.shape
        tab_neg = tab.copy()
        for i in range(h):
            for j in range(w):
                tab_neg[i, j] = tab_neg[255 - i, 255 - j]
        return Image.fromarray(tab_neg)
    return None


# negatyw(gwiazdka_bmp).show()



# b)
def rysuj_ramki_kolorowe(w, kolor, zmiana_koloru_r, zmiana_koloru_g, zmiana_koloru_b):
    t = (w, w, 3)
    tab = np.zeros(t, dtype=np.uint8)
    kolor_r = kolor[0]
    kolor_g = kolor[1]
    kolor_b = kolor[2]
    z = w
    for k in range(int(w / 2)):
        for i in range(k, z - k):
            for j in range(k, z - k):
                tab[i, j] = [kolor_r, kolor_g, kolor_b]
        kolor_r = (kolor_r - zmiana_koloru_r) % 256
        kolor_g = (kolor_g - zmiana_koloru_g) % 256
        kolor_b = (kolor_b - zmiana_koloru_b) % 256
    return Image.fromarray(tab)


obraz2B = rysuj_ramki_kolorowe(200, [20, 120, 220], 6, 9, -6)
#obraz2B.show()


# c)
def rysuj_po_skosie_szare(h,w, a, b):
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            tab[i, j] = (a*i + b*j) % 256
    return Image.fromarray(tab)


obraz2C = rysuj_po_skosie_szare(100, 300, 6, 9)
#obraz2C.show()

#------------------Zad 3------------------
def koloruj_w_paski(obraz, grub, kolor, kolor_paski):
    if obraz.mode == "1":
        t = np.asarray(obraz)
        h, w = t.shape
        tab = np.ones((h, w, 3), dtype=np.uint8) * 255

        for i in range(h):
            k = i // grub
            r = (kolor[0] + k * kolor_paski) % 256
            g = (kolor[1] + k * kolor_paski) % 256
            b = (kolor[2] + k * kolor_paski) % 256
            for j in range(w):
                if t[i, j] == 0:
                    tab[i, j] = [r, g, b]
        return Image.fromarray(tab)
    return None

# a)
inicjaly = Image.open("inicjaly.bmp")
print("Inicjaly mode: ", inicjaly.mode)
kolorowe_paski = koloruj_w_paski(inicjaly, 2,  (50, 100, 150), 150)
kolorowe_paski.show()

# b)
#kolorowe_paski.save("kolorowe_paski_png.png")
#kolorowe_paski.save("kolorowe_paski_jpg.jpg")

# Obrazy się różnią, obraz .jpg ma rozmazane kolory i ostrość, za to .png wygląda idealnie.
# Format JPG używa kompresji stratnej czyli kiedy zapisujemy obraz to algorytm usuwa część informacji o kolorach
# oraz ostrości, aby zmniejszyć rozmiar pliku co właśnie powoduje że wygląda on mniej czysto i ma plamy.

#------------------Zad 4------------------
# Zakres wartości uint8 to 0 - 255 (uint8 zawija się w modulo 256),
# dlatego używamy tego w kodzie aby zapobiec zawijaniu się automatycznie co może prowadzić do błędów kolorystycznych:

# a)
# 328 % 256 = 72 (uint8)

# b)
# -24 % 256 = 232 (uint8)
