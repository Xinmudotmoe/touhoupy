import newresource
import pyglet
player_danmaku_batch=[]

from pyglet.gl import GL_QUADS
class Danmuku(pyglet.sprite.Sprite):
    def __init__(self,danmuku,x,y):
        pyglet.sprite.Sprite.__init__(self,newresource.resource['PlayerDanmaku']['CirnoDanmaku'][danmuku],x=x,y=y)
        self._set_batch(batch=player_danmaku_batch)
        self.rotation=90
    def draw(self):
        self._set_y+=10
        self._group.set_state_recursive()
        self._vertex_list.draw(GL_QUADS)
        self._group.unset_state_recursive()
def new_Player_Danmaku(x,y):
    Danmuku('1',x=x,y=y+16)