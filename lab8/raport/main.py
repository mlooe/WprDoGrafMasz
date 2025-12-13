from PIL import Image
import numpy as np
from PIL import ImageChops, ImageOps
from PIL import ImageStat as stat
import matplotlib.pyplot as plt


#---------------------Zad 1---------------------
print("---------------------Zad 1---------------------")
im = Image.open('skan_xray.jpg')
tab_im = np.array(im)
r, g , b = im.split()

szary = r
print("Tryb obrazu: ", im.mode)

im_L = im.convert('L')
print("Tryb obrazu (po przekonwertowaniu): ", im_L.mode)


#---------------------Zad 2---------------------
print("---------------------Zad 2---------------------")
def statystyki(im):
    s = stat.Stat(im)
    print("extrema ", s.extrema)
    print("count ", s.count)
    print("mean ", s.mean)
    print("median ", s.median)
    print("stddev ", s.stddev)

print("Statystki obrazu: im")
statystyki(im)

print("\nStatystki obrazu: im_L")
statystyki(im_L)

hist = im_L.histogram()
plt.title("Histogram 1")
plt.bar(range(256), hist[:], color='b', alpha=0.8)
#plt.savefig('histogram1.png')


#---------------------Zad 3---------------------

def histogram_norm(obraz):
    hist = obraz.histogram()
    w, h = obraz.size
    total_pixels = w * h
    hist_norm = [x / total_pixels for x in hist]
    return hist_norm

hist2 = histogram_norm(im_L)

plt.figure(figsize=(10, 4))
plt.title("Histogram 2 (znormalizowany)")
plt.bar(range(256), hist2[:], color='b', alpha=0.8)
#plt.savefig("histogram2.png")

#---------------------Zad 4---------------------
def histogram_cumul(obraz):
    norm = histogram_norm(obraz)
    hist_kumul = []
    suma = 0.0
    for val in norm:
        suma += val
        hist_kumul.append(suma)
    return hist_kumul

hist3 = histogram_cumul(im_L)

plt.figure(figsize=(10, 4))
plt.title("Histogram 3 (skumulowany)")
plt.bar(range(256), hist3[:], color='b', alpha=0.8)
plt.savefig("histogram3.png")

#---------------------Zad 5---------------------
def histogram_equalization(obraz):
    hist_cumul = histogram_cumul(obraz)
    tab = [int(255 * x) for x in hist_cumul]
    return obraz.point(tab)

equalized = histogram_equalization(im_L)
#equalized.save("equalized.png")

#---------------------Zad 6---------------------
equalized1 = ImageOps.equalize(im_L)
#equalized1.save("equalized1.png")

#---------------------Zad 6.2---------------------
h_eq = equalized.histogram()
h_eq1 = equalized1.histogram()

plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.title("Histogram 'equalized.png'")
plt.bar(range(256), h_eq[:], color='r', alpha=0.8)

plt.subplot(2, 1, 2)
plt.title("Histogram 'equalized1.png'")
plt.bar(range(256), h_eq1[:], color='b', alpha=0.8)

#plt.savefig("histogram4.png")

#---------------------Zad 6.3---------------------
print("---------------------Zad 6.3---------------------")
print("\nObraz 'equalized.png'")
statystyki(equalized)

print("\nObraz 'equalized1.png'")
statystyki(equalized1)