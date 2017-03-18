# coding=utf-8
import group
from group import ISDEAD, DANMUAKUSPRITE, X, Y, ROTATION, DIRECTION, TMP, TIME, FUNC
import time as _time


def add_plDanmuku(danmukusprite, x, y, rotation, func):
    for i in group.plDanmakuBatch:
        if i[0] == 1:
            i[ISDEAD] = 0
            i[DANMUAKUSPRITE] = danmukusprite
            i[X] = x
            i[Y] = y
            i[ROTATION] = rotation
            i[TIME] = _time.clock()
            i[FUNC] = func
            return


def plDanmakuplus(lists):
    lists[Y] += (_time.clock() - lists[7]) * 600
    lists[TIME] = _time.clock()

