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

ramki_szare = rysuj_ramki_szare(200, 200, 8, 100, 67)
#ramki_szare.save("ramki_szare.png")


def rysuj_pasy_pionowe_szare(w,h,grub, kolor):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    ile = int(w / grub)+1
    for k in range(ile):
        for g in range(grub):
            j = k * grub + g
            if j < w:
                for i in range(h):
                    tab[i, j] = (k + kolor) % 256
    return Image.fromarray(tab)

pasy_pionowe_szare = rysuj_pasy_pionowe_szare(200, 150, 10, 30)
#pasy_pionowe_szare.save("pasy_pionowe_szare.png")


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
        h, w, _ = tab.shape
        tab_neg = tab.copy()
        for i in range(h):
            for j in range(w):
                tab_neg[i, j] = 255 - tab_neg[i, j]
        return Image.fromarray(tab_neg)
    return None


gwiazdka_negatyw = negatyw(gwiazdka_bmp)
#gwiazdka_negatyw.save("gwiazdka_negatyw.png")


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


ramki_kolorowe = rysuj_ramki_kolorowe(200, [20, 120, 220], 6, 9, -6)
#ramki_kolorowe.show()

ramki_kolorowe_negatyw = negatyw(ramki_kolorowe)
#ramki_kolorowe_negatyw.show()
#ramki_kolorowe_negatyw.save("ramki_kolorowe_negatyw.png")


# c)
def rysuj_po_skosie_szare(h,w, a, b):
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            tab[i, j] = (a*i + b*j) % 256
    return Image.fromarray(tab)


po_skosie_szare = rysuj_po_skosie_szare(100, 300, 6, 9)
#po_skosie_szare.show()
#po_skosie_szare.save("po_skosie_szare.png")


po_skosie_szare_negatyw = negatyw(po_skosie_szare)
#po_skosie_szare_negatyw.show()
#po_skosie_szare_negatyw.save("po_skosie_szare_negatyw.png")
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
#kolorowe_paski.show()

# b)
#kolorowe_paski.save("kolorowe_paski_png.png")
#kolorowe_paski.save("kolorowe_paski_jpg.jpg")

# Obrazy się różnią, obraz .jpg ma rozmazane kolory i ostrość, za to .png wygląda idealnie.
# Format JPG używa kompresji stratnej czyli kiedy zapisujemy obraz to algorytm usuwa część informacji o kolorach
# oraz ostrości, aby zmniejszyć rozmiar pliku co właśnie powoduje że wygląda on mniej czysto i ma plamy.

#------------------Zad 4------------------
# Zakres wartości uint8 to 0 - 255, jeśli nie damy zawijania (% 256) to numpy pokaże błąd
# o tym, że liczba 328 jest poza limitem uint8


# a)
# 328 % 256 = 72 (uint8)

# b)
# -24 % 256 = 232 (uint8)



#------------------Zad 5------------------
r = np.asarray(rysuj_pasy_pionowe_szare(300, 200, 10 ,20))
g = np.asarray(rysuj_pasy_pionowe_szare(300, 200, 18 ,10))
b = np.asarray(rysuj_pasy_pionowe_szare(300, 200, 26 ,60))

rgb = np.stack((r,g,b), axis=2)
obraz6 = Image.fromarray(rgb)
#obraz6.show()
#obraz6.save("obraz6.png")

#------------------Zad 6------------------
def rysuj_po_skosie_szare(h,w, a, b):  # formuła zmiany wartości elemntów tablicy a*i + b*j
    t = (h, w) # rysuje kwadratowy obraz
    tab = np.zeros(t, dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            tab[i, j] = (a*i + b*j) % 256
    return tab


alfa = rysuj_po_skosie_szare(200, 300, 6, 9)
obraz_rgb = Image.open("obraz6.png")
alfa_ext = np.expand_dims(alfa, axis=-1)
combined = np.concatenate((obraz_rgb, alfa_ext), axis=-1)

obraz7 = Image.fromarray(combined)
obraz7.show()
#obraz7.save("obraz7.png")

#------------------Zad 7------------------
def rgb_to_cmyk(rgb_array):
    # Przekształć wartości RGB na zakres [0, 1]
    rgb = rgb_array.astype(float) / 255
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]

    # Oblicz kanał Kk (black)
    k = 1 - np.max(rgb, axis=2)

    # Uniknij dzielenia przez zero
    c = (1 - r - k) / (1 - k + 1e-8)
    m = (1 - g - k) / (1 - k + 1e-8)
    y = (1 - b - k) / (1 - k + 1e-8)

    # Zastąp NaN (dla czystej czerni) zerami
    c[np.isnan(c)] = 0
    m[np.isnan(m)] = 0
    y[np.isnan(y)] = 0

    # Przekształć na zakres [0, 255]
    cmyk = np.stack((c, m, y, k), axis=2) * 255
    return cmyk.astype(np.uint8)


# Konwersja do CMYK
t_cmyk = rgb_to_cmyk(np.asarray(obraz6))

image_cmyk = Image.fromarray(t_cmyk, mode="CMYK")
#image_cmyk.save("obraz8.tiff")

# a)
r_png = Image.fromarray(r)
#r_png.save("r.png")

c_png = Image.fromarray(t_cmyk[:, :, 0])
#c_png.save("c.png")







