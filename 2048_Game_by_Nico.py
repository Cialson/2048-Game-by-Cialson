import pygame
from random import*
import time
import os

pygame.init()

if os.path.exists("Best score.txt"):
    with open("Best score.txt", "r") as best:
        l_best_score = best.readlines()
        best_score = l_best_score[0]
    best.close()
else:
    best_score = 0

nouveau = False
verif = False
verif_2 = False
victoir = False
bloc_mort = False
mort = False
verif_fin = False
bloc_vict = False
valeur_case = []
case_p = []
add = []
coor_case = []
R = 255
G = 255
B = 255
taille = 120
ancien = 16
pre = 16
bloc_add = 1
bloc_R = 0
valeur = 0
UP = 0
DOWN = 0
LEFT = 0
RIGHT = 0
depl = 0
num_c = 0
rejouer = 0
score = 0
debut = 0
num = 0
bloc = 0
bloc_app = 0
bloc_bout = 0
pas_mort = 0
contour_color = (77, 109, 100)
contour_color_2 = (49, 66, 61)
interieur_color = (112, 153, 140)
ecrit_color = (125, 0, 255)
fond_color = (32, 144, 122)
start_color = (255, 255, 255)
vert_color = (20, 142, 12)


def plateau():
    x = 300
    y = 40
    pygame.draw.rect(window, interieur_color, pygame.Rect(295, 35, 510, 510))
    pygame.draw.rect(window, contour_color, pygame.Rect(295, 35, 510, 510), 9)
    for i in range(0, 16):
        if i == 4 or i == 8 or i == 12:
            x = 300
            y += 125
            valeur_case.append(valeur)
            coor_case.append(x)
            coor_case.append(y)
            pygame.draw.rect(window, contour_color, pygame.Rect(x, y, 125, 125), 9)
            x += 125
        else:
            valeur_case.append(valeur)
            coor_case.append(x)
            coor_case.append(y)
            pygame.draw.rect(window, contour_color, pygame.Rect(x, y, 125, 125), 9)
            x += 125


image = pygame.image.load("2048.png")
pygame.display.set_icon(image)
pygame.display.set_caption("2048 Game by Nico")
window = pygame.display.set_mode((850, 600))
window.fill(fond_color)
image = pygame.image.load("2048P.png")
image.convert()
pygame.transform.scale
window.blit(image, [30, 310])
font = pygame.font.SysFont("cambria", 45)
text = font.render("Best score : ", False, ecrit_color)
text_2 = font.render(str(best_score), False, ecrit_color)
window.blit(text, [15, 20])
window.blit(text_2, [15, 70])
bouton = pygame.draw.rect(window, contour_color, pygame.Rect(20, 125, 250, 80), 5)
font = pygame.font.SysFont("cambria", 70)
text = font.render("Jouer", False, ecrit_color)
window.blit(text, [60, 115])
plateau()
pygame.display.flip()
running = True


