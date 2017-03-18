# coding=utf-8
import pyglet
import math
from pyglet.window import key
import threading


class Sprite(pyglet.sprite.Sprite):
    def __init__(self, img, x=0, y=0):
        pyglet.sprite.Sprite.__init__(self, img, x, y)
        self.lock = threading.Lock()
        self.base_x = 0
        self.base_y = 0
        self.base_rotation = 0

    """docstring for Sprite"""

    def arg_draw(self, x, y, rotation=0.0):
        # type: (float, float, float) -> None
        x = int(x)
        y = int(y)
        img = self._texture
        if not self._visible:
            vertices = [0, 0, 0, 0, 0, 0, 0, 0]
        elif rotation:
            x1 = -img.anchor_x * self._scale
            y1 = -img.anchor_y * self._scale
            x2 = x1 + img.width * self._scale
            y2 = y1 + img.height * self._scale

            r = -math.radians(rotation)
            cr = math.cos(r)
            sr = math.sin(r)
            ax = x1 * cr - y1 * sr + x
            ay = x1 * sr + y1 * cr + y
            bx = x2 * cr - y1 * sr + x
            by = x2 * sr + y1 * cr + y
            cx = x2 * cr - y2 * sr + x
            cy = x2 * sr + y2 * cr + y
            dx = x1 * cr - y2 * sr + x
            dy = x1 * sr + y2 * cr + y
            vertices = [ax, ay, bx, by, cx, cy, dx, dy]
        elif self._scale != 1.0:
            x1 = x - img.anchor_x * self._scale
            y1 = y - img.anchor_y * self._scale
            x2 = x1 + img.width * self._scale
            y2 = y1 + img.height * self._scale
            vertices = [x1, y1, x2, y1, x2, y2, x1, y2]
        else:
            x1 = x - img.anchor_x
            y1 = y - img.anchor_y
            x2 = x1 + img.width
            y2 = y1 + img.height
            vertices = [x1, y1, x2, y1, x2, y2, x1, y2]
        if not self._subpixel:
            vertices = [int(v) for v in vertices]
        self.lock.acquire()
        self._vertex_list.vertices[:] = vertices
        self.draw()
        self.lock.release()


key_handler = key.KeyStateHandler()
