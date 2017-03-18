import pyglet
import pyglet.image.codecs
import pyglet.sprite
import sqlite3
import pprint
import copy
import util
sqlitedata = sqlite3.connect("Sprite.db3")
resource = dict()
imagedata = dict()


def sqlitedatatodict(sqlitedata):
    cursor = sqlitedata.cursor()
    cursor.execute(u"select * from main")
    for i in cursor.fetchall():
        Name, tablename = i
        dictobject = {}
        resource[str(Name)] = dictobject
        tableintable(sqlitedata, dictobject, str(tablename))
    cursor.close()


def tableintable(sqlitedata, dictobject, tablename):
    cu = sqlitedata.cursor()
    cu.execute("select * from " + tablename)
    for i in cu.fetchall():
        Name, tablename = i
        dictobjectr = {}
        dictobject[str(Name)] = dictobjectr
        tabletoobject(sqlitedata, dictobjectr, str(tablename))
    cu.close()


def tabletoobject(sqlitedata, dictobject, tablename):
    cu = sqlitedata.cursor()
    cu.execute("select * from " + tablename)
    for i in cu.fetchall():
        Name, ImageObject, region_x, region_y, width, height, anchor_x, anchor_y = i
        Name, ImageObject=str(Name), str(ImageObject)
        if ImageObject not in imagedata.keys() :
            imagedata[ImageObject] = pyglet.image.load(ImageObject)
        image = imagedata[ImageObject]
        img = image.get_region(region_x, image.height - region_y - height, width, height)
        img.anchor_x, img.anchor_y = anchor_x, anchor_y
        dictobject[Name] = util.Sprite(img)
    cu.close()

sqlitedatatodict(sqlitedata)
pprint.pprint(resource)


def playerimagelistospritedict(playername):
    tmp = {"stand": [], "left": [], "right": []}
    lister = resource['Player'][playername]
    for i in lister.keys():
        if not i.find('Stand'):
            tmp["stand"].append(lister[i])
        elif not i.find("Left"):
            tmp["left"].append(lister[i])
        elif not i.find("Right"):
            tmp["right"].append(lister[i])
        else:
            pass

    return tmp