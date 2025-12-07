from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from PIL import ImageChops

#---------------------Zad 1---------------------
obraz = Image.open("im.png")
inicjaly = Image.open("inicjaly.bmp")

#---------------------Zad 2---------------------
# a)
def wstaw_inicjaly(obraz, inicjaly, m, n, kolor):
    im = obraz.copy()
    w,h = inicjaly.size
    for i in range(w):
        for j in range(h):
            if inicjaly.getpixel((i,j)) < 128:
                im.putpixel((m + i, n + j), tuple(kolor))
    return im

obraz1 = wstaw_inicjaly(obraz, inicjaly, -80, -40, [255,0,0])
#obraz1.show()
#obraz1.save("obraz1.png")


# b)
def wstaw_inicjaly_maska(obraz, inicjaly, m, n):
    im = obraz.copy()
    w, h = inicjaly.size
    for i in range(w):
        for j in range(h):
            if inicjaly.getpixel((i, j)) < 128:
                r, g, b = im.getpixel((m + i, n + j))
                im.putpixel((m + i, n + j), (255 - r, 255 - g, 255 - b))
    return im

obraz2 = wstaw_inicjaly_maska(obraz,inicjaly, 140, 190)
#obraz2.show()
#obraz2.save("obraz2.png")


#---------------------Zad 3---------------------
def wstaw_inicjaly_load(obraz, inicjaly, m, n, kolor):
    im = obraz.copy()
    pix_o = im.load()
    pix_i = inicjaly.load()
    for i in range(inicjaly.width):
        for j in range(inicjaly.height):
            if pix_i[i, j] < 128:
                pix_o[m + i, n + j] = tuple(kolor)
    return im

obraz_inicjaly_load = wstaw_inicjaly_load(obraz, inicjaly, -80, -40, [255, 0, 0])
#obraz_inicjaly_load.show()

def wstaw_inicjaly_maska_load(obraz, inicjaly, m, n):
    im = obraz.copy()
    pix_o = im.load()
    pix_i = inicjaly.load()
    for i in range(inicjaly.width):
        for j in range(inicjaly.height):
            if pix_i[i, j] < 128:
                r, g, b = pix_o[m + i, n + j]
                pix_o[m + i, n + j] = (255 - r, 255 - g, 255 - b)
    return im

obraz_inicjaly_maska_load = wstaw_inicjaly_maska_load(obraz, inicjaly, 140, 190)
#obraz_inicjaly_maska_load.show()

plt.figure(figsize=(16, 16))

plt.subplot(2, 2, 1)
plt.title("wstaw_inicjaly")
plt.axis('off')
plt.imshow(obraz1)

plt.subplot(2, 2, 2)
plt.title("wstaw_inicjaly_maska")
plt.axis('off')
plt.imshow(obraz2)

plt.subplot(2, 2, 3)
plt.title("wstaw_inicjaly_load")
plt.axis('off')
plt.imshow(obraz_inicjaly_load)

plt.subplot(2, 2, 4)
plt.title("wstaw_inicjaly_maska_load")
plt.axis('off')
plt.imshow(obraz_inicjaly_maska_load)

plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('fig1.png')

#---------------------Zad 4---------------------
# a)
def kontrast(obraz, wsp_kontrastu):
    mn = ((255 + wsp_kontrastu) / 255) ** 2
    return obraz.point(lambda i: 128 + (i - 128) * mn)

obraz_kontrast_0 = kontrast(obraz, 0)
obraz_kontrast_100 = kontrast(obraz, 100)
obraz_kontrast_30 = kontrast(obraz, 30)
obraz_kontrast_60 = kontrast(obraz, 60)


plt.figure(figsize=(16, 16))

plt.subplot(2, 2, 1)
plt.title("wsp_kontrastu 0")
plt.axis('off')
plt.imshow(obraz_kontrast_0)

plt.subplot(2, 2, 2)
plt.title("wsp_kontrastu 30")
plt.axis('off')
plt.imshow(obraz_kontrast_30)

plt.subplot(2, 2, 3)
plt.title("wsp_kontrastu 60")
plt.axis('off')
plt.imshow(obraz_kontrast_60)

