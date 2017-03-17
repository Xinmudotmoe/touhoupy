import pyglet
import pyglet.image.codecs
import pyglet.sprite

constpl00 = (
    ("pl00A0", 0, 0, 32, 48, 16, 24),
    ("pl00A1", 32, 0, 32, 48, 16, 24),
    ("pl00A2", 64, 0, 32, 48, 16, 24),
    ("pl00A3", 96, 0, 32, 48, 16, 24),
    ("pl00A4", 128, 0, 32, 48, 16, 24),
    ("pl00A5", 160, 0, 32, 48, 16, 24),
    ("pl00A6", 192, 0, 32, 48, 16, 24),
    ("pl00A7", 224, 0, 32, 48, 16, 24),
    ("pl00B0", 0, 48, 32, 48, 16, 24),
    ("pl00B1", 32, 48, 32, 48, 16, 24),
    ("pl00B2", 64, 48, 32, 48, 16, 24),
    ("pl00B3", 96, 48, 32, 48, 16, 24),
    ("pl00B4", 128, 48, 32, 48, 16, 24),
    ("pl00B5", 160, 48, 32, 48, 16, 24),
    ("pl00B6", 192, 48, 32, 48, 16, 24),
    ("pl00B7", 224, 48, 32, 48, 16, 24),
    ("pl00C0", 0, 96, 32, 48, 16, 24),
    ("pl00C1", 32, 96, 32, 48, 16, 24),
    ("pl00C2", 64, 96, 32, 48, 16, 24),
    ("pl00C3", 96, 96, 32, 48, 16, 24),
    ("pl00C4", 128, 96, 32, 48, 16, 24),
    ("pl00C5", 160, 96, 32, 48, 16, 24),
    ("pl00C6", 192, 96, 32, 48, 16, 24),
    ("pl00C7", 224, 96, 32, 48, 16, 24))
conetama2 = ('etama2.png', 0, 16, 64, 64, 32, 32)
etama2 = pyglet.image.load("etama2.png")
pl00 = dict()
pl00["Image"] = pyglet.image.load("pl00.png")
width = pl00["Image"].width
height = pl00["Image"].height
pl00["Playerimages"] = []
for i in constpl00:
    tmp = pl00["Image"].get_region(i[1], height - i[2] - i[4], i[3], i[4])
    tmp.anchor_x, tmp.anchor_y = i[5:]
    pl00["Playerimages"].append(tmp)
    # tmp.save(i[0]+'.png',encoder=pyglet.image.codecs.png.PNGImageEncoder())#debug
image = {"stand": [], "left": [], "right": []}
for i in range(8):
    image["stand"].append(pl00['Playerimages'][i])
    image["left"].append(pl00['Playerimages'][i + 8])
    image["right"].append(pl00['Playerimages'][i + 16])
sprite = {"stand": [], "left": [], "right": []}
for i in range(8):
    sprite["stand"].append(pyglet.sprite.Sprite(image["stand"][i]))
    sprite["left"].append(pyglet.sprite.Sprite(image["left"][i]))
    sprite["right"].append(pyglet.sprite.Sprite(image["right"][i]))
shift = etama2.get_region(conetama2[1], etama2.height - conetama2[2] - conetama2[4], conetama2[3], conetama2[4])
shift.anchor_x, shift.anchor_y = conetama2[5:7]