def deplacement():
    bloc_R = 0
    R = 255
    G = 255
    B = 255
    couleur = 2
    while couleur != valeur:
        if R == 255 and bloc_R == 0:
            R = 125
        elif R == 125 and bloc_R == 0:
            R = 0
        elif R == 0 and bloc_R == 0:
            if B == 255:
                B = 125
            elif B == 125:
                B = 0
            elif B == 0:
                bloc_R = 1

        if R == 0 and bloc_R == 1:
            R = 125
        elif R == 125 and bloc_R == 1:
            R = 255
        elif R == 255 and bloc_R == 1:
            if G == 255:
                G = 125
            elif G == 125:
                G = 0
            elif G == 0:
                if B == 0:
                    B = 125
                elif B == 125:
                    B = 255
                elif B == 255:
                    bloc_R = 2

        if R == 255 and bloc_R == 2:
            R = 125
        elif R == 125 and bloc_R == 2:
            R = 0
        elif R == 0 and bloc_R == 2:
            if B == 255:
                B = 125
            elif B == 125:
                B = 0

        couleur = couleur*2
    pygame.draw.rect(window, (R, G, B), pygame.Rect(coor_case[num_c*2] + 5, coor_case[num_c*2 + 1] + 5, 115, 115))
    if len(str(valeur)) == 1:
        font = pygame.font.SysFont("cambria", 100)
        if valeur > 4:
            text = font.render(str(valeur), False, start_color)
        else:
            text = font.render(str(valeur), False, contour_color_2)
        window.blit(text, [coor_case[num_c*2] + 30, coor_case[num_c*2 + 1]])
    if len(str(valeur)) == 2:
        font = pygame.font.SysFont("cambria", 80)
        text = font.render(str(valeur), False, start_color)
        window.blit(text, [coor_case[num_c*2] + 15, coor_case[num_c*2 + 1] + 10])
    if len(str(valeur)) == 3:
        font = pygame.font.SysFont("cambria", 65)
        text = font.render(str(valeur), False, start_color)
        window.blit(text, [coor_case[num_c*2] + 5, coor_case[num_c*2 + 1] + 20])
    if len(str(valeur)) == 4:
        font = pygame.font.SysFont("cambria", 47)
        text = font.render(str(valeur), False, start_color)
        window.blit(text, [coor_case[num_c*2] + 7, coor_case[num_c*2 + 1] + 30])
    if len(str(valeur)) == 5:
        font = pygame.font.SysFont("cambria", 38)
        text = font.render(str(valeur), False, start_color)
        window.blit(text, [coor_case[num_c*2] + 5, coor_case[num_c*2 + 1] + 35])
    pygame.draw.rect(window, fond_color, pygame.Rect(15, 120, 275, 130))
    font = pygame.font.SysFont("cambria", 50)
    text = font.render("Score : ", False, ecrit_color)
    text_2 = font.render(str(score), False, ecrit_color)
    window.blit(text, [15, 130])
    window.blit(text_2, [15, 190])
    pygame.display.flip()


def apparetre():
    nouveau = False
    while nouveau == False:
        case = randint(0, 15)
        if valeur_case[case] == 0:
            nouveau = True
            valeur = choice([2, 4, 2])
            if valeur == 4:
                pygame.draw.rect(window, (R - 125, G, B), pygame.Rect(coor_case[case*2] + 5, coor_case[case*2 + 1] + 5, 115, 115))
            else:
                pygame.draw.rect(window, (R, G, B), pygame.Rect(coor_case[case*2] + 5, coor_case[case*2 + 1] + 5, 115, 115))
            font = pygame.font.SysFont("cambria", 100)
            text = font.render(str(valeur), False, contour_color_2)
            window.blit(text, [coor_case[case*2] + 30, coor_case[case*2 + 1]])
            valeur_case[case] = valeur


