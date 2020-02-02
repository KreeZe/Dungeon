#Jeu Fait Par Yamis MANFALOTI

"""
Librairies
"""
import time
import pygame
from random import*


"""
    Initialisation pygame + paramètre
"""
hauteur = 14
largeur = 12
TITLE_SIZE = 48
pygame.init()
fenetre = pygame.display.set_mode((largeur*TITLE_SIZE, (hauteur+1)*TITLE_SIZE))
pygame.display.set_caption("Jeu")
font = pygame.font.Font('freesansbold.ttf', 20)

"""
Fonction Main
"""

def main():
    """
    Initialisation Variable Main
    """
    loop = True
    tiles=[]
    numeroTile = ''
    NB_TILES = 38
    hauteur = 14
    largeur = 12
    TITLE_SIZE = 48
    joueurX = 1
    joueurY = 2
    posX = ''
    posY = ''
    bas = 2
    droite = 1
    player = 12
    cooldownDash = 0
    cooldownCoffre = 0
    coffre = 0
    attaque = 0
    countTemps  = 0
    countTemps2 = 0
    countTemps3 = 0
    countTemps4 = 0
    countTemps5 = 0
    countTemps6 = 0
    vieJoueur = 100
    direction = ''
    dash = 0

    #ennemie
    FRAMERATE_ennemie= 50   #vitesse du ennemie chiffre elevé = vitesse lente
    NB_DEPLACEMENT_ennemie = 10  #le ennemie se deplace sur 9 cases
    frameRateCounterennemie=0
    positionennemie = 1
    posfX1,posfY1 = 1,3
    posfX2,posfY2 = 7,6
    posfX3,posfY3 = 1,9
    vieMob1 = 100
    vieMob2 = 100
    vieMob3 = 100
    mortMob1 = 0
    mortMob2 = 0
    mortMob3 = 0
    lvl = 0



    niveauVierge = [
    [8 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,9 ],
    [1 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,2 ],
    [1 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,2 ],
    [1 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,2 ],
    [1 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,2 ],
    [1 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,2 ],
    [1 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,2 ],
    [1 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,2 ],
    [1 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,2 ],
    [1 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,2 ],
    [1 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,2 ],
    [1 ,7 ,7 ,7 ,7 ,7 ,0 ,7 ,7 ,7 ,7 ,2 ],
    [1 ,4 ,4 ,4 ,4 ,4 ,4 ,4 ,4 ,4 ,4 ,2 ],
    [10,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,11] ]


    """
    Differente Fonctions
    """

    def chargetiles(tiles): #fonction permettant de charger les images tiles dans une liste tiles[]
        for n in range(0,NB_TILES):
            tiles.append(pygame.image.load('data/'+str(n)+'.png'))

    def afficheNiveau(niveau): #affiche le niveau a partir de la liste a deux dimensions niveau[][]
        for y in range(hauteur):
            for x in range(largeur):
                fenetre.blit(tiles[niveau[y][x]],(x*TITLE_SIZE,y*TITLE_SIZE))

    def affichePac(numero):  #affiche le pacman en position joueurX et joueurY
        if numeroTile == 4 or numeroTile == 6:
            fenetre.blit(tiles[numero],(joueurX * TITLE_SIZE,joueurY * TITLE_SIZE-15))
        elif (numeroTile == 1 or numeroTile == 2) and joueurY == 12:
            fenetre.blit(tiles[numero],(joueurX * TITLE_SIZE,joueurY * TITLE_SIZE-15))
        else:
            fenetre.blit(tiles[numero],(joueurX * TITLE_SIZE,joueurY * TITLE_SIZE-5))

    def cooldown(CooldownEnSec):
        start = time.time()
        end = 0
        while end <= CooldownEnSec :
            end = time.time() - start
        return 'passed'

    def deplaceEnnemie(posfX,posfY,monstre):
        if posfX <= 1:
            posfX = 1
            mob = tiles[monstre].convert_alpha()
            fenetre.blit(mob,(posfX * TITLE_SIZE,posfY * TITLE_SIZE))
            return posfX,posfY
        else:
            mob = tiles[monstre].convert_alpha()
            fenetre.blit(mob,(posfX * TITLE_SIZE,posfY * TITLE_SIZE))
            return posfX,posfY




    while loop==True:
        print("bas :",bas,"droite : ",droite)
        """
        Detection touche
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    loop = False
                elif event.key == pygame.K_UP:
                    direction = 'haut'
                elif event.key == pygame.K_DOWN:
                    direction = 'bas'
                elif event.key == pygame.K_RIGHT:
                    direction = 'droite'
                elif event.key == pygame.K_LEFT:
                    direction = 'gauche'
                elif event.key == pygame.K_x:
                    dash = 1

        """
        Fonction Dirrection/Déplacement/Animation

        """

        if direction == 'droite':

            start2 = time.time()
            end = 0
            while end <= 0.033 :
                end = time.time() - start2
            countTemps3 += 0.5

            if droite+1 >= 11:
                print("déplacement impossible")
                countTemps3 = 0
                direction = ''
            elif countTemps3 >= 0.5 and countTemps3 <= 1:
                player = 12
                joueurX += 0.25
                posY = joueurY
            elif countTemps3 >= 1 and countTemps3 <= 1.5:
                player = 13
                joueurX += 0.25
                posY = joueurY
            elif countTemps3 >= 1.5 and countTemps3 <= 1.9:
                player = 14
                joueurX += 0.25
                posY = joueurY

            elif countTemps3 >= 2 and countTemps3 <= 2.1:
                player = 15
                joueurX += 0.25
                posY = joueurY
                countTemps3 = 0
                direction =''
                droite += 1
                joueurX = int(joueurX)

            if posY != joueurY:
                countTemps3 = 0
                direction =''
                joueurX = int(joueurX)

        if direction == 'gauche':
            start4 = time.time()
            end = 0
            while end <= 0.033 :
                end = time.time() - start4
            countTemps4 += 0.5

            if droite-1 <= 0:
                print("déplacement impossible")
                countTemps4 = 0
                direction = ''
            elif countTemps4 >= 0.5 and countTemps4 <= 1:
                player = 16
                joueurX -= 0.25
                posY = joueurY
            elif countTemps4 >= 1 and countTemps4 <= 1.5:
                player = 17
                joueurX -= 0.25
                posY = joueurY
            elif countTemps4 >= 1.5 and countTemps4 <= 1.9:
                player = 18
                joueurX -= 0.25
                posY = joueurY
            elif countTemps4 >= 2 and countTemps4 <= 2.1:
                player = 19
                joueurX -= 0.25
                posY = joueurY
                countTemps4 = 0
                direction =''
                joueurX = int(joueurX)
                droite -= 1
            if posY != joueurY:
                countTemps4 = 0
                direction =''
                joueurX = int(joueurX)

        if direction == 'haut':
            start3 = time.time()
            end = 0
            while end <= 0.033 :
                end = time.time() - start3
            countTemps5 += 0.5

            if bas-1 <= 1:
                print("déplacement impossible")
                countTemps5 = 0
                direction = ''
            elif countTemps5 >= 0.5 and countTemps5 <= 1:
                player = 20
                joueurY -= 0.25
                posX = joueurX
            elif countTemps5 >= 1 and countTemps5 <= 1.5:
                player = 21
                joueurY -= 0.25
                posX = joueurX
            elif countTemps5 >= 1.5 and countTemps5 <= 1.9:
                player = 22
                joueurY -= 0.25
                posX = joueurX
            elif countTemps5 >= 2 and countTemps5 <= 2.1:
                player = 23
                joueurY -= 0.25
                posX = joueurX
                countTemps5 = 0
                direction =''
                joueurY = int(joueurY)
                bas -= 1
            if posX != joueurX:
                countTemps5 = 0
                direction = ''
                joueurY = int(joueurY)

        if direction == 'bas':
            start3 = time.time()
            end = 0
            while end <= 0.033 :
                end = time.time() - start3
            countTemps6 += 0.5

            if bas+1 == 13:
                print("déplacement impossible")
                countTemps6 = 0
                direction = ''
            elif countTemps6 >= 0.5 and countTemps6 <= 1:
                player = 24
                joueurY += 0.25
                posX = joueurX
            elif countTemps6 >= 1 and countTemps6 <= 1.5:
                player = 25
                joueurY += 0.25
                posX = joueurX
            elif countTemps6 >= 1.5 and countTemps6 <= 1.9:
                player = 26
                joueurY += 0.25
                posX = joueurX
            elif countTemps6 >= 2 and countTemps6 <= 2.1:
                player = 27
                joueurY += 0.25
                posX = joueurX
                countTemps6 = 0
                direction =''
                joueurY = int(joueurY)
                bas += 1
            if posX != joueurX:
                countTemps6 = 0
                direction = ''
                joueurY = int(joueurY)


        """
        Fonction attaque
        """

        if dash == 1:
            if cooldown(0.033) == 'passed':
                countTemps += 1
            player = 35
            dash = 1
            if countTemps >= 30:
                countTemps = 0
                print(cooldownDash)
                print("dash")
                dash = 0
                player = 12


        """
        Fonction fin attaque (relever épée)
        """

        if attaque == 1 and cooldownAtk == 1:
            player = 14
            cooldownAtk = 0
            attaque = 0
            print("attaque")



        """
        Fonction detection coffre
        """
        if cooldown(0.033) == 'passed':
                countTemps2 += 1

        numeroTile = niveauVierge[int(joueurY)][int(joueurX)]
        if numeroTile == 0:
            coffre = 1
            if countTemps2 >= 30:
                countTemps2 = 0
                cooldownCoffre = 1

        if coffre == 1 and cooldownCoffre == 1:
            cooldownCoffre = 1
            cooldownCoffre = 0
            print("vous êtes sur le coffre")
            loop = False
            coffre = 0

        """
        Appel Des Différentes Fonctions
        """

        fenetre.fill((0,0,0))
        chargetiles(tiles)
        afficheNiveau(niveauVierge)
        affichePac(player)


        """
        Fonction + Appel du déplacement de l'énnemie
        """
        posfX1,posfY1 = deplaceEnnemie((posfX1+0.5)%10,posfY1,32)
        posfX2,posfY2 = deplaceEnnemie((posfX2+0.5)%10,posfY2,33)
        posfX3,posfY3 = deplaceEnnemie((posfX3+0.5)%10,posfY3,34)


        """
        Detecte Game Over
        """

        if vieJoueur <= 0:
            loop = False

        pygame.display.update()

    pygame.quit()
"""
Menu Du Jeux
"""
def menu():
    continuer = 1
    choix = ''
    print("-----------------------------------------------------")
    print("1  - Jouer Au Jeu")
    print("2 - Quitter")
    print("-----------------------------------------------------")
    while continuer == 1:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        choix = '1'
        if choix == '1':
            main()
            continuer = 0
        elif choix == '2':
            print("Au Revoir")
            continuer = 0
            pygame.quit()


"""
Execution
"""
menu()