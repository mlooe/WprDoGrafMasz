from PIL import Image, ImageFilter
from matplotlib import pyplot as plt

print("---------------------Zad 1---------------------")
#---------------------Zad 1---------------------
obraz = Image.open("obraz.png")
print("Tryb obrazu: ", obraz.mode)
print("rozmiar", obraz.size)

def filtruj(obraz, kernel, scale):
    size = int(len(kernel)**0.5)
    size_tuple = (size, size)
    kernel_filter = ImageFilter.Kernel(size_tuple, kernel, scale=scale, offset=0)
    obraz_po_filter = obraz.filter(kernel_filter)
    return obraz_po_filter

print("---------------------Zad 2---------------------")
#---------------------Zad 2---------------------
#a)
obraz_blur_2a = obraz.filter(ImageFilter.BLUR)

#b)
print("Informacje filtru BLUR:")
print(ImageFilter.BLUR.filterargs)
obraz_blur_2b = filtruj(obraz, (1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1), 16)

#c)
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(obraz)
plt.title("Oryginał")
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(obraz_blur_2a)
plt.title("Gotowy filtr BLUR")
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(obraz_blur_2b)
plt.title("Funkcja filtruj (z parametrami filtru BLUR)")
plt.axis('off')
plt.tight_layout()
plt.show()
#plt.savefig("zad2.png")

print("---------------------Zad 3---------------------")
#---------------------Zad 3---------------------
#a)
obraz_contour_3a = obraz.filter(ImageFilter.CONTOUR)

#b)
print("Informacje filtru CONTOUR:")
print(ImageFilter.CONTOUR.filterargs)
obraz_contour_3b = filtruj(obraz, (-1, -1, -1, -1, 8, -1, -1, -1, -1), 1)

#c)
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(obraz)
plt.title("Oryginał")
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(obraz_contour_3a)
plt.title("Gotowy filtr CONTOUR")
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(obraz_contour_3b)
plt.title("Funkcja CONTOUR (z parametrami filtru CONTOUR)")
plt.axis('off')
plt.tight_layout()
plt.show()
#plt.savefig("zad3.png")

print("---------------------Zad 4---------------------")
#---------------------Zad 4---------------------
obraz_L = obraz.convert('L')

#a)
obraz_emboss = obraz_L.filter(ImageFilter.EMBOSS)

#b)
print("Informacje filtru EMBOSS:")
print(ImageFilter.EMBOSS.filterargs)

obraz_sobel_4b_1 = filtruj(obraz_L,(-1, 0, 1, -2, 0, 2, -1, 0, 1), 1)
obraz_sobel_4b_2 = filtruj(obraz_L, (-1, -2, -1, 0, 0, 0, 1, 2, 1), 1)

#c)
plt.figure(figsize=(15, 15))

plt.subplot(2, 2, 1)
plt.imshow(obraz_L, cmap='gray')
plt.title("Obraz L")
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(obraz_emboss, cmap='gray')
plt.title("Gotowy filtr EMBOSS")
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(obraz_sobel_4b_1, cmap='gray')
plt.title("Obraz z listą kernel SOBEL1")
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(obraz_sobel_4b_2, cmap='gray')
plt.title("Obraz z listą kernel SOBEL2")
plt.axis('off')

plt.tight_layout()
#plt.savefig("fig2.png")
plt.show()
