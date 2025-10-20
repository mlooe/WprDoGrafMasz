from PIL import Image
import numpy as np

#------------------Zad 1------------------
def rysuj_ramki(w, h, grub, kolor):
    wymiary = (h, w)
    tab_obraz = np.ones(wymiary, dtype=np.uint8)
    ile = int(w/grub)

    for i in range(ile):
        top = i * grub
        right = w - i * grub
        bottom = h - i * grub
        left = i * grub

        if i % 2 == 1:
            tab_obraz[top:bottom, left:right] = 1
        else:
            tab_obraz[top:bottom, left:right] = 0

    tab_obraz = tab_obraz * kolor
    return Image.fromarray(tab_obraz)

# rysuj_ramki(200, 200, 5, 60).show()


def rysuj_pasy_pionowe(w,h,grub, kolor):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    ile = int(w / grub)
    for k in range(ile):
        for g in range(grub):
            j = k * grub + g
            for i in range(h):
                tab[i, j] = (g + kolor) % 256
    return Image.fromarray(tab)

# rysuj_pasy_pionowe(200, 150, 10, 60).show()


#------------------Zad 2------------------
# a)
gwiazdka = Image.open("gwiazdka.bmp")
print(gwiazdka.mode)

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


# negatyw(gwiazdka).show()



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
# obraz2B.show()

# c)
def rysuj_po_skosie_szare(h,w, a, b):
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            tab[i, j] = (a*i + b*j) % 256
    return Image.fromarray(tab)


obraz2C = rysuj_po_skosie_szare(100, 300, 6, 9)
# obraz2C.show()










