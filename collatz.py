import pygame
from pygame.locals import *
import math
import time

def main():
    WIDTH = 100
    HEIGHT = 1

    LOGMULT = 15

    PIXWIDTH = 1800
    DIV = float(PIXWIDTH)/float(WIDTH)

    MILESTONE = 250000

    maxLength = 0
    rangeVals = []
    
    startTime = time.time()
    
    for x in xrange(0, WIDTH):
        if collatz(x) > HEIGHT:
            HEIGHT = collatz(x)
        if collatz(x) > maxLength:
            maxLength = collatz(x)
        rangeVals.append(collatz(x))

    end = time.time()
    print "It took:", str(end - startTime)

    HEIGHT += 20

    PIXHEIGHT = 1000
    HDIV = float(PIXHEIGHT)/float(HEIGHT)

    screen = pygame.display.set_mode((PIXWIDTH, PIXHEIGHT), 0, 32)
    pygame.display.set_caption("Collatz Conjecture")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_a:
                    LOGMULT -= 1
                elif event.key == K_s:
                    LOGMULT += 1

        screen.fill((0, 0, 0))

        displayText(screen, "Domain: [0, " + str(WIDTH) + "]", (0, 0), (255, 255, 0))
        displayText(screen, "Range: [0, " + str(maxLength) + "]", (0, 20), (255, 255, 0))
        displayText(screen, "Milelines: mod " + str(MILESTONE), (0, 40), (255, 255, 0))
        displayText(screen, "f(x) = " + str(LOGMULT) + "*ln(x)", (0, 60), (0, 0, 255))

        #pygame.draw.line(screen, (255, 0, 0), (0, PIXHEIGHT/2), (PIXWIDTH, PIXHEIGHT/2))

        ## Ln(x)
        for x in xrange(1, PIXWIDTH):
            pygame.draw.line(screen, (0, 0, 255), (x, (PIXHEIGHT-((LOGMULT*math.log(x))*HDIV))), (x, (PIXHEIGHT-((LOGMULT*math.log(x))*HDIV))))

        ## Collatz points
        for x, y in enumerate(rangeVals):

            if int(x*DIV) % int(MILESTONE*DIV) == 0:
                pygame.draw.line(screen, (255, 0, 0), (x*DIV, 0), (x*DIV, PIXHEIGHT))

            pygame.draw.line(screen, (255, 180, 70), (x*DIV, (PIXHEIGHT-(y*HDIV))), (x*DIV, (PIXHEIGHT-(y*HDIV))))



        pygame.display.update()


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

def displayText(screen, text, pos, colour):
    pygame.font.init()
    font = pygame.font.Font(None, 16)
    text = font.render(text, 1, colour)
    screen.blit(text, pos)


if __name__ == "__main__": main()
