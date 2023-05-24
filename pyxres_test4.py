import pyxel,random

pyxel.init(128, 128, title="NDC 2023",fps=60)
tirs_liste=[]
vaisseau_x = 64
vaisseau_y = 64
ennemis_liste = []
vies=3
score=0
debut=False
pyxel.text(120,120,'score',7)
pyxel.load("3.pyxres")
def vaisseau_mouvement(x, y):
    """déplacement avec les touches de directions"""

    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x < 120) :
            x = x + 1
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > 0) :
            x = x - 1
    if pyxel.btn(pyxel.KEY_DOWN):
        if (y < 120) :
            y = y + 1
    if pyxel.btn(pyxel.KEY_UP):
        if (y > 0) :
            y = y - 1
    return x, y

def tirs_creation(x, y, tirs_liste):
    """création d'un tir avec la barre d'espace"""

    # btnr pour eviter les tirs multiples
    if pyxel.btnr(pyxel.KEY_SPACE):
        tirs_liste.append([x-1, y-7])
    return tirs_liste


def tirs_deplacement(tirs_liste):
    """déplacement des tirs vers le haut et suppression s'ils sortent du cadre"""

    for tir in tirs_liste:
        tir[1] -= 1
        if  tir[1]<-8:
            tirs_liste.remove(tir)
    return tirs_liste


def ennemis_creation(ennemis_liste):
    """création aléatoire des ennemis"""

    # un ennemi par seconde
    if (pyxel.frame_count % 30 == 0):
        ennemis_liste.append([random.randint(0, 120), 0])
    return ennemis_liste

def vaisseau_suppression(vies):
    """disparition du vaisseau et d'un ennemi si contact"""

    for ennemi in ennemis_liste:
        if ennemi[0] <= vaisseau_x+8 and ennemi[1] <= vaisseau_y+8 and ennemi[0]+8 >= vaisseau_x and ennemi[1]+8 >= vaisseau_y:
            ennemis_liste.remove(ennemi)
            vies -=1
    return vies


def ennemis_suppression(score):
    """disparition d'un ennemi et d'un tir si contact"""

    for ennemi in ennemis_liste:
        for tir in tirs_liste:
            if ennemi[0] <= tir[0]+1 and ennemi[0]+11 >= tir[0] and ennemi[1]+11 >= tir[1]:
                ennemis_liste.remove(ennemi)
                tirs_liste.remove(tir)
                score=score+1
    return score


def ennemis_deplacement(ennemis_liste):
    """déplacement des ennemis vers le haut et suppression s'ils sortent du cadre"""

    for ennemi in ennemis_liste:
        ennemi[1] += 1
        if  ennemi[1]>128:
            ennemis_liste.remove(ennemi)
    return ennemis_liste


def actualisation():
    """mise à jour des variables (60 fois par seconde)"""
    global vaisseau_x, vaisseau_y, tirs_liste, ennemis_liste, vies, score,debut
    if pyxel.btn(pyxel.KEY_RETURN) and debut == False:
        debut = True
    
    if debut == True :
        
        
        

        # mise à jour de la position du vaisseau
        vaisseau_x, vaisseau_y = vaisseau_mouvement(vaisseau_x, vaisseau_y)

        # creation des tirs en fonction de la position du vaisseau
        tirs_liste = tirs_creation(vaisseau_x, vaisseau_y, tirs_liste)

        # mise a jour des positions des tirs
        tirs_liste = tirs_deplacement(tirs_liste)

        # creation des ennemis
        ennemis_liste = ennemis_creation(ennemis_liste)

        # mise a jour des positions des ennemis
        ennemis_liste = ennemis_deplacement(ennemis_liste)

        # suppression des ennemis et tirs si contact

        score= ennemis_suppression(score)


        # suppression du vaisseau et ennemi si contact
        vies = vaisseau_suppression(vies)


def objet():
    """création des objets """
    if debut==True:
        pyxel.cls(0)
       # si le vaisseau possede des vies le jeu continue
        if vies > 0:
            pyxel.cls(0)
            pyxel.text(0,7,f'score:{score}',7)
            pyxel.text(0,0,f'vies:{vies}',8)
               #pyxel.rect(vaisseau_x, vaisseau_y, 8, 8, 1)
            pyxel.blt(vaisseau_x, vaisseau_y, 0, 0, 0, 9, 7)
            for tir in tirs_liste:
                pyxel.blt(tir[0], tir[1], 0, 9, 0, 10, 7)
                   # ennemis
            for ennemi in ennemis_liste:
                pyxel.blt(ennemi[0], ennemi[1] ,0,20,11,11,11 )
          
        if vies==0:
            pyxel.text(50,64,'GAME OVER',10)
          
    else:
        pyxel.cls(0)
        pyxel.blt(20, 32,0,0,30,84,42)
        pyxel.text(20,82,f"press 'ENTER' to start",7)
        pyxel.playm(2,loop=False)
pyxel.run(actualisation, objet)



