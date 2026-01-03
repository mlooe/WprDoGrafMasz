from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageFilter
from PIL import ImageChops
from PIL import ImageOps
from PIL import ImageStat as stat
from PIL.Image import Transpose


def statystyki(im):
    print("tryb obrazu", im.mode)
    print("rozmiar obrazu", im.size)
    s = stat.Stat(im)
    print("extrema ", s.extrema)  # max i min
    print("count ", s.count)  # zlicza
    print("mean ", s.mean)  # srednia
    print("median ", s.median)  # mediana
    print("stddev ", s.stddev)  # odchylenie standardowe

def statystyki_z_maska(im, maska):
    print("tryb obrazu", im.mode,  "tryb maski",  maska.mode)
    print("rozmiar obrazu", im.size, "rozmiar maski", maska.size)
    s = stat.Stat(im, mask = maska)
    print("extrema ", s.extrema)  # max i min
    print("count ", s.count)  # zlicza
    print("mean ", s.mean)  # srednia
    print("median ", s.median)  # mediana
    print("stddev ", s.stddev)  # odchylenie standardowe


print("---------------------Zad 1---------------------")
#---------------------Zad 1---------------------
im = Image.open("postac.jpg")
w,h = im.size
s_w = 0.15
s_h = 0.27
w0 = int(w * s_w)
h0 = int(h * s_h)

im_NEAREST = im.resize((w0,h0), 0, reducing_gap = None)
diff_NEAREST = ImageChops.difference(im_NEAREST, im_NEAREST)
print("Statystyki dla: NEAREST vs NEAREST")
stat1 = statystyki(diff_NEAREST)

im_LANCZOS = im.resize((w0,h0), 1, reducing_gap=None)
diff_LANCZOS = ImageChops.difference(im_NEAREST, im_LANCZOS)
print("\nStatystyki dla: NEAREST vs LANCZOS")
stat2 = statystyki(diff_LANCZOS)

im_BILINEAR = im.resize((w0,h0), 2, reducing_gap = None)
diff_BILINEAR = ImageChops.difference(im_NEAREST, im_BILINEAR)
print("\nStatystyki dla: NEAREST vs BILINEAR")
stat3 = statystyki(diff_BILINEAR)

im_BICUBIC = im.resize((w0,h0), 3, reducing_gap = None)
diff_BICUBIC = ImageChops.difference(im_NEAREST, im_BICUBIC)
print("\nStatystyki dla: NEAREST vs BICUBIC")
stat4 = statystyki(diff_BICUBIC)

im_BOX = im.resize((w0,h0), 4, reducing_gap = None)
diff_BOX = ImageChops.difference(im_NEAREST, im_BOX)
print("\nStatystyki dla: NEAREST vs BOX")
stat5 = statystyki(diff_BOX)

im_HAMMING = im.resize((w0,h0), 5, reducing_gap = None)
diff_HAMMING = ImageChops.difference(im_NEAREST, im_HAMMING)
print("\nStatystyki dla: NEAREST vs HAMMING")
stat6 = statystyki(diff_HAMMING)

plt.figure(figsize=(16, 8))

# NEAREST
plt.subplot(2, 6, 1)
plt.title("NEAREST")
plt.imshow(im_NEAREST)
plt.axis("off")
plt.tight_layout()

plt.subplot(2, 6, 7)
plt.title("diff NEAREST")
plt.imshow(diff_NEAREST)
plt.axis("off")
plt.tight_layout()

# LANCZOS
plt.subplot(2, 6, 2)
plt.title("LANCZOS")
plt.imshow(im_LANCZOS)
plt.axis("off")
plt.tight_layout()

plt.subplot(2, 6, 8)
plt.title("diff LANCZOS")
plt.imshow(diff_LANCZOS)
plt.axis("off")
plt.tight_layout()

# BILINEAR
plt.subplot(2, 6, 3)
plt.title("BILINEAR")
plt.imshow(im_BILINEAR)
plt.axis("off")
plt.tight_layout()

plt.subplot(2, 6, 9)
plt.title("diff BILINEAR")
plt.imshow(diff_BILINEAR)
plt.axis("off")
plt.tight_layout()

# BICUBIC
plt.subplot(2, 6, 4)
plt.title("BICUBIC")
plt.imshow(im_BICUBIC)
plt.axis("off")
plt.tight_layout()

