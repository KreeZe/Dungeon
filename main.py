#Jeu Fait Par Yamis MANFALOTI

"""
Librairies
"""

import pygame
from random import*

"""
Initialisation pygame + paramètre
"""

hauteur = 14
largeur = 12
TITLE_SIZE = 48
pygame.init()
#infoObject = pygame.display.Info()
#fenetre = pygame.display.set_mode((infoObject.current_w-100, infoObject.current_h-100))
fenetre = pygame.display.set_mode((largeur*TITLE_SIZE, (hauteur+1)*TITLE_SIZE))
pygame.display.set_caption("Jeu")
font = pygame.font.Font('freesansbold.ttf', 20)

"""
Fonction Main
"""

def main():
    """
    Initialisation Variable MaiN
    """
    loop = True
    tiles=[]
    NB_TILES = 14
    hauteur = 14
    largeur = 12
    TITLE_SIZE = 48
    joueurX = 1
    joueurY = 2

    niveauVierge = [
    [8 ,4 ,4 ,4 ,4 ,4 ,4 ,4 ,4 ,4 ,4 ,9 ],
    [1 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,2 ],
    [1 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,2 ],
    [1 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,2 ],
    [1 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,2 ],
    [1 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,2 ],
    [1 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,2 ],
    [1 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,2 ],
    [1 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,2 ],
    [1 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,2 ],
    [1 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,2 ],
    [1 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,2 ],
    [1 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,2 ],
    [10,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,11] ]

    def chargetiles(tiles): #fonction permettant de charger les images tiles dans une liste tiles[]
        for n in range(0,NB_TILES):
            tiles.append(pygame.image.load('data/'+str(n)+'.png'))
        for i in range(0,3):
            tiles.append(pygame.image.load('data/demon/mob'+str(i)+'.png'))

    def afficheNiveau(niveau): #affiche le niveau a partir de la liste a deux dimensions niveau[][]
        for y in range(hauteur):
            for x in range(largeur):
                fenetre.blit(tiles[niveau[y][x]],(x*TITLE_SIZE,y*TITLE_SIZE))

    def affichePac(numero):  #affiche le pacman en position joueurX et joueurY
        fenetre.blit(tiles[numero],(joueurX * TITLE_SIZE,joueurY * TITLE_SIZE-5))

    while loop==True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    numeroTile = niveauVierge[joueurY-1][joueurX]
                    print("up",numeroTile,end=':')
                    if (numeroTile == 7 ):
                        joueurY -= 1
                        print("deplacement possible",joueurX,joueurY)
                    else:
                        print("deplacement impossible")
                elif event.key == pygame.K_DOWN:
                    numeroTile = niveauVierge[joueurY+1][joueurX]
                    print("up",numeroTile,end=':')
                    if (numeroTile == 7 ):
                        joueurY += 1
                        print("deplacement possible",joueurX,joueurY)
                    else:
                        print("deplacement impossible")
                elif event.key == pygame.K_LEFT:
                    numeroTile = niveauVierge[joueurY][joueurX-1]
                    print("up",numeroTile,end=':')
                    if (numeroTile == 7 ):
                        joueurX -= 1
                        print("deplacement possible",joueurX,joueurY)
                    else:
                        print("deplacement impossible")
                elif event.key == pygame.K_RIGHT:
                    numeroTile = niveauVierge[joueurY][joueurX+1]
                    print("up",numeroTile,end=':')
                    if (numeroTile == 7 ):
                        joueurX += 1
                        print("deplacement possible",joueurX,joueurY)
                    else:
                        print("deplacement impossible")




    fenetre.fill((0,0,0))
    chargetiles(tiles)
    afficheNiveau(niveauVierge)
    affichePac(12)

    pygame.display.update() #mets à jour la fentre graphique




"""
Menu Du Jeux
"""

def menu():
    print("-----------------------------------------------------")
    print("1  - Jouer Au Jeu")
    print("2 - Quitter")
    print("-----------------------------------------------------")
    choix = str(input("choix"))
    if choix == '1 ':
        main()
    elif choix == '2':
        print("Au Revoir")
        pygame.quit()


"""
Execution
"""

main()