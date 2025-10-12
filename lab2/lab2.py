from PIL import Image
import numpy as np

inicjaly = Image.open("inicjaly.bmp")
#inicjaly.show()

print("tryb", inicjaly.mode)
print("format", inicjaly.format)
print("rozmiar", inicjaly.size)

t_inicjaly = np.asarray(inicjaly)
print("typ danych tablicy", t_inicjaly.dtype)
print("rozmiar tablicy", t_inicjaly.shape)

# ---------------------Zad 1---------------------
def rysuj_paski_w_obrazie(obraz, grub):
    tab_obraz = np.asarray(obraz).astype(np.uint8)
    h, w = tab_obraz.shape
    for i in range(h):
        for j in range(grub):
            tab_obraz[i][j]=0
        for j in range(w-grub,w):
            tab_obraz[i][j]=0
    tab = tab_obraz.astype(bool)
    return Image.fromarray(tab)



def rysuj_ramke_w_obrazie(obraz, grub):
    obraz = rysuj_paski_w_obrazie(obraz, grub)
    tab_obraz = np.asarray(obraz).astype(np.uint8)
    h, w = tab_obraz.shape

    for i in range(grub):
        for j in range(w):
            tab_obraz[i][j]=0
    for i in range(h-grub, h):
        for j in range(w):
            tab_obraz[i][j]=0
    tab = tab_obraz.astype(bool)
    return Image.fromarray(tab)

# rysuj_ramke_w_obrazie(inicjaly, 6).show()


# ---------------------Zad 2---------------------
# Zad 2.1
def rysuj_ramki(w, h, grub):
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

    tab_obraz = tab_obraz * 255
    return Image.fromarray(tab_obraz)

# rysuj_ramki(200, 200, 5).show()

# Zad 2.2
def rysuj_pasy_pionowe(w,h,grub):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    ile = int(w / grub)
    for k in range(ile):
        for g in range(grub):
            j = k * grub + g
            for i in range(h):
                tab[i, j] = k % 2
    tab = tab * 255
    return Image.fromarray(tab)

# rysuj_pasy_pionowe(200, 150, 10).show()


# Zad 2.3
# Funkcja będzie rysować obraz szachownicy o rozmiarach "w x h", i grubości pól szachownicy "grub"

def rysuj_wlasne(w, h, grub):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    ile = int(w / grub)
    for i in range(h):
        rzad = i // grub
        for j in range(w):
            kolumna = j // grub
            if(rzad + kolumna) % 2 == 0:
                tab[i, j] = 1
            else:
                tab[i, j] = 0
    tab = tab * 255
    return Image.fromarray(tab)
# rysuj_wlasne(200, 200, 20).show()

# ---------------------Zad 3---------------------
obraz1 = Image.open("bs.bmp")
obraz2 = Image.open("inicjaly.bmp")

def wstaw_obraz_w_obraz(obraz_bazowy, obraz_wstawiany, m, n):
    tab_pocz = np.asarray(obraz_bazowy).astype(np.int_)
    tab_wstaw = np.asarray(obraz_wstawiany).astype(np.int_)

    h, w = tab_pocz.shape
    h0, w0 = tab_wstaw.shape

    n_pocz = max(0, n)
    m_pocz = max(0, m)
    n_kon = min(h, n + h0)
    m_kon = min(w, m + w0)

    for i in range(n_pocz, n_kon):
        for j in range(m_pocz, m_kon):
            tab_i = i - n
            tab_j = j - m
            tab_pocz[i][j] = tab_wstaw[tab_i][tab_j]
    tab = tab_pocz.astype(bool)
    return Image.fromarray(tab)

# wstaw_obraz_w_obraz(obraz1, obraz2, -30, 20).show()