plt.subplot(2, 6, 10)
plt.title("diff BICUBIC")
plt.imshow(diff_BICUBIC)
plt.axis("off")
plt.tight_layout()

# BOX
plt.subplot(2, 6, 5)
plt.title("BOX")
plt.imshow(im_BOX)
plt.axis("off")
plt.tight_layout()

plt.subplot(2, 6, 11)
plt.title("diff BOX")
plt.imshow(diff_BOX)
plt.axis("off")
plt.tight_layout()

# HAMMING
plt.subplot(2, 6, 6)
plt.title("HAMMING")
plt.imshow(im_HAMMING)
plt.axis("off")
plt.tight_layout()

plt.subplot(2, 6, 12)
plt.title("diff HAMMING")
plt.imshow(diff_HAMMING)
plt.axis("off")
plt.tight_layout()
plt.savefig("fig1.png")

#---------------------Zad 2---------------------
box = (200, 50, 450, 300)
box_crop = im.crop(box)
w, h = box_crop.size
w0 = w * 2
h0 = h * 3

# a)
frag_a = im.crop(box).resize((w0, h0), resample=Image.Resampling.BICUBIC)
frag_a.save("zad2a.png")

# b)
frag_b = im.resize((w0,h0), resample=Image.Resampling.BICUBIC, box=box)
frag_b.save("zad2b.png")

difference = ImageChops.difference(frag_a, frag_b)
difference.save("difference.png")

plt.figure(figsize=(10,4))

plt.subplot(1, 4, 1)
plt.title("Fragment")
plt.imshow(box_crop)
plt.axis("off")

plt.subplot(1, 4, 2)
plt.title("Fragment resized")
plt.imshow(frag_b)
plt.axis("off")

plt.subplot(1, 4, 3)
plt.title("Fragment resized + crop")
plt.imshow(frag_a)
plt.axis("off")

plt.subplot(1, 4, 4)
plt.title("Difference")
plt.imshow(difference)
plt.axis("off")
plt.show()

#---------------------Zad 3---------------------
rot_left = im.rotate(60, expand=True, fillcolor=(255, 0, 0))
rot_left.save("rot_left.png")

rot_right = im.rotate(-60, expand=False, fillcolor=(0, 255, 0))
rot_right.save("rot_right.png")

#---------------------Zad 4---------------------
w, h = im.size
new_size = (w * 2, h * 2)

new_im = Image.new("RGB", new_size, (0, 0, 0))
new_im.paste(im, (w, h))
rot = new_im.rotate(45, expand=True)

rot.save("obrot.png")


#---------------------Zad 5---------------------
transpose1 = im.rotate(90, expand=True).transpose(0)
transpose2 = im.rotate(-90).transpose(0)

#transpose1.show()
#transpose2.show()

# Tak, można to uzyskać dzięki obrotowi + flip

#---------------------Zad 6---------------------
postac = Image.open("postac.jpg").convert("RGB")
motyl_src = Image.open("motylek.png").convert("L")

maska_czysta = ImageOps.invert(motyl_src)
maska_czysta = maska_czysta.point(lambda x: 255 if x > 1 else 0)

tlo = Image.open("kolorowe_tlo.png").convert("RGB")
tlo = tlo.resize(maska_czysta.size)

kolorowy_motylek = Image.new('RGB', maska_czysta.size)
kolorowy_motylek.paste(tlo, (0, 0), mask=maska_czysta)

w = postac.width // 6
prop = maska_czysta.height / maska_czysta.width
h = int(w * prop)
size = (w, h)

motyl_res = kolorowy_motylek.resize(size, Image.Resampling.LANCZOS)
maska_res = maska_czysta.resize(size, Image.Resampling.LANCZOS)

motyl_normal = motyl_res
motyl_right = motyl_res.rotate(-60, expand=True, resample=Image.Resampling.BICUBIC)
motyl_left = motyl_res.rotate(60, expand=True, resample=Image.Resampling.BICUBIC)

maska_normal = maska_res
maska_right = maska_res.rotate(-60, expand=True, fillcolor=0)
maska_left = maska_res.rotate(60, expand=True, fillcolor=0)

postac.paste(motyl_normal, (50, 400), mask=maska_normal)
postac.paste(motyl_right, (400, 500), mask=maska_right)
postac.paste(motyl_left, (300, 300), mask=maska_left)

postac.save("postac_motylki.png")
