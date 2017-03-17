import resource
import pyglet
import player
from pyglet import clock
#import touhou
import Danmaku
window = pyglet.window.Window(640, 480)
play = player.player('Cirno')

window.push_handlers(play.get_key_handler())
fps_display = clock.ClockDisplay()

def update(dt=None):
    window.clear()
    play.update()
    play.keyupdata()
    play.draw()
    play.shiftdraw()
    fps_display.draw()
    for i in range(len(Danmaku.player_danmaku_batch)):
        if Danmaku.player_danmaku_batch[i].y>400:
            try:
                Danmaku.player_danmaku_batch[i].delete()
            except:
                pass
        else:
            Danmaku.player_danmaku_batch[i].y+=10
            Danmaku.player_danmaku_batch[i].draw()


pyglet.clock.schedule_interval(update, 1 / 60.0)
pyglet.app.run()
