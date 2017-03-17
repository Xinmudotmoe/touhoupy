pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass

import resource
import newresource
import pyglet
import player
import pyglet.window.key
key_handler=pyglet.window.key.KeyStateHandler()
doplayer=None
def defplayer(playername=""):
    global doplayer
    doplayer=player.player(playername=playername)
def update(dt=None):
    pass