plt.subplot(2, 2, 4)
plt.title("wsp_kontrastu 100")
plt.axis('off')
plt.imshow(obraz_kontrast_100)

plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('fig2.png')

# b)
def transformacja_logarytmiczna(obraz):
    return obraz.point(lambda i: int(255 * np.log(1 + i / 255)))

def zakres(w, h):  # funkcja, która uprości podwójna petle for
    return [(i, j) for i in range(w) for j in range(h)]

def filtr_liniowy(image, a, b): # a, b liczby całkowite
    w, h = image.size
    pixele = image.load()
    for i, j in zakres(w, h):
        pixele[i, j] = (pixele[i, j][0]* a + b, pixele[i, j][1]* a + b, pixele[i, j][2]* a + b)

obraz_transformacja_logarytmiczna = transformacja_logarytmiczna(obraz)

temp_obraz = obraz.copy()
filtr_liniowy(temp_obraz, 2, 100)

plt.figure(figsize=(16, 16))

plt.subplot(2, 2, 1)
plt.title("oryginalny obraz")
plt.axis('off')
plt.imshow(obraz)

plt.subplot(2, 2, 2)
plt.title("po transformacji logarytmicznej")
plt.axis('off')
plt.imshow(obraz_transformacja_logarytmiczna)

plt.subplot(2, 2, 3)
plt.title("po funkcji liniowej a=2, b=100")
plt.axis('off')
plt.imshow(temp_obraz)

plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('fig3.png')


# c)
def transformacja_gamma(obraz, gamma):
    return obraz.point(lambda i: int((i / 255) ** (1 / gamma) * 255))

obraz_gamma_02 = transformacja_gamma(obraz, 0.2)
obraz_gamma_2 = transformacja_gamma(obraz, 2)
obraz_gamma_50 = transformacja_gamma(obraz, 50)

plt.figure(figsize=(16, 16))
plt.subplot(2, 2, 1)
plt.title("oryginalny obraz")
plt.axis('off')
plt.imshow(obraz)

plt.subplot(2, 2, 2)
plt.title("gamma 0.2")
plt.axis('off')
plt.imshow(obraz_gamma_02)

plt.subplot(2, 2, 3)
plt.title("gamma 2")
plt.axis('off')
plt.imshow(obraz_gamma_2)

plt.subplot(2, 2, 4)
plt.title("gamma 50")
plt.axis('off')
plt.imshow(obraz_gamma_50)

plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('fig4.png')

#---------------------Zad 5---------------------
def transformacja_gamma_lista(obraz, gamma):
    lista = [int((i / 255) ** (1 / gamma) * 255) for i in range(256)]
    lista = lista * 3
    return obraz.point(lista)

# a)
obraz_gamma_lista = transformacja_gamma_lista(obraz, 0.5)
obraz_gamma_05 = transformacja_gamma(obraz, 0.5)

plt.figure(figsize=(16, 16))

plt.subplot(2, 1, 1)
plt.title("transformacja gamma 0.5")
plt.axis('off')
plt.imshow(obraz_gamma_05)

plt.subplot(2, 1, 2)
plt.title("transformacja gamma lista 0.5")
plt.axis('off')
plt.imshow(obraz_gamma_lista)

plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('fig5.png')

#---------------------Zad 6---------------------
# a)
T = np.array(obraz, dtype='uint8')
T += 100
przyklad_1 = Image.fromarray(T)
przyklad_2 = obraz.point(lambda i: i + 100)

# b)
def zad6b(obraz):
    T = np.array(obraz, dtype='int32')
    T += 100
    T[T > 255] = 255
    T = T.astype('uint8')
    return Image.fromarray(T.astype(dtype='uint8'))

przyklad_3 = zad6b(obraz)

plt.figure(figsize=(16, 16))

plt.subplot(3, 1, 1)
plt.title("obraz T+=100")
plt.axis('off')
plt.imshow(przyklad_1)

plt.subplot(3, 1, 2)
plt.title("obraz lambda i + 100")
plt.axis('off')
plt.imshow(przyklad_2)

plt.subplot(3, 1, 3)
plt.title("funkcja zad6b")
plt.axis('off')
plt.imshow(przyklad_3)

plt.subplots_adjust(wspace=0, hspace=0.05)
plt.savefig('fig6.png')


