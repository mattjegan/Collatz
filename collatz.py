## collatz.py
## Written by Matthew Egan
## Written on Friday 28th March
##
## Displays a visual representation of the 
## relationship between the length of Collatz sequences
## as n -> infinity
##
## More info: http://en.wikipedia.org/wiki/Collatz_conjecture

import pygame
from pygame.locals import *
import math
import time

def main():
    ## The upper limit of the domain
    WIDTH = 1000000
    
    ## Used later to store the maximum length and
    ## determine scaling factors
    HEIGHT = 1

    ## The coefficient of the ln(x) line
    LOGMULT = 15

    ## Maximum window width and scaling factor
    PIXWIDTH = 1800
    DIV = float(PIXWIDTH)/float(WIDTH)

    ## Value at which milestones/lines will be placed
    MILESTONE = 250000

    maxLength = 0
    rangeVals = []
    
    ## Used to time the calculations
    startTime = time.time()
    
    ## Get all the points
    for x in xrange(0, WIDTH):
        if collatz(x) > HEIGHT:
            HEIGHT = collatz(x)
        if collatz(x) > maxLength:
            maxLength = collatz(x)
        rangeVals.append(collatz(x))

    ## Print time taken to compute
    end = time.time()
    print "It took:", str(end - startTime)

    ## Add padding to allow for easier viewing
    HEIGHT += 20

    ## Maximum window height and scaling factor
    PIXHEIGHT = 1000
    HDIV = float(PIXHEIGHT)/float(HEIGHT)

    ## Initialise the window and set the title of the window
    screen = pygame.display.set_mode((PIXWIDTH, PIXHEIGHT), 0, 32)
    pygame.display.set_caption("Collatz Conjecture")

    ## Application Loop
    running = True
    while running:
        ## Event Loop
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            ## Press 'a' to lower the coefficient of ln(x)
            ## Press 's' to raise the coefficient of ln(x)
            elif event.type == KEYDOWN:
                if event.key == K_a:
                    LOGMULT -= 1
                elif event.key == K_s:
                    LOGMULT += 1

        ## Fill the screen with black
        screen.fill((0, 0, 0))

        ## Render program parameters: domain, range, milestones, coef of ln(x)
        displayText(screen, "Domain: [0, " + str(WIDTH) + "]", (0, 0), (255, 255, 0))
        displayText(screen, "Range: [0, " + str(maxLength) + "]", (0, 20), (255, 255, 0))
        displayText(screen, "Milelines: mod " + str(MILESTONE), (0, 40), (255, 255, 0))
        displayText(screen, "f(x) = " + str(LOGMULT) + "*ln(x)", (0, 60), (0, 0, 255))

        ## Draw f(x) = LOGMULT*ln(x)
        for x in xrange(1, PIXWIDTH):
            pygame.draw.line(screen, (0, 0, 255), (x, (PIXHEIGHT-((LOGMULT*math.log(x))*HDIV))), (x, (PIXHEIGHT-((LOGMULT*math.log(x))*HDIV))))

        ## Draw all Collatz points
        for x, y in enumerate(rangeVals):
            ## Draw milelines every MILESTONE value
            if int(x*DIV) % int(MILESTONE*DIV) == 0:
                pygame.draw.line(screen, (255, 0, 0), (x*DIV, 0), (x*DIV, PIXHEIGHT))
            ## Draw a pixel at every Collatz point
            pygame.draw.line(screen, (255, 180, 70), (x*DIV, (PIXHEIGHT-(y*HDIV))), (x*DIV, (PIXHEIGHT-(y*HDIV))))
        
        ## Update changes to the window
        pygame.display.update()


## Function that computes the length of
## any Collatz sequence given the initial
## value as a natural number
def collatz(number):
    height = 0
    while number != 1:
        if number == 0:
            break
        if number % 2 == 0:
            number /= 2
        else:
            number = number*3 + 1
        height += 1

    return height

## Function to render text on the window
## and increase code reusability
def displayText(screen, text, pos, colour):
    pygame.font.init()
    font = pygame.font.Font(None, 16)
    text = font.render(text, 1, colour)
    screen.blit(text, pos)

## Calls the main function if the program is running independantly
if __name__ == "__main__": main()
