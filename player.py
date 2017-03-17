import resource
import pyglet
from pyglet.window import key
import newresource
import Danmaku



class player:
    x = 320
    y = 240
    id = 0
    state = 0
    keys = dict(left=False, right=False, up=False, down=False)
    sprite=None
    shift = bool(0)
    key_handler = key.KeyStateHandler()

    def __init__(self,playername):
        self.x = 320
        self.y = 240
        self.__event_z=bool(0)
        self.id = 0
        self.state = 0
        self.keys = dict(left=False, right=False, up=False, down=False)
        self.sprite = resource.sprite
        self.shift = 0
        self.__shiftid=0
        self.key_handler = key.KeyStateHandler()
        self.shiftsprite = [pyglet.sprite.Sprite(resource.shift), pyglet.sprite.Sprite(resource.shift)]
        self.sprite=newresource.playerimagelistospritedict(playername)
        self.___id=0
    def update_x_y(self):
        for i in self.sprite.keys():
            for j in self.sprite[i]:
                j._set_x(self.x)
                j._set_y(self.y)
        for i in self.shiftsprite:
            i._set_x(self.x)
            i._set_y(self.y)

    def draw(self):
        self.update_x_y()
        tmp = None
        if self.state == 0:
            tmp = self.sprite["stand"]
        elif self.state == 1:
            tmp = self.sprite["left"]
        elif self.state == 2:
            tmp = self.sprite["right"]
        tmp[self.id].draw()

    def update(self):
        if self.state:
            if self.id >= 7:
                pass
            else:
                self.id += 1
        else:
            if self.id >= 7:
                self.id = 0
            else:
                self.id += 1

    def keyupdata(self, symbol=None, modifiers=None):
        keyer = dict(left=False, right=False, up=False, down=False,z=False)
        if self.___id!=0:
            self.___id-=1

        if self.key_handler[key.Z]:
            if self.___id == 0:
                self.___id=8
                #print
                danmu=pyglet.sprite.Sprite(newresource.resource['PlayerDanmaku']['CirnoDanmaku']['1'],
                                                                     x=self.x, y=self.y+16)
                danmu.rotation=90
                Danmaku.player_danmaku_batch.append(danmu)
                danmu=pyglet.sprite.Sprite(newresource.resource['PlayerDanmaku']['CirnoDanmaku']['1'],
                                                                     x=self.x+16, y=self.y+16)
                danmu.rotation=90
                Danmaku.player_danmaku_batch.append(danmu)

            #Danmaku.Danmuku('1',self.x,self.y+16)
        if self.key_handler[key.LSHIFT]:
            self.shift = 1
            dx = 1
        else:
            self.shift = 0
            self.__shiftid = 0
            dx = 5
        if self.key_handler[key.UP]:
            keyer['up'] = True
            self.change_y(dx)
        if self.key_handler[key.LEFT]:
            keyer['left'] = True
            self.change_x(-dx)
        if self.key_handler[key.RIGHT]:
            keyer['right'] = True
            self.change_x(dx)
        if self.key_handler[key.DOWN]:
            keyer['down'] = True
            self.change_y(-dx)
        for i in self.keys.keys():
            if keyer[i] != self.keys[i]:
                self.keys[i] = keyer[i]
                if i == 'up' or i == 'down':
                    pass
                else:
                    if keyer[i] == True:
                        if i == 'left':
                            self.id = 0
                        if i == 'right' and keyer[i] == True:
                            self.id = 0
                    elif keyer[i] == False:
                        self.id = 0
        self.state = 0
        if keyer["right"]==True and keyer["left"]==True:
            return
        if keyer["left"]:
            self.state=1
        if keyer['right']:
            self.state=2


    def shiftdraw(self):
        if self.shift:
            self.shiftsprite[0].rotation += 2.0
            self.shiftsprite[1].rotation -= 2.0
            if self.__shiftid==0:
                self.__shiftid=1
                self.shiftsprite[0].rotation = 0
                self.shiftsprite[1].rotation = 0
            self.shiftsprite[0].draw()
            self.shiftsprite[1].draw()
    def event_z(self):
        pass
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def change_x(self, ints):
        if ints > 0:
            if self.x >= 640 - 32:
                pass
            else:
                self.x += ints
        else:
            if self.x <= 0 + 32:
                pass
            else:
                self.x += ints

    def change_y(self, ints):
        if ints > 0:
            if self.y >= 480 - 32:
                pass
            else:
                self.y += ints
        else:
            if self.y <= 0 + 32:
                pass
            else:
                self.y += ints

    def get_id(self):
        return self.id

    def get_state(self):
        return self.state

    def get_keys(self):
        return self.keys

    def get_sprite(self):
        return self.sprite

    def get_key_handler(self):
        return self.key_handler
