from PIL import Image
import numpy as np
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt

#---------------------Zad 1---------------------
# a)
im = Image.open('bombardino.png')
print("rozmiar", im.size)
print("tryb", im.mode)
print("format", im.format)

def rysuj_histogram_RGB(obraz):
    hist = obraz.histogram()
    plt.title("histogram  ")
    plt.bar(range(256), hist[:256], color='r', alpha=0.5)
    plt.bar(range(256), hist[256:2 * 256], color='g', alpha=0.4)
    plt.bar(range(256), hist[2 * 256:], color='b', alpha=0.3)
    plt.show()

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


r, g, b = im.split()
print("tryb kanału r: ", r.mode)
print("tryb kanału g: ", g.mode)
print("tryb kanału b: ", b.mode)

plt.figure(figsize=(16, 16))
plt.subplot(2,2,1) # ile obrazów w pionie, ile w poziomie, numer obrazu
plt.imshow(im)
plt.axis('off')
plt.subplot(2,2,2)
plt.imshow(r, "gray")
plt.axis('off')
plt.subplot(2,2,3)
plt.imshow(g, "gray")
plt.axis('off')
plt.subplot(2,2,4)
plt.imshow(b, "gray")
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.show()

rysuj_histogram_L(r)
rysuj_histogram_L(g)
rysuj_histogram_L(b)

# b)
zad2b = im.histogram()
print("Kanał R: ", zad2b[155])
print("Kanał G: ", zad2b[155 + 256])
print("Kanał B: ", zad2b[155 + 2 * 256])


#---------------------Zad 2---------------------
# a)
im_jpg = Image.open("bombardino.jpg")
statystyki(im)
print("\n")
statystyki(im_jpg)

# b)
diff = ImageChops.difference(im, im_jpg)
diff.show()
print("\n")
statystyki(diff)


#---------------------Zad 3---------------------
# a)
t = np.asarray(im)
t_r = t[:, :, 0]
t_g = t[:, :, 1]
t_b = t[:, :, 2]

r = Image.fromarray(t_r)
g = Image.fromarray(t_g)
b = Image.fromarray(t_b)

# b)
im1 = Image.merge("RGB", (r, g, b))
im_merged = ImageChops.difference(im, im1)

# c)
plt.figure(figsize=(16, 16))
plt.subplot(2,2,1) # ile obrazów w pionie, ile w poziomie, numer obrazu
plt.title("im")
plt.imshow(im)
plt.axis('off')
plt.subplot(2,2,2)
plt.title("im1")
plt.imshow(im_merged)
plt.axis('off')
plt.subplot(2,2,3)
plt.title("Porównianie")
plt.imshow(ImageChops.difference(im, im_merged))
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.25)
plt.savefig('fig1.png')
plt.show()
