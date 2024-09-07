from js import myfunc,jsval
import pyxel

pyxel.init(240,160)
pyxel.mouse(True)
val = "no data"
ret = "nothing"
def update():
    global val,ret
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        ret = myfunc("from Pyxel!")
        val = jsval

    return

def draw():
    pyxel.cls(1)
    pyxel.text(40,40, "Click to test.",7)
    pyxel.text(40,50, "ret = "+str(ret),7)
    pyxel.text(40,60, "val = "+str(val),7)
    return

pyxel.run(update,draw)
