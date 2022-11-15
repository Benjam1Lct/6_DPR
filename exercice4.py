from PIL import Image
im = Image.open("assets/image.png")
largeur, hauteur = im.size
px = im.load()

def rotation_aux(px, x, y, t):
    if t==1:
        return
    else:
        t//=2
        rotation_aux(px, x, y, t)
        rotation_aux(px, x-t, y, t)
        rotation_aux(px, x, y-t, t)
        rotation_aux(px, x-t, y-t, t)
        for i in range():
            for j in range():

def rotation(px, taille):
    rotation_aux(px)
    im.save("rotation.png")

if __name__=="__main__":
    rotation(px, )
