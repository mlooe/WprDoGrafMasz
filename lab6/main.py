from PIL import Image
import numpy as np
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt
import random

def rysuj_histogram_L(obraz):
    hist = obraz.histogram()
    plt.title("histogram  ")
    plt.bar(range(256), hist[:])
    plt.show()

def statystyki(im):
    s = stat.Stat(im)
    print("extrema ", s.extrema)  # max i min
    print("count ", s.count)  # zlicza
    print("mean ", s.mean)  # srednia
    print("rms ", s.rms)  # pierwiastek średniokwadratowy
    print("median ", s.median)  # mediana
    print("stddev ", s.stddev)  # odchylenie standardowe



#---------------------Zad 1---------------------
# a)

print("---------------------Zad 1---------------------")
print("a)")


def rysuj_histogram_RGB(obraz):
    hist = obraz.histogram()
    plt.figure(figsize=(16, 16))

    plt.subplot(2, 2, 1)
    plt.title("kanał R")
    plt.bar(range(256), hist[:256], color='r', alpha=0.5)

    plt.subplot(2, 2, 2)
    plt.title("kanał G")
    plt.bar(range(256), hist[256:2 * 256], color='g', alpha=0.5)

    plt.subplot(2, 2, 3)
    plt.title("kanał B")
    plt.bar(range(256), hist[2 * 256:], color='b', alpha=0.5)

    plt.subplot(2, 2, 4)
    plt.title("Histogram")
    plt.bar(range(256), hist[:256], color='r', alpha=0.5)
    plt.bar(range(256), hist[256:2 * 256], color='g', alpha=0.4)
    plt.bar(range(256), hist[2 * 256:], color='b', alpha=0.3)
    plt.subplots_adjust(wspace=0.05, hspace=0.05)
    #plt.savefig("zad1a")


im = Image.open("robert_lewandowski.png")
#rysuj_histogram_RGB(im)

print("rozmiar", im.size)
print("tryb", im.mode)
print("format", im.format)
statystyki(im)


# b)
print("b)")
zad1b = im.histogram()
print("Kanał R: ", zad1b[155])
print("Kanał G: ", zad1b[155 + 256])
print("Kanał B: ", zad1b[155 + 2 * 256])

# c)
print("c)")

def zlicz_piksele(obraz, kolor):
    piksele = obraz.load()
    szer, wys = obraz.size
    licznik = 0

    for y in range(wys):
        for x in range(szer):
            if list(piksele[x, y]) == kolor:
                licznik += 1
    return licznik

zad1c = zlicz_piksele(im, [155,155,155])
print("Liczba pikseli o wartości [155,155,155]: ", zad1c)

#---------------------Zad 2---------------------
# a)
print("---------------------Zad 2---------------------")
print("a)")
im_jpg = Image.open("robert_lewandowski.jpg")

print("Statystyki obrazu im: \n")
statystyki(im)
print("\nStatystyki obrazu im_jpg: \n")
statystyki(im_jpg)

# b)
print("\nb)")
roznica = ImageChops.difference(im, im_jpg)
statystyki(roznica)

# c)
print("\nc)")
im_jpg3 = Image.open("robert_lewandowski3.jpg")
print("Statystyki obrazu im: \n")
statystyki(im)
print("\nStatystyki obrazu im_jpg3: \n")
statystyki(im_jpg3)


#---------------------Zad 3---------------------
# a)
print("---------------------Zad 3---------------------")
print("a)")

arr = np.asarray(im)
t_r = arr[:, :, 0]
t_g = arr[:, :, 1]
t_b = arr[:, :, 2]

im_r = Image.fromarray(t_r)
im_g = Image.fromarray(t_g)
im_b = Image.fromarray(t_b)

# b)
print("b)")
im1 = Image.merge("RGB", (im_r, im_g, im_b))
diff = ImageChops.difference(im, im1)

# c)
print("c)")
plt.figure(figsize=(16, 16))

plt.subplot(2, 2, 1)
plt.title("Obraz im")
plt.axis('off')
plt.imshow(im)

plt.subplot(2, 2, 2)
plt.title("Obraz im1")
plt.axis('off')
plt.imshow(im1)

plt.subplot(2, 2, 3)
plt.title("Różnica obrazów")
plt.axis('off')
plt.imshow(diff)
plt.subplots_adjust(wspace=0.05, hspace=0.05)

#plt.savefig('fig1.png')
# plt.show()

# d)
print("Statystyki diff:\n")
statystyki(diff)


print("---------------------Zad 4---------------------")
print("a)")
#---------------------Zad 4---------------------
def mieszaj_kanaly(obraz):
    r, g, b = obraz.split()

    nr = Image.fromarray(255 - np.array(r))
    ng = Image.fromarray(255 - np.array(g))
    nb = Image.fromarray(255 - np.array(b))

    kanal_lista = [r, g, b, nr, ng, nb]
    nowe_kanaly = [random.choice(kanal_lista) for _ in range(3)]
    return Image.merge("RGB", nowe_kanaly)

# a)
#mix = mieszaj_kanaly(im)
#mix.show()
#mix.save("mix.png")

print("b)")
# b)
def rozpoznaj_mix(obraz, mix):
    r, g, b = obraz.split()

    nr = Image.fromarray(255 - np.array(r))
    ng = Image.fromarray(255 - np.array(g))
    nb = Image.fromarray(255 - np.array(b))

    kanal_dict = {
        "r": np.array(r),
        "g": np.array(g),
        "b": np.array(b),
        "nr": np.array(nr),
        "ng": np.array(ng),
        "nb": np.array(nb)
    }

    mr, mg, mb = mix.split()
    mix_kanaly = [np.array(mr), np.array(mg), np.array(mb)]

    wynik = []
    for mk in mix_kanaly:
        znaleziono = False
        for nazwa, kanal in kanal_dict.items():
            if np.array_equal(mk, kanal):
                wynik.append(nazwa)
                znaleziono = True
                break
        if not znaleziono:
            wynik.append("nieznany")

    return wynik

