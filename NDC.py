import pyxel

pyxel.init(128, 128, title="NDC 2023", display_scale=6, fps=60)
pyxel.load("3.pyxres")

spaceship_x:64
spaceship_y:64

def spaceship_displacement:
    if pyxel.btn(pyxel.key

def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit
        
def draw():
    pyxel.cls(0)
    pyxel.rect(10,10,20,20,11)
    
pyxel.run(update, draw)