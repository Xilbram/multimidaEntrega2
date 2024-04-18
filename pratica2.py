from urllib.request import urlopen
from PIL import Image # package pillow
import math

def criarImagemRGB():
    img = Image.new( "RGB", (512,256))
    raster = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            #raster[i,j] = (220,219,97,255) # R=220,G=219,B=98,alfa=255, amarelo
            raster[i,j] = (220,219,97,255)
    (r, g, b) = img.getpixel((0, 0))
    print("Size: " + str(img.size[0]))
    print(r, g, b)
    return img

def criarImagemCinza():
    img = Image.new( "L", (256,256))
    raster = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            raster[i,j] = i #0 ate 255
    y = img.getpixel((5, 5))
    print(y)
    return img

def criarImagemBinaria():
    # checkerboard pattern.
    img = Image.new("1", (500,500))
    raster = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if ((int(i/50)+int(j/50)) % 2 == 0):
                raster[i,j] = 0 
            else:
                raster[i,j] = 1
    y = img.getpixel((0, 0))
    print(y)
    return img

def reduzirPeixe():
    peixeImg = Image.open(urlopen("https://www.inf.ufsc.br/~roberto.willrich/INE5431/peixe.jpg"))
    peixeLargura = peixeImg.size[0] 
    peixeAltura = peixeImg.size[1] 
    newL = int(peixeLargura - (peixeLargura/4))
    newA = int(peixeAltura - (peixeAltura/4))
    newImg = Image.new("RGB", (newL,newA))
    raster = newImg.load()
    for i in range(newL):
        for j in range(newA):
            raster[i,j] = peixeImg.getpixel((i,j))
    return newImg

img = Image.open(urlopen("https://www.inf.ufsc.br/~roberto.willrich/INE5431/peixe.jpg"))
img.show()
#criarImagemRGB().show()
#criarImagemCinza().show()
#criarImagemBinaria().show()
reduzirPeixe().show()