mix = Image.open("mix.png")
print("Kanał w mix [R, G, B] pochodzi z kanału: ")
print(rozpoznaj_mix(im, mix))

print("---------------------Zad 5---------------------")
#---------------------Zad 5---------------------
im = Image.open('beksinski.png')
print("Tryb obrazu 'beksinki.png': ", im.mode)
im1 = Image.open('beksinski1.png')
print("Tryb obrazu 'beksinski1.png': ", im1.mode)

# r, g, b = im1.split()



print("---------------------Zad 6---------------------")
#---------------------Zad 6---------------------
def ocen_czy_identyczne(obraz1, obraz2):
    if obraz1.mode != obraz2.mode:
        return "obrazy nie są identyczne, bo mają różne tryby"

    if obraz1.size != obraz2.size:
        return "obrazy nie są identyczne, bo mają różne wymiary"

    arr1 = np.array(obraz1)
    arr2 = np.array(obraz2)

    if np.array_equal(arr1, arr2):
        return "obrazy identyczne"
    else:
        return "obrazy nie są identyczne, bo wartości pikseli są różne"

beksinski = Image.open("beksinski.png")
beksinski1 = Image.open("beksinski1.png")
beksinski2 = Image.open("beksinski2.png")
beksinski3 = Image.open("beksinski3.png")

print(ocen_czy_identyczne(beksinski, beksinski1))
print(ocen_czy_identyczne(beksinski, beksinski2))
print(ocen_czy_identyczne(beksinski, beksinski3))


print("---------------------Zad 7---------------------")
#---------------------Zad 7---------------------
# a)
def pokaz_roznice(obraz_wejsciowy):
    arr = np.asarray(obraz_wejsciowy)
    if len(arr.shape) == 3:
        wynik = np.zeros_like(arr)

        for kanal in range(arr.shape[2]):
            max_val = arr[:, :, kanal].max()
            if max_val > 0:
                wynik[:, :, kanal] = (arr[:, :, kanal] / max_val) * 255
            else:
                wynik[:, :, kanal] = arr[:, :, kanal]

        wynik = wynik.astype(np.uint8)
        return Image.fromarray(wynik)

    else:
        max_val = arr.max()
        if max_val > 0:
            arr = (arr / max_val) * 255

        arr = arr.astype(np.uint8)
        return Image.fromarray(arr)

im_jpg3 = Image.open("im_jpg3.jpg")

# b)
im = Image.open("im.png")
diff = ImageChops.difference(im, im_jpg3)

pokaz_diff = pokaz_roznice(diff)

# c)
plt.figure(figsize=(16, 16))

plt.subplot(2, 2, 1)
plt.title("Obraz im")
plt.axis('off')
plt.imshow(im)

plt.subplot(2, 2, 2)
plt.title("Obraz im_jpg3")
plt.axis('off')
plt.imshow(im_jpg3)

plt.subplot(2, 2, 3)
plt.title("Obraz diff")
plt.axis('off')
plt.imshow(diff)

plt.subplot(2, 2, 4)
plt.title("pokaz_roznice(diff)")
plt.axis('off')
plt.imshow(pokaz_diff)

plt.subplots_adjust(wspace=0.05, hspace=0.05)
#plt.savefig('fig2.png')

print("---------------------Zad 8---------------------")
#---------------------Zad 8---------------------
def wstaw_inicjaly(obraz_bazowy, obraz_wstawiany, m, n, kolor):
    tab = np.asarray(obraz_bazowy, dtype=np.uint8)
    tab_start = np.copy(tab)
    tab_end = np.asarray(obraz_wstawiany)

    h_ins, w_ins = tab_end.shape
    h_baz, w_baz, dim = tab_start.shape

    m_start = max(0, m)
    n_start = max(0, n)

    m_end = min(w_baz, m + w_ins)
    n_end = min(h_baz, n + h_ins)

    for wysokosc in range(n_start, n_end):
        for szerokosc in range(m_start, m_end):
            if tab_end[wysokosc - n, szerokosc - m] == 0:
                tab_start[wysokosc, szerokosc] = kolor

    return Image.fromarray(tab_start)


inicjaly = Image.open("inicjaly.bmp")
wstawione_inicjaly = wstaw_inicjaly(im, inicjaly, 270, 0, [0, 255, 255])
wstawione_inicjaly = wstaw_inicjaly(wstawione_inicjaly, inicjaly, 0, 355, [255, 255, 0])
wstawione_inicjaly = wstaw_inicjaly(wstawione_inicjaly, inicjaly, 300, 200, [0, 255, 0])

#wstawione_inicjaly.save("obraz_inicjaly.png")

print("---------------------Zad 9---------------------")
#---------------------Zad 9---------------------
# a)
def odkoduj(obraz1, obraz2):
    arr1 = np.asarray(obraz1)
    arr2 = np.asarray(obraz2)

    difference = np.any(arr1 != arr2, axis=2)
    diff_image_array = difference.astype(np.uint8) * 255

    diff_image = Image.fromarray(diff_image_array)

    return diff_image

# b)
obraz_zakodowany = Image.open("zakodowany1.bmp")
jesien = Image.open("jesien.jpg")

obraz_odkodowany = odkoduj(obraz_zakodowany, jesien)
#obraz_odkodowany.save("kod2.bmp")