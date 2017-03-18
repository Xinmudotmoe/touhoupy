# coding=utf-8
import threading
import resource
import pyglet
import player
import time as _time
import group
import util

play = None
clock = _time.clock()

window = pyglet.window.Window(640, 480)
window.push_handlers(util.key_handler)
fps_display = pyglet.clock.ClockDisplay()


def defplayer(playername=""):
    global play
    play = player.player(playername=playername)
    group.player = play


def runtime():
    global clock
    dt = _time.clock() - clock
    clock = _time.clock()
    play.update()
    play.keyupdata(dt)
    global fps_display
    for i in group.enemyBatch:
        if i[0] == 0:
            x = i[group.X]
            y = i[group.Y]
            if x < 0 or x > 640:
                i[group.ISDEAD] = 1
            elif y < 0 or y > 480:
                i[group.ISDEAD] = 1
            else:
                if i[group.FUNC]:
                    i[group.FUNC](i)
    for i in group.plDanmakuBatch:
        if i[0] == 0:
            x = i[group.X]
            y = i[group.Y]
            if x < 0 or x > 640:
                i[group.ISDEAD] = 1
            elif y < 0 or y > 480:
                i[group.ISDEAD] = 1
            else:
                if i[group.FUNC]:
                    i[group.FUNC](i)
    for i in group.enemyDanmakuBatch:
        if i[0] == 0:
            x = i[group.X]
            y = i[group.Y]
            if x < 0 or x > 640:
                i[group.ISDEAD] = 1
            elif y < 0 or y > 480:
                i[group.ISDEAD] = 1
            else:
                if i[group.FUNC]:
                    i[group.FUNC](i)


def draw_update(*args):
    #*args不可省略
    window.clear()
    group.draw()
    fps_display.draw()


def tmp():
    while 1:
        runtime()
        _time.sleep(0.0004)


pyglet.clock.schedule_interval(draw_update, 1 / 60.0)
defplayer("Cirno")
runtimeThread = threading.Thread(target=tmp)
runtimeThread.setDaemon(True)
runtimeThread.start()
pyglet.app.run()
