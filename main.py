import pygame
import sys, random, os
from pygame.locals import*
from random import randint
os.system("cls")
pygame.init()

BLACK=(0,0,0)
WHITE=(225,225,225)

#impostazione finestra

window_size= (850, 640)
screen= pygame.display.set_mode(window_size)
clock=pygame.time.Clock()
fps= 50
Font = pygame.font.SysFont("font.ttf", 50)
pygame.display.set_caption("progetto recupero")

#load delle immagini

sfondo_surface = pygame.image.load("sfondo.png").convert()
terreno_surface= pygame.image.load("terreno.png").convert()

mostro2_surf = pygame.image.load("mostro2.png").convert_alpha()
original_width, original_height = mostro2_surf.get_size()
larghezza2 = original_width // 19
altezza2 = original_height // 19
mostro2_rect=mostro2_surf.get_rect(topleft= (480,410))


mostro1_surf = pygame.image.load("mostro1.png").convert_alpha()
original_width, original_height = mostro1_surf.get_size()
larghezza1 = original_width // 19
altezza1 = original_height // 19
mostro1_rect=mostro1_surf.get_rect(topleft= (840,410))

fantasmino_surf = pygame.image.load("fantasmino.png").convert_alpha()
original_width, original_height = fantasmino_surf.get_size()
larghezza3 = original_width // 3
altezza3 = original_height // 3
personaggio_rect=fantasmino_surf.get_rect(topleft= (0,370))


testo_surface= Font.render('score:', False, 'BLACK')
gameover_surface= Font.render('GAME OVER', False, 'WHITE')

#scalo le immagini

immagine_scalata1_surf = pygame.transform.scale(mostro1_surf, (larghezza1, altezza1))
immagine_scalata1_surf_x_pos=500

immagine_scalata2_surf = pygame.transform.scale(mostro2_surf, (larghezza2, altezza2))
immagine_scalata2_surf_x_pos=800

immagine_scalata3_surf = pygame.transform.scale(fantasmino_surf, (larghezza3, altezza3))

score=0
incrementa_punteggio = pygame.USEREVENT + 1
pygame.time.set_timer(incrementa_punteggio, 1000)

salto=False
velocita=30
gravita=0.9
velocita_y=0

#ciclo principale

def aggiorna(): 
    pygame.display.update()
    clock.tick(fps)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == incrementa_punteggio:
            score += 1
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not salto:
                salto = True
                velocita_y = -velocita
    
    if salto:
        velocita_y += gravita
        personaggio_rect.y += velocita_y

    if personaggio_rect.y >= 370:
            personaggio_rect.y = 370
            salto = False



    screen.blit(sfondo_surface, (0,0))
    screen.blit(terreno_surface, (0,500))
    screen.blit(testo_surface, (365, 30))
     
    score_text = Font.render(str(score), True, BLACK)

    mostro1_rect.x -= 3.5
    if mostro1_rect.x < -180: 
        mostro1_rect.x = 900
    screen.blit(immagine_scalata1_surf, mostro1_rect) 

    screen.blit(immagine_scalata3_surf, personaggio_rect) 
    
    mostro2_rect.x -= 3.5
    if mostro2_rect.x < -180: 
        mostro2_rect.x = 857
    screen.blit(immagine_scalata2_surf, mostro2_rect) 

    pygame.key.get_pressed

    screen.blit(score_text, (477,32))
    
    # if(personaggio_rect.colliderect(mostro1_rect)) and (personaggio_rect.colliderect(mostro2_rect)) :
    #     screen.fill(BLACK)
    #     screen.blit(gameover_surface, (365, 250))

    print(personaggio_rect.colliderect(mostro2_rect))

    aggiorna()