while running:
    mouse_xy = pygame.mouse.get_pos()
    clic = bouton.collidepoint(mouse_xy)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if os.path.exists("Best score.txt"):
                with open("Best score.txt", "r") as best:
                    if int(best_score) <= score:
                        font = pygame.font.SysFont("cambria", 60)
                        text = font.render("Best score battu!", False, vert_color)
                        window.blit(text, [320, 60])
                        n_best = open("Best score.txt", "w")
                        n_best.write(str(score))
                        best_score = score
                        n_best.close()
                    best.close()
            else:
                with open("Best score.txt", "w") as best:
                    if int(best_score) <= score:
                        font = pygame.font.SysFont("cambria", 60)
                        text = font.render("Best score battu!", False, vert_color)
                        window.blit(text, [320, 60])
                        n_best = open("Best score.txt", "w")
                        n_best.write(str(score))
                        best_score = score
                    best.close()
            running = False
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and clic and bloc_bout == 0:
            if mort == True:
                bloc_mort = False
                mort = False
                victoir = False
                valeur_case = []
                coor_case = []
                R = 255
                G = 255
                B = 255
                valeur = 0
                plateau()
            bloc_bout = 1
            score = 0
            pygame.draw.rect(window, fond_color, pygame.Rect(43, 235, 200, 77))
            pygame.draw.rect(window, fond_color, pygame.Rect(15, 20, 275, 130))
            font = pygame.font.SysFont("cambria", 45)
            text = font.render("Best score : ", False, ecrit_color)
            text_2 = font.render(str(best_score), False, ecrit_color)
            window.blit(text, [15, 20])
            window.blit(text_2, [15, 70])
            pygame.draw.rect(window, fond_color, pygame.Rect(15, 120, 275, 130))
            font = pygame.font.SysFont("cambria", 50)
            text = font.render("Score : ", False, ecrit_color)
            text_2 = font.render(str(score), False, ecrit_color)
            window.blit(text, [15, 130])
            window.blit(text_2, [15, 190])
            for i in range(0, 3):
                x = 300
                y = 40
                case = randint(0, 15)
                while ancien == case:
                    case = randint(0, 15)
                for z in range(0, 16):
                    valeur = 0
                    if z == 4 or z == 8 or z == 12:
                        x = 300
                        y += 125
                        x += 125
                    else:
                        x += 125
                    if z == case:
                        valeur = choice([2, 4, 2])
                        if valeur == 4:
                            pygame.draw.rect(window, (R - 125, G, B), pygame.Rect(x - 120, y + 5, 115, 115))
                        else:
                            pygame.draw.rect(window, (R, G, B), pygame.Rect(x - 120, y + 5, 115, 115))
                        font = pygame.font.SysFont("cambria", 100)
                        text = font.render(str(valeur), False, contour_color_2)
                        window.blit(text, [x - 93, y])
                        valeur_case[z] = valeur
                ancien = case
        elif event.type == pygame.KEYDOWN:
            UP = 0
            DOWN = 0
            LEFT = 0
            RIGHT = 0
            if event.key == pygame.K_UP:
                UP = 1
            if event.key == pygame.K_DOWN:
                DOWN = 1
            if event.key == pygame.K_LEFT:
                LEFT = 1
            if event.key == pygame.K_RIGHT:
                RIGHT = 1

    if UP == 1 and mort == False:
        add = []
        for i in range(4, 16):
            num_c = i
            if valeur_case[i] > 0:
                case_p = [i]
                while num_c >= 4:
                    if valeur_case[num_c-4] > 0:
                        case_p.append(num_c-4)
                    num_c = num_c - 4
                while len(case_p) > 0:
                    num_c = case_p[-1]
                    while valeur_case[num_c - 4] == 0 and num_c >= 4:
                        bloc_app = 1
                        pygame.draw.rect(window, interieur_color, pygame.Rect(coor_case[num_c*2] + 5, coor_case[num_c*2 + 1] + 5, 115, 115))
                        valeur = valeur_case[case_p[-1]]
                        num_c = num_c - 4
                        deplacement()
                        depl = 1
                    verif = num_c - 4 in add
                    verif_2 = num_c in add
                    if valeur_case[num_c - 4] == valeur_case[case_p[-1]] and num_c >= 4 and verif == False and verif_2 == False:
                        bloc_app = 1
                        pygame.draw.rect(window, interieur_color, pygame.Rect(coor_case[num_c*2] + 5, coor_case[num_c*2 + 1] + 5, 115, 115))
                        valeur = valeur_case[case_p[-1]]*2
                        score = score + valeur
                        num_c = num_c - 4
                        deplacement()
                        depl = 1
                        add.append(num_c)
                    if depl == 1:
                        valeur_case[case_p[-1]] = 0
                        valeur_case[num_c] = valeur
                        depl = 0
                    del case_p[-1]
        if bloc_app == 1:
            apparetre()
            verif_fin = 0 in valeur_case
            if verif_fin == False:
                pas_mort = 0
                for i in range(0, 16):
                    if i == 0 or i == 1 or i == 2 or i == 3:
                        if i == 0:
                            if valeur_case[i] == valeur_case[i+1] or valeur_case[i] == valeur_case[i+4]:
                                pas_mort = 1
                        elif i == 3:
                            if valeur_case[i] == valeur_case[i-1] or valeur_case[i] == valeur_case[i+4]:
                                pas_mort = 1
                        else:
                            if valeur_case[i] == valeur_case[i-1] or valeur_case[i] == valeur_case[i+1] or valeur_case[i] == valeur_case[i+4]:
                                pas_mort = 1
                    elif i == 4 or i == 8 or i == 12:
                        if i == 12:
                            if valeur_case[i] == valeur_case[i+1] or valeur_case[i] == valeur_case[i-4]:
                                pas_mort = 1
                        else:
                            if valeur_case[i] == valeur_case[i-4] or valeur_case[i] == valeur_case[i+1] or valeur_case[i] == valeur_case[i+4]:
                                pas_mort = 1
                    elif i == 7 or i == 11 or i == 15:
                        if i == 15:
                            if valeur_case[i] == valeur_case[i-1] or valeur_case[i] == valeur_case[i-4]:
                                pas_mort = 1
                        else:
                            if valeur_case[i] == valeur_case[i-4] or valeur_case[i] == valeur_case[i-1] or valeur_case[i] == valeur_case[i+4]:
                                pas_mort = 1
                    elif i == 13 or i == 11 or i == 14:
                        if valeur_case[i] == valeur_case[i-1] or valeur_case[i] == valeur_case[i+1] or valeur_case[i] == valeur_case[i-4]:
                                pas_mort = 1
                    else:
                        if valeur_case[i] == valeur_case[i-1] or valeur_case[i] == valeur_case[i+1] or valeur_case[i] == valeur_case[i-4] or valeur_case[i] == valeur_case[i+4]:
                                pas_mort = 1
                    if pas_mort == 1:
                        pas_mort = 0
                        break
                    if i == 15:
                        mort = True
            bloc_app = 0

    if DOWN == 1 and mort == False:
        add = []
        for i in range(0, 12):
            num_c = i
            if valeur_case[i] > 0:
                case_p = [i]
                while num_c <= 11:
                    if valeur_case[num_c+4] > 0:
                        case_p.append(num_c+4)
                    num_c = num_c + 4
                while len(case_p) > 0:
                    num_c = case_p[-1]
                    while num_c <= 11 and valeur_case[num_c + 4] == 0:
                        bloc_app = 1
                        pygame.draw.rect(window, interieur_color, pygame.Rect(coor_case[num_c*2] + 5, coor_case[num_c*2 + 1] + 5, 115, 115))
                        valeur = valeur_case[case_p[-1]]
                        num_c = num_c + 4
                        deplacement()
                        depl = 1
                    verif = num_c + 4 in add
                    verif_2 = num_c in add
                    if num_c <= 11 and valeur_case[num_c + 4] == valeur_case[case_p[-1]] and verif == False and verif_2 == False:
                        bloc_app = 1
                        pygame.draw.rect(window, interieur_color, pygame.Rect(coor_case[num_c*2] + 5, coor_case[num_c*2 + 1] + 5, 115, 115))
                        valeur = valeur_case[case_p[-1]]*2
                        score = score + valeur
                        num_c = num_c + 4
                        deplacement()
                        depl = 1
                        add.append(num_c)
                    if depl == 1:
                        valeur_case[case_p[-1]] = 0
                        valeur_case[num_c] = valeur
                        depl = 0
                    del case_p[-1]
        if bloc_app == 1:
            apparetre()
            verif_fin = 0 in valeur_case
            if verif_fin == False:
                pas_mort = 0
                for i in range(0, 16):
                    if i == 0 or i == 1 or i == 2 or i == 3:
                        if i == 0:
                            if valeur_case[i] == valeur_case[i+1] or valeur_case[i] == valeur_case[i+4]:
                                pas_mort = 1
                        elif i == 3:
                            if valeur_case[i] == valeur_case[i-1] or valeur_case[i] == valeur_case[i+4]:
                                pas_mort = 1
                        else:
                            if valeur_case[i] == valeur_case[i-1] or valeur_case[i] == valeur_case[i+1] or valeur_case[i] == valeur_case[i+4]:
                                pas_mort = 1
                    elif i == 4 or i == 8 or i == 12:
                        if i == 12:
                            if valeur_case[i] == valeur_case[i+1] or valeur_case[i] == valeur_case[i-4]:
                                pas_mort = 1
                        else:
                            if valeur_case[i] == valeur_case[i-4] or valeur_case[i] == valeur_case[i+1] or valeur_case[i] == valeur_case[i+4]:
                                pas_mort = 1
                    elif i == 7 or i == 11 or i == 15:
                        if i == 15:
                            if valeur_case[i] == valeur_case[i-1] or valeur_case[i] == valeur_case[i-4]:
                                pas_mort = 1
                        else:
                            if valeur_case[i] == valeur_case[i-4] or valeur_case[i] == valeur_case[i-1] or valeur_case[i] == valeur_case[i+4]:
                                pas_mort = 1
                    elif i == 13 or i == 11 or i == 14:
                        if valeur_case[i] == valeur_case[i-1] or valeur_case[i] == valeur_case[i+1] or valeur_case[i] == valeur_case[i-4]:
                                pas_mort = 1
                    else:
                        if valeur_case[i] == valeur_case[i-1] or valeur_case[i] == valeur_case[i+1] or valeur_case[i] == valeur_case[i-4] or valeur_case[i] == valeur_case[i+4]:
                                pas_mort = 1
                    if pas_mort == 1:
                        pas_mort = 0
                        break
                    if i == 15:
                        mort = True
            bloc_app = 0

    if LEFT == 1 and mort == False:
        add = []
        for i in range(0, 16):
            num_c = i
            if valeur_case[i] > 0 and i != 0 and i != 4 and i != 8 and i != 12:
                case_p = [i]
                while num_c != 0 and num_c != 4 and num_c != 8 and num_c != 12:
                    if valeur_case[num_c-1] > 0:
                        case_p.append(num_c-1)
                    num_c = num_c - 1
                while len(case_p) > 0:
                    num_c = case_p[-1]
                    while num_c <= 15 and valeur_case[num_c - 1] == 0 and num_c != 0 and num_c != 4 and num_c != 8 and num_c != 12:
                        bloc_app = 1
                        pygame.draw.rect(window, interieur_color, pygame.Rect(coor_case[num_c*2] + 5, coor_case[num_c*2 + 1] + 5, 115, 115))
                        valeur = valeur_case[case_p[-1]]
                        num_c = num_c - 1
                        deplacement()
                        depl = 1
                    verif = num_c - 1 in add
                    verif_2 = num_c in add
                    if num_c <= 15 and valeur_case[num_c - 1] == valeur_case[case_p[-1]] and verif == False and verif_2 == False and num_c != 0 and num_c != 4 and num_c != 8 and num_c != 12:
                        bloc_app = 1
                        pygame.draw.rect(window, interieur_color, pygame.Rect(coor_case[num_c*2] + 5, coor_case[num_c*2 + 1] + 5, 115, 115))
                        valeur = valeur_case[case_p[-1]]*2
                        score = score + valeur
                        num_c = num_c - 1
                        deplacement()
                        depl = 1
                        add.append(num_c)
                    if depl == 1:
                        valeur_case[case_p[-1]] = 0
                        valeur_case[num_c] = valeur
                        depl = 0
                    del case_p[-1]
        if bloc_app == 1:
            apparetre()
            verif_fin = 0 in valeur_case
            if verif_fin == False:
                pas_mort = 0
                for i in range(0, 16):
                    if i == 0 or i == 1 or i == 2 or i == 3:
                        if i == 0:
                            if valeur_case[i] == valeur_case[i+1] or valeur_case[i] == valeur_case[i+4]:
                                pas_mort = 1
                        elif i == 3:
                            if valeur_case[i] == valeur_case[i-1] or valeur_case[i] == valeur_case[i+4]:
                                pas_mort = 1
                        else:
                            if valeur_case[i] == valeur_case[i-1] or valeur_case[i] == valeur_case[i+1] or valeur_case[i] == valeur_case[i+4]:
                                pas_mort = 1
                    elif i == 4 or i == 8 or i == 12:
                        if i == 12:
                            if valeur_case[i] == valeur_case[i+1] or valeur_case[i] == valeur_case[i-4]:
                                pas_mort = 1
                        else:
                            if valeur_case[i] == valeur_case[i-4] or valeur_case[i] == valeur_case[i+1] or valeur_case[i] == valeur_case[i+4]:
                                pas_mort = 1
                    elif i == 7 or i == 11 or i == 15:
                        if i == 15:
                            if valeur_case[i] == valeur_case[i-1] or valeur_case[i] == valeur_case[i-4]:
                                pas_mort = 1
                        else:
                            if valeur_case[i] == valeur_case[i-4] or valeur_case[i] == valeur_case[i-1] or valeur_case[i] == valeur_case[i+4]:
                                pas_mort = 1
                    elif i == 13 or i == 11 or i == 14:
                        if valeur_case[i] == valeur_case[i-1] or valeur_case[i] == valeur_case[i+1] or valeur_case[i] == valeur_case[i-4]:
                                pas_mort = 1
                    else:
                        if valeur_case[i] == valeur_case[i-1] or valeur_case[i] == valeur_case[i+1] or valeur_case[i] == valeur_case[i-4] or valeur_case[i] == valeur_case[i+4]:
                                pas_mort = 1
                    if pas_mort == 1:
                        pas_mort = 0
                        break
                    if i == 15:
                        mort = True
            bloc_app = 0

    if RIGHT == 1 and mort == False:
        add = []
        for i in range(0, 16):
            num_c = i
            if valeur_case[i] > 0 and i != 3 and i != 7 and i != 11 and i != 15:
                case_p = [i]
                while num_c != 3 and num_c != 7 and num_c != 11 and num_c != 15:
                    if valeur_case[num_c+1] > 0:
                        case_p.append(num_c+1)
                    num_c = num_c + 1
                while len(case_p) > 0:
                    num_c = case_p[-1]
                    while num_c <= 14 and valeur_case[num_c + 1] == 0 and num_c != 3 and num_c != 7 and num_c != 11:
                        bloc_app = 1
                        pygame.draw.rect(window, interieur_color, pygame.Rect(coor_case[num_c*2] + 5, coor_case[num_c*2 + 1] + 5, 115, 115))
                        valeur = valeur_case[case_p[-1]]
                        num_c = num_c + 1
                        deplacement()
                        depl = 1
                    verif = num_c + 1 in add
                    verif_2 = num_c in add
                    if num_c <= 14 and valeur_case[num_c + 1] == valeur_case[case_p[-1]] and verif == False and verif_2 == False and num_c != 3 and num_c != 7 and num_c != 11:
                        bloc_app = 1
                        pygame.draw.rect(window, interieur_color, pygame.Rect(coor_case[num_c*2] + 5, coor_case[num_c*2 + 1] + 5, 115, 115))
                        valeur = valeur_case[case_p[-1]]*2
                        score = score + valeur
                        num_c = num_c + 1
                        deplacement()
                        depl = 1
                        add.append(num_c)
                    if depl == 1:
                        valeur_case[case_p[-1]] = 0
                        valeur_case[num_c] = valeur
                        depl = 0
                    del case_p[-1]
        if bloc_app == 1:
            apparetre()
            verif_fin = 0 in valeur_case
            if verif_fin == False:
                pas_mort = 0
                for i in range(0, 16):
                    if i == 0 or i == 1 or i == 2 or i == 3:
                        if i == 0:
                            if valeur_case[i] == valeur_case[i+1] or valeur_case[i] == valeur_case[i+4]:
                                pas_mort = 1
                        elif i == 3:
                            if valeur_case[i] == valeur_case[i-1] or valeur_case[i] == valeur_case[i+4]:
                                pas_mort = 1
                        else:
                            if valeur_case[i] == valeur_case[i-1] or valeur_case[i] == valeur_case[i+1] or valeur_case[i] == valeur_case[i+4]:
                                pas_mort = 1
                    elif i == 4 or i == 8 or i == 12:
                        if i == 12:
                            if valeur_case[i] == valeur_case[i+1] or valeur_case[i] == valeur_case[i-4]:
                                pas_mort = 1
                        else:
                            if valeur_case[i] == valeur_case[i-4] or valeur_case[i] == valeur_case[i+1] or valeur_case[i] == valeur_case[i+4]:
                                pas_mort = 1
                    elif i == 7 or i == 11 or i == 15:
                        if i == 15:
                            if valeur_case[i] == valeur_case[i-1] or valeur_case[i] == valeur_case[i-4]:
                                pas_mort = 1
                        else:
                            if valeur_case[i] == valeur_case[i-4] or valeur_case[i] == valeur_case[i-1] or valeur_case[i] == valeur_case[i+4]:
                                pas_mort = 1
                    elif i == 13 or i == 11 or i == 14:
                        if valeur_case[i] == valeur_case[i-1] or valeur_case[i] == valeur_case[i+1] or valeur_case[i] == valeur_case[i-4]:
                                pas_mort = 1
                    else:
                        if valeur_case[i] == valeur_case[i-1] or valeur_case[i] == valeur_case[i+1] or valeur_case[i] == valeur_case[i-4] or valeur_case[i] == valeur_case[i+4]:
                                pas_mort = 1
                    if pas_mort == 1:
                        pas_mort = 0
                        break
                    if i == 15:
                        mort = True
            bloc_app = 0

    victoir = 2048 in valeur_case
    if victoir == True and bloc_vict == False:
        bloc_vict = True
        font = pygame.font.SysFont("cambria", 65)
        text = font.render("Gagné !", False, vert_color)
        window.blit(text, [43, 235])

    if mort == True and bloc_mort == False:
        bloc_mort = True
        bloc_bout = 0
        s = pygame.Surface((500, 500))
        s.set_alpha(120)
        s.fill((255, 255, 255))
        window.blit(s, (300, 40))
        pygame.display.flip()
        font = pygame.font.SysFont("cambria", 70)
        text = font.render("GAME OVER!", False, (255, 0, 0))
        window.blit(text, [350, 180])
        bouton = pygame.draw.rect(window, ecrit_color, pygame.Rect(425, 310, 250, 80), 5)
        font = pygame.font.SysFont("cambria", 60)
        text = font.render("Rejouer", False, vert_color)
        window.blit(text, [440, 310])
        if os.path.exists("Best score.txt"):
            with open("Best score.txt", "r") as best:
                if int(best_score) < score:
                    font = pygame.font.SysFont("cambria", 60)
                    text = font.render("Best score battu!", False, vert_color)
                    window.blit(text, [320, 60])
                    n_best = open("Best score.txt", "w")
                    n_best.write(str(score))
                    best_score = score
                    n_best.close()
                best.close()
        else:
            with open("Best score.txt", "w") as best:
                if int(best_score) < score:
                    font = pygame.font.SysFont("cambria", 60)
                    text = font.render("Best score battu!", False, vert_color)
                    window.blit(text, [320, 60])
                    n_best = open("Best score.txt", "w")
                    n_best.write(str(score))
                    best_score = score
                best.close()

    UP = 0
    DOWN = 0
    LEFT = 0
    RIGHT = 0
    pygame.display.flip()
