import pygame, sys, time, random
from pygame.locals import *


TRUE = 1
FALSE = 0
isFirstTimeCall = TRUE
letter = ''
user_text = []
check_text = []
check_text = ''
reStart = FALSE
isGameOver = FALSE
chances_left = 6
correct_entry = 0
wrong_guess = 0
isWordPresent = FALSE
    
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)
CYAN = (0,255,255)

DISPLAYSURF = pygame.display.set_mode((860,640),0,32)

pygame.init()

backGround = pygame.image.load("Data/Images/hangMan_start.png")
DISPLAYSURF.blit(backGround,(0,0))
pygame.display.update()



def text_on_screen(text,pos_x,pos_y):
    text_font = pygame.font.SysFont(None, 40)
    text_area = text_font.render(text, True, (255, 0, 0))
    text_positon = text_area.get_rect()
    text_positon.centerx = pos_x
    text_positon.centery = pos_y
    DISPLAYSURF.blit(text_area,text_positon)
    pygame.display.update()

def HangMan(letter,selected_word):

    global isGameOver
    global chances_left
    global correct_entry
    global wrong_guess
    global isWordPresent
    global check_text
    global reStart

    isGameOver = FALSE
    
    print (" RESTART STAT ",reStart)
    if reStart == TRUE:
        print (" RESTART ")
        isGameOver = FALSE
        chances_left = 6
        correct_entry = 0
        wrong_guess = 0
        reStart = FALSE
        del user_text[:]
        isWordPresent = FALSE

    print (selected_word)
    for alphabet in range(len(selected_word)):
        if selected_word[alphabet] == letter:
            correct_entry = correct_entry + 1
            if letter in user_text:
                correct_entry 
            else:
                user_text.insert(correct_entry,letter)
            isWordPresent = TRUE
    
    # DECREMENT USER CHANCES IS WRONG ANSWER
    if isWordPresent == FALSE:
        chances_left = chances_left - 1
        
        wrong_guess = wrong_guess + 1
            
        if wrong_guess == 1:
            image = pygame.image.load("Data/Images/logocabeza.png")
            DISPLAYSURF.blit(image,(0,0))
                
        if wrong_guess == 2:
            image = pygame.image.load("Data/Images/logopalo.png")
            DISPLAYSURF.blit(image,(0,0))
                
        if wrong_guess == 3:
            image = pygame.image.load("Data/Images/logobrazo1.png")
            DISPLAYSURF.blit(image,(0,0))
                
        if wrong_guess == 4:
            image = pygame.image.load("Data/Images/logobrazo2.png")
            DISPLAYSURF.blit(image,(0,0))
                
        if wrong_guess == 5:
            image = pygame.image.load("Data/Images/logopierna1.png")
            DISPLAYSURF.blit(image,(0,0))
                
        if wrong_guess == 6:
            image = pygame.image.load("Data/Images/final.png")
            DISPLAYSURF.blit(image,(0,0))
            pygame.display.update()
            time.sleep(1)
    
    pygame.display.update()

    indices = 0
    for alphabet in range(len(user_text)):
        Posx = 200
        Posy = 570
        indices = 0
        for index in range(len(selected_word)):
            if user_text[alphabet] == selected_word[index]:
                text_on_screen(selected_word[index],(Posx+(indices*25)),Posy)
                text_on_screen("",(Posx+(indices*25)),(Posy-10))
                pygame.display.update()
            else:
                text_on_screen("_",(Posx+(indices*25)),Posy)
                text_on_screen("",(Posx+(indices*25)),(Posy-10))
                pygame.display.update()
            indices = indices + 1

    if len(user_text) == 0:
        for index in range(len(selected_word)):
            text_on_screen("_",(200+(index*25)),570)
            text_on_screen("",(200+(index*25)),(560))
            pygame.display.update()
        
    print (" USER ",user_text, len(user_text), len(selected_word),correct_entry)

    isWordPresent = FALSE

    if correct_entry == len(selected_word):
        isGameOver = TRUE
        correct_entry = 0
        DISPLAYSURF.fill(CYAN)
        text_on_screen(" YOU WON !!!!!",400,300)
        pygame.display.update()
        time.sleep(1)

    if( wrong_guess == 6 and not(correct_entry == len(selected_word))):
        wrong_guess = 0
        isGameOver = TRUE
        DISPLAYSURF.fill(CYAN)
        text_on_screen(" YOU LOST !!!!!",400,300)
        pygame.display.update()
        time.sleep(1)
        
    return isGameOver
    
def start_Game():
    global reStart
    selected_word = ''
   # letter = open('words.txt','r')
    letter = open('sample_words.txt','r')
    counter = 0
    isGameComplete = FALSE
# total word count in dictonary 354934, so to get a random word from Dictonary
    count = random.randint(1,2983)
    for line in letter:
        for word in line.split():
            counter = counter + 1
            if counter == count:
                selected_word = word
    time.sleep(1)
    backGround = pygame.image.load("Data/Images/logoinicio.png")
    DISPLAYSURF.blit(backGround,(0,0))
    pygame.display.update()
    
    if isFirstTimeCall:
        startPosx = 200
        startPosy = 570
        for index in range(len(selected_word)): 
            text_on_screen("_",(startPosx+(index*25)),startPosy)
            text_on_screen("",(startPosx+(index*25)),(startPosy-10))
            pygame.display.update()

    while True:
        for event in pygame.event.get():

            if (event.type==KEYDOWN and event.key == pygame.K_RETURN):
                isGameComplete = FALSE
                backGround = pygame.image.load("Data/Images/logoinicio.png")
                DISPLAYSURF.blit(backGround,(0,0))
                pygame.display.update()
                start_Game()
        
            if event.type==KEYDOWN :
                if event.unicode.lower() in ("abcdefghijklmnopqrstuvwxyz"):
                    isGameComplete = HangMan(event.unicode,selected_word)

            if isGameComplete:
                print("FINAL ")
                DISPLAYSURF.fill(WHITE)
                text_on_screen(" PRESS ENTER TO CONTINUE OR ESCAPE TO QUIT", 400,300)
                text_on_screen(" THE WORD WAS : ",200,200)
                text_on_screen(selected_word,500,200)
                reStart = TRUE
                
                if (event.type==KEYDOWN and event.key == pygame.K_RETURN):
                    print (" GAME RESTARTED ",reStart)
                    start_Game()
                if (event.type==KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit(0)
                

start_Game()
