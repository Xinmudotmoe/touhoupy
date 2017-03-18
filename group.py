# coding=utf-8
import pyglet as pyglet
import time as _time
import player as _player

enemyBatch = list()
bossBatch = list()
plDanmakuBatch = list()
player = None
enemyDanmakuBatch = list()
particleBatch = list()
guiBatch = list()
[ISDEAD, DANMUAKUSPRITE, X, Y, ROTATION, DIRECTION, TMP, TIME, FUNC] = range(0, 9)


def danmukuobject(isdead, danmukusprite, x, y, rotation, direction, func):
    tmp = list()
    return list((isdead, danmukusprite, x, y, rotation, direction, tmp, _time.clock(), func))


def _init_danmukuobject():
    return danmukuobject(1, 0, 0, 0, 0, 0, 0)


def _init():
    for i in range(0, 1024):
        plDanmakuBatch.append(_init_danmukuobject())
        enemyDanmakuBatch.append(_init_danmukuobject())
        particleBatch.append(_init_danmukuobject())
        if i < 128:
            enemyBatch.append(_init_danmukuobject())
            bossBatch.append(_init_danmukuobject())
            guiBatch.append(_init_danmukuobject())


def draw():
    for i in enemyBatch:
        if i[0] == 0:
            i[1].arg_draw(i[X], i[Y], i[ROTATION])
    for i in bossBatch:
        if i[0] == 0:
            i[1].arg_draw(i[X], i[Y], i[ROTATION])
    for i in plDanmakuBatch:
        if i[0] == 0:
            i[1].arg_draw(i[X], i[Y], i[ROTATION])
    if player:
        player.draw()
        _player.shift.draw(*player.get_position())
    for i in enemyDanmakuBatch:
        if i[0] == 0:
            i[1].arg_draw(i[X], i[Y], i[ROTATION])
    for i in particleBatch:
        if i[0] == 0:
            i[1].arg_draw(i[X], i[Y], i[ROTATION])
    for i in guiBatch:
        if i[0] == 0:
            i[1].arg_draw(i[X], i[Y], i[ROTATION])


_init()
