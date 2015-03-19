import sys, PIL.Image

img = PIL.Image.open(sys.argv[-1]).convert('L')

threshold = 128*[0] + 128*[255]

for y in range(img.size[1]):
    for x in range(img.size[0]):
        old = img.getpixel((x, y))
        new = threshold[old]
        err = (old - new) # difference from right value

        img.putpixel((x, y), new)

        
        nxy = (x+1, y)
        try:
            img.putpixel(nxy, img.getpixel(nxy) + err*0.5)
        except IndexError:
            pass

        nxy = (x-1, y+1)
        try:
            img.putpixel(nxy, img.getpixel(nxy) + err*0.2)
        except IndexError:
            pass

        nxy = (x, y+1)
        try:
            img.putpixel(nxy, img.getpixel(nxy) + err*0.3)
        except IndexError:
            pass

name=sys.argv[-1]
name=name.split(".")
name='bit-'+name[0]+'.png'
img.save(name, optimize=True)
