# coding=utf-8
from pyglet.window import key
import resource
import Danmaku
import util


class player:
    x = 320
    y = 240
    id = 0
    state = 0
    keys = dict(left=False, right=False, up=False, down=False)
    sprite = None
    shift = bool(0)
    key_handler = util.key_handler

    def __init__(self, playername):
        self.x = 320
        self.y = 240
        self.__event_z = bool(0)
        self.id = 0
        self.state = 0
        self.keys = dict(left=False, right=False, up=False, down=False)
        self.key_handler = util.key_handler
        self.sprite = resource.playerimagelistospritedict(playername)
        self.drawsprite = self.sprite["stand"][0]
        self.__cooling = 0

    def draw(self):
        self.update()
        tmp = None
        if self.state == 0:
            tmp = self.sprite["stand"]
        elif self.state == 1:
            tmp = self.sprite["left"]
        elif self.state == 2:
            tmp = self.sprite["right"]
        tmp[self.id].arg_draw(self.x, self.y)

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

    def keyupdata(self, dt):
        keyer = dict(left=False, right=False, up=False, down=False, z=False)

        self.__cooling += dt

        if self.key_handler[key.Z]:
            if self.__cooling > 0.13:
                self.__cooling = 0

                Danmaku.add_plDanmuku(resource.resource['PlayerDanmaku']['CirnoDanmaku']['1'],
                                      self.x, self.y + 16, 90.0, Danmaku.plDanmakuplus)
                Danmaku.add_plDanmuku(resource.resource['PlayerDanmaku']['CirnoDanmaku']['1'],
                                      self.x + 16, self.y + 16, 90.0, Danmaku.plDanmakuplus)

        if self.key_handler[key.LSHIFT]:
            dx = 60 * dt
        else:
            dx = 300 * dt
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
                    if keyer[i]:
                        if i == 'left':
                            self.id = 0
                        if i == 'right' and keyer[i]:
                            self.id = 0
                    elif not keyer[i]:
                        self.id = 0
        self.state = 0
        if keyer["right"] and keyer["left"]:
            return
        if keyer["left"]:
            self.state = 1
        if keyer['right']:
            self.state = 2

    def get_position(self):
        return self.x, self.y

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


play = player('Reimu')


class shift_sprite:
    def __init__(self):
        self.__shiftid = 0
        self.sprite = resource.resource['PlayerDanmaku']['CirnoDanmaku']['TEMPconetama2']
        self.rotation = 0.0

    def draw(self, x, y):
        if util.key_handler[key.LSHIFT]:
            if self.__shiftid == 0:
                self.__shiftid = 1
                self.rotation = 0
            for i in range(0, 2):
                self.rotation += 2.0
                self.sprite.arg_draw(x, y, self.rotation if i == 1 else -self.rotation)
        else:
            self.__shiftid = 0


shift = shift_sprite()
