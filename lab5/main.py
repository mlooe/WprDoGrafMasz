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

r, g, b = im1.split()



